# 🤖 AI Code Review Agent

A smart, pluggable, and local-friendly code review tool powered by LLMs (OpenAI, Anthropic, or Ollama). It analyzes Python scripts, detects bugs, reviews style, suggests improvements, and summarizes feedback in Markdown.

---

## 🚀 Features

- Accepts Python files or code snippets
- Reviews for:
  - ❌ Bugs
  - ✨ Style issues
  - 🧪 Missing or weak tests
  - 🧠 Code clarity & suggestions
- Dual mode: Use OpenAI, Anthropic, or local Ollama models
- Prompt profiles (strict, mentor, test-focus)
- Output as clean Markdown in `reviews/review_output.md`

---

## 🧱 Project Structure

```
ai-project/
├── agent/
│   ├── analyzer.py          # Prompt builder + code analysis
│   └── llm_interface.py     # Provider logic (OpenAI, Ollama, Anthropic)
├── examples/                # Sample scripts to test
├── prompts/templates.yaml   # Prompt profiles
├── reviews/review_output.md# Review output
├── cli.py                   # Command-line runner
├── config.yaml              # API keys + model configs
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 1. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. 🔑 Add API Keys and Models

Edit `config.yaml`:

```yaml
openai:
  key: "YOUR_OPENAI_API_KEY"
  model: "gpt-4"

ollama:
  key: "YOUR_OLLAMA_API_KEY"
  model: "mistral"

anthropic:
  key: "YOUR_ANTHROPIC_API_KEY"
  model: "claude-3-opus-20240229"
```

> ✅ **Note**: Ollama requires you to have the model running locally. Start it with `ollama run mistral` before using.

---

## ⚙️ How to Run

### Basic Command

```bash
python cli.py --file examples/buggy_script.py --mode strict --provider openai
```

### Options

| Flag         | Description                                      |
| ------------ | ------------------------------------------------ |
| `--file`     | Path to the Python file to analyze               |
| `--mode`     | Prompt style: `strict`, `mentor` or `test_focus` |
| `--provider` | LLM backend: `openai`, `anthropic` or `ollama`   |

---

## 🧪 Example Review Output

```markdown
## 🚨 Bugs

- Variable `x` is used before assignment

## 💡 Suggestions

- Use `with open(...)` to handle files safely
- Add tests for edge cases in function `parse_input`

## ✍️ Style

- Line 24 exceeds 79 characters
```
