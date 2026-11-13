# 💍 Multi-Agent Wedding Planner

An AI wedding planning assistant built with **LangChain**, **OpenAI**, **Tavily**, and **Streamlit**. A main planner agent coordinates specialized research subagents to turn a couple's preferences into a complete, client-ready wedding plan.

## ✨ Overview

The user provides:

- Preferences and style direction
- Budget and location
- Guest count
- Constraints and planning priorities
- Cultural details

The system then produces a full planning strategy with recommendations, timelines, risks, tradeoffs, and open questions.

## 🧠 Architecture

```
            ┌──────────────────────┐
            │  Main Planner Agent  │
            │    (orchestrator)    │
            └──────────┬───────────┘
          ┌────────────┴────────────┐
          ▼                         ▼
┌────────────────────┐   ┌────────────────────┐
│ Research Subagent 1│   │ Research Subagent 2│
│ Venues & Logistics │   │ Vendors & Budget   │
└─────────┬──────────┘   └─────────┬──────────┘
          └────────► Tavily ◄──────┘
                   Web Search
```

- **Main agent**: coordinates the subagents and synthesizes the final plan
- **Subagents**: use Tavily to gather current venue, vendor, logistics, budget, and market data

## 🛠️ Tech Stack

- Python
- LangChain
- OpenAI API
- Tavily Search API
- Streamlit (web interface)
- uv (dependency management)

## 📁 Project Structure

```
├── app.py        # Streamlit web app
├── main.py       # CLI entry point
├── agents.py     # Main agent and subagents
├── tools.py      # Tavily search tools
├── models.py     # Model configuration
├── prompts.py    # System prompts
└── pyproject.toml
```

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Med-Hajji/multi-agent-wedding-planner.git
cd multi-agent-wedding-planner
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file at the root of the project:

```
OPENAI_API_KEY=your_key
TAVILY_API_KEY=your_key
```

### 4. Run

**Streamlit app**

```bash
uv run streamlit run app.py
```

**CLI**

```bash
uv run main.py
```

## 📦 Output

A structured wedding plan including:

- Venue and vendor recommendations
- Budget breakdown
- Planning timeline
- Risks and tradeoffs
- Open questions for the couple

## 📚 What I Learned

- How multi-agent systems are structured and coordinated
- Delegating tasks to subagents with LangChain
- Integrating real-time web search into agents
- Building both a CLI and a Streamlit interface
