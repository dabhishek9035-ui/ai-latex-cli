# AI LaTeX CLI — Project Architecture & Vision Document

# 1. Project Overview

## What are we building?

We are building an AI-powered terminal-based CLI tool for generating VTU-formatted LaTeX reports and assignments.

The primary target audience is:

* VTU students
* Engineering students
* Academic report writers

The tool helps students convert rough markdown/text notes into properly structured VTU-compliant LaTeX projects.

The goal is to let students focus on content while the system handles formatting, structure, and LaTeX generation automatically.

Instead of manually formatting reports in Word or learning complicated LaTeX syntax, students can:

* provide metadata
* provide markdown content
* optionally use AI enhancement
* automatically generate a complete `.tex` project
* compiles the `.tex` to pdf

The generated project can then be:

* opened in Overleaf
* compiled locally
* edited manually if needed

---

# 2. Why are we building this?

## Problem Statement

VTU students regularly face:

* repetitive formatting work
* strict formatting rules
* inconsistent report structures
* difficulty learning LaTeX
* time wasted on margins/fonts/layout instead of actual content

Most students:

* already prepare rough notes/content
* use AI tools for research
* create markdown/text documents

But converting that into:

* institution-compliant reports
* professional formatting
* structured LaTeX documents

is painful and repetitive.

---

# 3. Core Idea

The user focuses on:

* ideas
* content
* research

The tool handles:

* VTU formatting
* margins
* title pages
* certificates
* section formatting
* LaTeX generation
* project structure

The philosophy is:

> Separate CONTENT from FORMAT.

---

# 4. Why CLI Instead of GUI/Web App?

We intentionally chose a terminal-first workflow because:

## Advantages of CLI

### Lightweight

No browser or heavy frontend needed.

### Developer-Friendly

Works naturally with:

* VSCode terminal
* Linux
* Git workflows
* Overleaf workflows

### Automation Friendly

Future scripting becomes possible.

### Faster Workflow

Interactive prompts are faster than navigating GUIs repeatedly.

### Better Architecture

Terminal apps naturally align with:

* file systems
* markdown processing
* LaTeX tooling

---

# 5. Technology Stack

## Main Language

Python

## Why Python?

* Easy CLI development
* Excellent AI ecosystem
* Strong markdown/text processing
* Huge LaTeX tooling support
* Fast prototyping
* Beginner-friendly for team collaboration

---

# 6. Core Libraries

## CLI Interface

### Typer

Used for:

* CLI commands
* command structure
* application flow

Reason:
Simple and clean CLI development.

---

## Terminal UI

### Rich

Used for:

* colors
* panels
* banners
* progress bars
* beautiful terminal experience

Reason:
Provides modern “Claude Code”-style terminal feel.

---

## Interactive Prompts

### Questionary

Used for:

* user input prompts
* selection menus
* interactive terminal questions

Reason:
Makes terminal interaction user-friendly.

---

## Templating Engine

### Jinja2

Used for:

* dynamic LaTeX templates
* injecting user data
* conditional rendering

Reason:
Avoids messy string concatenation.

---

## Markdown Conversion

### Pandoc

Used for:

* converting markdown → LaTeX

Reason:
Reliable and battle-tested.

We will later add our own customization layer on top of Pandoc.

---

# 7. Initial Workflow (MVP)

## User Flow

```text
latex-ai (vtu-cli)
   ↓
User Input (Interactive menu / prompt)
   ↓
CLI Core (Click / Typer) — captures command and flags
   ↓
LLM Engine (DeepSeek) — optional AI processing for rewriting/enhancement
   ↓
Pandoc — Markdown → LaTeX conversion
   ↓
VTU Template (Jinja2) — apply VTU-specific formatting and pages
   ↓
File System (`fs_manager.py`) — write project files and assets
   ↓
Compiler (`compiler.py` + `latexmk`) — compile to PDF (returns logs on errors)
```

---

# 8. Example User Interaction

```bash
vtu-cli
```

Then:

```text
1. Generate VTU Report
2. Exit

Select Option:
>
```

Then:

