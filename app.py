import html
from pathlib import Path

import streamlit as st

from pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent Research Lab",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

CSS_PATH = Path(__file__).with_name("app.css")
st.html(CSS_PATH)

STEPS = [
    ("01", "Search", "Locate recent, reliable sources on the topic."),
    ("02", "Reader", "Open the strongest source and extract depth."),
    ("03", "Writer", "Compose a structured research report."),
    ("04", "Critic", "Score the draft and name what to improve."),
]


def init_state():
    defaults = {
        "result": None,
        "topic": "",
        "error": None,
        "running": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_state()

with st.sidebar:
    st.markdown("### The desk")
    st.markdown(
        """
        Four specialists run in sequence — same engine as the terminal pipeline.

        **01  Search** · Tavily web search  
        **02  Reader** · scrape a top URL  
        **03  Writer** · structured report  
        **04  Critic** · score and notes  
        """
    )
    st.divider()
    st.caption("Keys live in `.env` — OPENAI_API_KEY and TAVILY_API_KEY.")
    if st.button("Clear last run", use_container_width=True):
        st.session_state.result = None
        st.session_state.error = None
        st.session_state.topic = ""
        st.rerun()

st.html(
    """
    <div class="hero">
      <div class="eyebrow">Research operations</div>
      <h1>Multi-Agent Research Lab</h1>
      <p>Brief a topic. Search, Reader, Writer, and Critic produce a sourced report you can review and export.</p>
    </div>
    """
)

topic = st.text_input(
    "Research brief",
    placeholder="e.g. Impact of small language models on on-device AI",
    value=st.session_state.topic or "",
)
cols = st.columns([1.1, 3])
with cols[0]:
    run_clicked = st.button("Run research", type="primary", use_container_width=True)

if run_clicked:
    clean_topic = topic.strip()
    if not clean_topic:
        st.warning("Enter a research topic first.")
    else:
        st.session_state.topic = clean_topic
        st.session_state.error = None
        st.session_state.result = None

        progress = st.progress(0, text="Opening the lab…")
        status_box = st.status("Agents are working…", expanded=True)

        step_progress = {
            "search": 10,
            "search_done": 25,
            "reader": 35,
            "reader_done": 50,
            "writer": 60,
            "writer_done": 80,
            "critic": 88,
            "critic_done": 100,
        }

        def on_progress(step_id, label, payload=None):
            pct = step_progress.get(step_id, 50)
            progress.progress(min(pct, 100), text=label)
            if step_id.endswith("_done"):
                status_box.write(f"✓ {label}")
            else:
                status_box.write(f"⏳ {label}")

        try:
            with status_box:
                result = run_research_pipeline(clean_topic, on_progress=on_progress)
            progress.progress(100, text="Pipeline complete")
            status_box.update(label="Research complete", state="complete")
            st.session_state.result = result
        except Exception as exc:
            status_box.update(label="Pipeline failed", state="error")
            st.session_state.error = str(exc)

if st.session_state.error:
    st.error(f"The pipeline failed: {st.session_state.error}")

result = st.session_state.result
if result:
    safe_topic = html.escape(str(result.get("topic", st.session_state.topic)))
    st.html(f'<div class="ready">Report ready — <strong>{safe_topic}</strong></div>')

    search_n = len(result.get("search_results") or "")
    scrape_n = len(result.get("scraped_content") or "")
    report_n = len(result.get("report") or "")
    st.html(
        f"""
        <div class="stat-grid">
          <div class="stat"><div class="k">Agents</div><div class="v">04</div></div>
          <div class="stat"><div class="k">Search notes</div><div class="v">{search_n:,}</div></div>
          <div class="stat"><div class="k">Scraped text</div><div class="v">{scrape_n:,}</div></div>
          <div class="stat"><div class="k">Report length</div><div class="v">{report_n:,}</div></div>
        </div>
        """
    )

    tab_report, tab_critic, tab_search, tab_scrape = st.tabs(
        ["Report", "Critic review", "Search results", "Scraped content"]
    )

    with tab_report:
        st.markdown(result.get("report") or "_No report produced._")
        filename = f"research_{result.get('topic', 'topic').replace(' ', '_')[:40]}.md"
        st.download_button(
            "Download report as Markdown",
            data=result.get("report") or "",
            file_name=filename,
            mime="text/markdown",
        )

    with tab_critic:
        st.markdown(result.get("feedback") or "_No critic feedback._")

    with tab_search:
        st.text(result.get("search_results") or "No search results.")

    with tab_scrape:
        st.text(result.get("scraped_content") or "No scraped content.")
else:
    cards = "".join(
        f'<div class="stage"><div class="n">{n}</div><div class="rule"></div><h3>{name}</h3><p>{desc}</p></div>'
        for n, name, desc in STEPS
    )
    st.html(f'<div class="stage-grid">{cards}</div>')
    st.caption("Enter a brief above, then run research. Results stay here until you clear the desk.")
