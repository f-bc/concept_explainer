# concept_explainer

A simple AI-powered web application that explains unfamiliar concepts in **under 100 words**, adapting the explanation to the learner's background.

The application uses **Gradio** for the interface, **LangChain** for prompt templating and LLM interaction, and **Groq** to run the language model.

## ✨ Features

* 💡 Explain any concept in under 100 words
* 🎯 Adapt explanations to the user's background
* 🧩 Use intuitive analogies and practical examples
* 🤖 Powered by an LLM through Groq
* 🖥️ Simple Gradio web interface
* ⚙️ Easy dependency installation with `pyproject.toml`
* 🔐 API key managed through environment variables

## 🛠️ Tech Stack

* **Python**
* **Gradio** — Web interface
* **LangChain Core** — Prompt templates
* **LangChain Groq** — Groq LLM integration
* **Groq** — LLM inference
* **python-dotenv** — Environment variable management

## 📁 Project Structure

```text
concept_explainer/
│
├── app.py
├── pyproject.toml
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Setup

### 1. Clone the repository

```bash
git clone https://github.com/f-bc/concept_explainer.git
cd concept_explainer
```

### 2. Create a virtual environment

#### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

#### Windows

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install the dependencies

The project uses `pyproject.toml` to manage its dependencies.

```bash
pip install .
```

For development, you can use an editable installation:

```bash
pip install -e .
```

### 4. Configure the Groq API key

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_groq_api_key_here
```

You can use `.env.example` as a template.

### 5. Run the application

```bash
python app.py
```

Gradio will provide a local URL, typically:

```text
http://127.0.0.1:7860
```

Open the URL in your browser.

## 🖥️ How It Works

The application takes two inputs:

1. **Concept** — The topic the user wants to understand.
2. **Your Background** — The user's educational or technical background.

For example:

```text
Concept:
Roman Empire

Your Background:
High-school student
```

These inputs are inserted into a LangChain `PromptTemplate`.

The resulting prompt is sent to the Groq-hosted language model, which generates a concise explanation adapted to the provided background.

### Flow

```text
User
 │
 ├── Concept
 │
 └── Background
       │
       ▼
  PromptTemplate
       │
       ▼
    ChatGroq
       │
       ▼
   LLM Response
       │
       ▼
  Gradio Interface
```

## 🔐 Environment Variables

The application requires the following environment variable:

| Variable       | Description                         |
| -------------- | ----------------------------------- |
| `GROQ_API_KEY` | API key used to access the Groq API |

The application loads this variable using `python-dotenv`:

```python
from dotenv import load_dotenv

load_dotenv()
```

## 📦 Dependencies

Dependencies are defined in `pyproject.toml`, so users do not need to manually install each package.

Example:

```toml
[project]
name = "concept_explainer"
version = "0.1.0"
description = "A simple concept explanation app using Gradio, LangChain, and Groq"
requires-python = ">=3.10"
dependencies = [
    "gradio",
    "langchain-core",
    "langchain-groq",
    "python-dotenv"
]
```