```text
Enter Report Title:
>

Enter Student Name:
>

Enter USN:
>

Enter Markdown File Path:
>
```

---

# 9. VTU Formatting Rules

The template system will enforce:

* A4 paper
* Left margin: 1.25 inch
* Right margin: 1 inch
* Top/Bottom: 0.75 inch
* Justified text

## Typography

### Chapter Titles

* Size 18
* Bold
* ALL CAPS

### Headings

* Size 16
* Bold

### Sub-headings

* Size 14
* Bold

### Body

* Size 12
* Regular

---

# 10. Template System

The VTU template will include:

* title page
* certificate page
* college logo
* department details
* signatures/stamps
* report structure

These are reusable LaTeX templates.

---

# 11. Why Markdown?

Markdown was selected because:

* lightweight
* readable
* Git-friendly
* easier to parse
* easier than PDFs
* structured enough for automation

The user writes:

* headings
* paragraphs
* tables
* equations
* images

in markdown.

The tool converts it into LaTeX.

---

# 12. Offline Mode vs AI Mode

## Mode 1 — Offline Mode

No API required.

Behavior:

* markdown copied mostly as-is
* formatting applied
* VTU template generated

Purpose:

* fully offline usage
* low-resource users
* deterministic generation

---

## Mode 2 — AI Enhanced Mode

Requires API key.

Behavior:

* rewrites into formal academic language
* improves grammar
* improves structure
* generates cleaner report sections

Purpose:

* enhanced academic writing quality

---

# 13. Important Design Decisions

## AI Is Optional

The tool must work even without AI.

Reason:

* accessibility
* easier debugging
* offline support

---

## Never Modify Original Markdown

The tool only reads markdown and generates new output.

Reason:

* user trust
* safer workflows

---

## Generate Project Structure

Not just one `.tex` file.

Example:

```text
project/
 ├── main.tex
 ├── chapters/
 ├── assets/
 ├── references.bib
```

Reason:
Real LaTeX projects are modular.

---

## Pandoc First, Custom Layer Later

We will not reinvent markdown parsing initially.

Architecture:

```text
Markdown
   ↓
Pandoc
   ↓
Custom VTU Styling Layer
   ↓
Final LaTeX
```

Reason:
Saves development time and reduces bugs.

---

# 14. Recommended Folder Structure

```text
ai-latex-cli/
│
├── main.py
├── requirements.txt
│
├── templates/
│   └── vtu/
│
├── assets/
│
├── generators/
│
├── parsers/
│
├── ai/
│
├── output/
│
└── utils/
```

---

# 15. Development Phases

# Phase 1 — Core CLI

Goal:
Basic interactive terminal app.

Features:

* menu
* metadata collection
* file path input

No AI.

---

# Phase 2 — VTU Template Engine

Goal:
Generate proper VTU `.tex` project.

Features:

* title pages
* formatting
* margins
* logos

No AI yet.

---

# Phase 3 — Markdown Processing

Goal:
Convert markdown → structured LaTeX.

Features:

* headings
* sections
* tables
* equations

---

# Phase 4 — AI Enhancement

Goal:
Improve writing quality.

Features:

* academic rewriting
* grammar correction
* abstract generation
* section enhancement

---

# Phase 5 — Advanced Features

Possible future additions:

* bibliography generation
* citation support
* image management
* equation correction
* LaTeX error fixing
* multi-template system
* IEEE templates
* resume generation
* PDF compilation
* local LLM support
* collaborative workflows

---

# 16. Long-Term Vision

The long-term goal is not just:

> “generate reports”

The larger vision is:

> Build an AI-native academic document engineering system.

Where users describe intent,
and the system handles:

* formatting
* structure
* technical document generation
* institution-specific compliance

through a terminal-first workflow.

---

# 17. Current MVP Goal

The immediate target is ONLY:

```text
CLI
 ↓
Ask Metadata
 ↓
Read Markdown
 ↓
Generate VTU .tex Project
```

No unnecessary complexity.

Focus:

* reliability
* clean architecture
* working pipeline
* deterministic generation

This is the foundation of the entire project.
