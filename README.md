# 🚀 AI CLI-Based LaTeX Generation System (`latex-ai`)

Hey team! Welcome to the repository. 🎉 

This project is all about building a terminal-native, AI-driven document engine. The core idea is simple: **we shouldn't have to manually fight with LaTeX boilerplate, packaging errors, or tables ever again.** Instead, we are building a Python CLI tool that lets users control, write, edit, and compile structured LaTeX documents entirely using natural language prompts right from the terminal.

The edits don't just vanish into the cloud—they happen **live, in real-time, on actual files** inside the workspace, so you can keep your favorite code editor open and watch the document change as you prompt the AI.

---

## 🧠 How the Magic Happens (The Pipeline)

Our CLI acts as a real-time bridge connecting four major components:

1. **The User ➔** Inputs a prompt (e.g., `latex-ai append "Add a chart comparing our speeds"`).
2. **The CLI Core (`Click`) ➔** Captures the command, parses the flags, and fetches project context.
3. **The LLM Engine (`DeepSeek`) ➔** Takes the prompt + file context and generates pure, smart LaTeX syntax.
4. **The File System (`fs_manager.py`) ➔** Edits, modifies, or appends the text directly onto the local `.tex` files.
5. **The Compiler (`compiler.py` + `latexmk`) ➔** Compiles the document to a PDF. If it crashes, it grabs the error log, passes it back to DeepSeek, and fixes the code automatically. 🤯

## 📁 Project Structure

```text
ai-latex-cli/
│
├── .github/
│   └── workflows/
│       ├── main-ci.yml
│       └── README.md
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── COMMAND_REFERENCE.md
│   └── README.md
│
├── src/
│   ├── api/
│   │   ├── deepseek.py
│   │   └── README.md
│   │
│   ├── cli/
│   │   ├── main.py
│   │   └── README.md
│   │
│   ├── core/
│   │   ├── fs_manager.py
│   │   ├── compiler.py
│   │   └── README.md
│   │
│   ├── __init__.py
│   └── README.md
├──tests/
│   ├──test_cli.py
│   ├──test_compiler.py
│   ├──test_deepseek.py
│   └──test_fs_manager.py
│  
├── templates/
│   ├── standard_article.tex
│   ├── ieee_paper.tex
│   ├── presentation.tex
│   ├── clinical_protocal.tex
│   └── README.md
│
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── FUTURE_SCOPE.md
├── README.md
├── PROJECT_VISION_AND_ROADMAP.md
├── requirements.txt
└── setup.py
```

## 🛠️ Quick Installation & Setup Guide

Before jumping in, make sure you have Python 3.10+ and a local LaTeX distribution installed. 

### 1. Download LaTeX & `latexmk` (If you don't have it)
Because the compilation happens locally on your machine, you need the actual tools:
* **Windows:** Download **MiKTeX** (`miktex.org/download`) + **Strawberry Perl** (`strawberryperl.com`) (Perl is required to run `latexmk`).
* **macOS:** Run `brew install --cask mactex`.
* **Linux:** Run `sudo apt update && sudo apt install texlive-full latexmk`.

### 2. Fork, Clone, and Setup Environment
```bash
# Clone your fork of the repo
git clone https://github.com/YOUR-USERNAME/ai-latex-cli.git
cd ai-latex-cli

# Fire up a virtual environment so dependencies don't clash globally
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install the dependencies + dev tools
pip install -r requirements.txt
