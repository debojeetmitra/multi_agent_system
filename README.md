# 🔬 Multi-Agent Research Lab

An AI-powered multi-agent research system that automatically searches the web, extracts relevant information, generates a structured research report, and uses a dedicated critic agent to review the generated output.

The project demonstrates how specialized AI agents can work together as an orchestrated pipeline instead of relying on a single LLM prompt.

## 🚀 Live Demo

**Live Application:** https://debojeet-multi-agent.streamlit.app

> Enter a research topic and let the multi-agent pipeline search, analyze, write, and review the report automatically.

---

## 📸 Screenshots

[Multi-Agent Research Lab]<img width="1366" height="768" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/50c66c3a-0abe-48ae-bbef-89ffef6453f8" />

[Generated Research Report]<img width="1366" height="768" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/fee0a2e8-b483-42ac-b29f-c596cb4989b3" />


[Critic Review]<img width="1366" height="768" alt="Screenshot (14)" src="https://github.com/user-attachments/assets/d5da3d47-4243-4520-bfff-475a226480d0" />

---

## ✨ Features

* 🔎 **Search Agent** — Searches the web for relevant information and sources.
* 📖 **Reader Agent** — Extracts and processes content from selected web pages.
* ✍️ **Writer Agent** — Generates a structured research report from the collected information.
* 🧐 **Critic Agent** — Reviews the generated report and provides feedback.
* 🔗 **Multi-Agent Pipeline** — Coordinates multiple specialized agents through a shared workflow.
* 📚 **Source-Based Reports** — Generated reports include references to the sources used during research.
* 🖥️ **Streamlit UI** — Interactive interface for entering research briefs and reviewing results.
* 📊 **Pipeline Metrics** — Displays agent count, search notes, scraped content, and report statistics.
* 📄 **Report Review** — Allows users to inspect the generated report and critic feedback.

---

## 🏗️ Architecture

```text
                 Research Brief
                       │
                       ▼
                ┌──────────────┐
                │ Search Agent │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ Reader Agent │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ Writer Agent │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ Critic Agent │
                └──────┬───────┘
                       │
                       ▼
              Final Research Report
                       │
                       ▼
                Streamlit Interface
```

### Pipeline Flow

1. The user provides a **research brief**.
2. The **Search Agent** discovers relevant web sources.
3. The **Reader Agent** extracts useful information from the selected pages.
4. The **Writer Agent** synthesizes the collected information into a structured report.
5. The **Critic Agent** evaluates the generated report.
6. The final report, sources, and critic feedback are presented through the Streamlit interface.

---

## 🛠️ Tech Stack

| Technology        | Purpose                                      |
| ----------------- | -------------------------------------------- |
| **Python**        | Core application development                 |
| **LangChain**     | LLM orchestration and agent/tool integration |
| **LLMs**          | Research, synthesis, and evaluation          |
| **Web Search**    | Finding relevant research sources            |
| **Web Scraping**  | Extracting webpage content                   |
| **Streamlit**     | Interactive web interface                    |
| **python-dotenv** | Environment variable management              |

---

## 📁 Project Structure

```text
multi_agent_system/
│
├── app.py                 # Streamlit application
├── pipeline.py            # Multi-agent research pipeline
├── agents.py              # Agent definitions and configurations
├── tools.py               # Search/scraping and custom tools
│
├── .streamlit/
│   └── config.toml        # Streamlit configuration
│
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Project configuration
├── pyrightconfig.json     # Python type-checking configuration
├── .gitignore
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/multi_agent_system.git
cd multi_agent_system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```powershell
.\venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and add the API keys required by the application.

```env
YOUR_API_KEY=your_api_key
```

> Never commit `.env` or API keys to GitHub.

### 6. Run the application

```bash
streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

## 🔐 Environment & Secrets

For local development, API credentials are loaded through environment variables.

For deployment, configure the required secrets through the hosting platform's secret management system.

The repository intentionally does **not** contain `.env` or API credentials.

---

## 📸 Application

The application provides a research dashboard where users can:

* Submit a research topic
* Track pipeline progress
* View search results
* Inspect scraped content
* Read the generated report
* Review critic feedback
* Inspect cited sources

---

## 🎯 Example

### Research Brief

```text
Impact of AI on the Job Market
```

### Pipeline

```text
Search
   ↓
Read
   ↓
Write
   ↓
Critique
```

### Output

The system generates a structured research report containing:

* Introduction
* Key findings
* Analysis
* Conclusion
* Sources
* Critic review

---

## 🧠 What I Learned

This project helped me understand and implement:

* Multi-agent AI architecture
* LangChain agent and tool orchestration
* LLM-based research workflows
* Web search and content extraction
* Prompt-driven report generation
* AI-generated content evaluation
* Shared state between pipeline stages
* Streamlit application development
* Environment and secret management
* Deploying an AI application

---

## 🚀 Future Improvements

* Add persistent research history
* Add PDF report export
* Introduce parallel research agents
* Add source credibility scoring
* Add RAG with a vector database
* Add human-in-the-loop approval before report generation
* Improve critic-based iterative refinement
* Add authentication and user-specific research history

---

## 👨‍💻 Author

**Debojeet Mitra**

Computer Science (AI & ML) | Backend & Generative AI Developer

* GitHub: https://github.com/debojeetmitra
* Portfolio: https://debojeet-portfolio.vercel.app/

---

## ⭐ If you find this project useful

Feel free to explore the code, try the live demo, or give the repository a star.
