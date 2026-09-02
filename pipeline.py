from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain


def run_research_pipeline(topic: str, on_progress=None) -> dict:
    """Run the 4-agent research pipeline.

    on_progress is an optional callback: on_progress(step_id, label, payload).
    Used by the Streamlit UI to show live stage updates. CLI still prints as before.
    """

    def emit(step_id: str, label: str, payload=None):
        print(f"\n{' =' * 50}")
        print(label)
        print("=" * 50)
        if on_progress:
            on_progress(step_id, label, payload)

    state = {"topic": topic}

    emit("search", "Step 1 — Search agent is gathering sources...")

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    state["search_results"] = search_result["messages"][-1].content
    print("\n search result", state["search_results"])
    emit("search_done", "Search complete", state["search_results"])

    emit("reader", "Step 2 — Reader agent is scraping top resources...")

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })

    state["scraped_content"] = reader_result["messages"][-1].content
    print("\nscraped_content\n", state["scraped_content"])
    emit("reader_done", "Reading complete", state["scraped_content"])

    emit("writer", "Step 3 — Writer is drafting the report...")

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })
    print("\n Final Report\n", state["report"])
    emit("writer_done", "Draft complete", state["report"])

    emit("critic", "Step 4 — Critic is reviewing the report...")

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })
    print("\n critic report \n", state["feedback"])
    emit("critic_done", "Review complete", state["feedback"])

    return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic :")
    run_research_pipeline(topic)    
