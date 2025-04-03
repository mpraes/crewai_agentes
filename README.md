# 🧠 Local AI Blog Generator (CrewAI + Ollama + DeepSeek)

This project is a fully local AI-powered blog post generator, using [CrewAI](https://docs.crewai.com/) to simulate a multi-agent system for researching and writing AI news content.

No cloud, no keys, no limits — powered entirely by [Ollama](https://ollama.com) + `deepseek-r1:7b` running locally on your machine.

---

## 📌 What It Does

- ✅ Uses an **AI Researcher agent** to generate futuristic AI headlines
- ✅ Uses a **Tech Writer agent** to compose a blog post from those headlines
- ✅ Runs 100% locally (no OpenAI, no internet required)
- ✅ Outputs a full blog post in Markdown format

---

## ⚙️ Technologies Used

| Tool        | Purpose                          |
|-------------|----------------------------------|
| CrewAI      | Multi-agent task orchestration   |
| Ollama      | Local LLM backend                |
| DeepSeek-R1 | Language model (7B, fast & smart)|
| LangChain   | LLM wrapper interface            |
| Python 3.10+| Core runtime                     |
| uv          | Blazing-fast dependency manager  |

---

## 🚀 How to Run

1. **Install [Ollama](https://ollama.com) and pull the model:**

```bash
ollama pull deepseek-r1:7b

2. **Clone the project and set it up:**

```bash
uv venv
source .venv/Scripts/activate    # or `.venv/bin/activate` on macOS/Linux
uv pip install --editable .

3. **Run the app**
python main.py

4. Check the output:

Blog post will be saved at:

```bash
blog-posts/ai_blog.md

👨‍👩‍👧 Agent Architecture
Agent	Role
AI Researcher	Generates 5 futuristic headlines
Tech Blogger	Writes a blog post from research
They work together using a sequential CrewAI flow to simulate realistic writing workflows.

📁 Output Sample
blog-posts/
├── ai_blog.md

🧠 Future Ideas
 Add memory system to recall past posts
 Add CLI flags for theme/topic
 Use DirectoryReadTool to train from local content
 Add auto-publishing (e.g. to Ghost/WordPress)
 Add fact-checking agent

 🧡 Credits
Built with CrewAI
Model: deepseek-r1:7b via Ollama


---

Let me know if you'd like:
- A version with badges (GitHub-style)
- A Portuguese 🇧🇷 version
- A README for your supplier system team project next 🛠️
