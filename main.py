import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from crewai import Agent, Task, Crew, Process, LLM
import os

# ✅ LLM Configuration (Ollama + DeepSeek-R1)
llm = LLM(
    model="ollama/deepseek-r1:7b",
    provider="ollama",
    config={
        "base_url": "http://localhost:11434",
        "model": "deepseek-r1:7b"
    },
    temperature=0.7,
    streaming=True
)

# 👤 Agent: Researcher
researcher = Agent(
    role="AI Researcher",
    goal="Generate future AI news headlines",
    backstory="A highly skilled researcher with access to past AI reports.",
    tools=[],
    llm=llm,
    verbose=True
)

# 👤 Agent: Writer
writer = Agent(
    role="Tech Blogger",
    goal="Write engaging blog content based on research",
    backstory="A talented writer who turns raw insights into engaging content.",
    tools=[],
    llm=llm,
    verbose=True
)

# 📋 Task 1: Generate AI headlines
research_task = Task(
    description="Generate 5 fictional but realistic AI news headlines with one-line summaries.",
    expected_output="A markdown bullet list of 5 AI news headlines with summaries.",
    agent=researcher
)

# 📋 Task 2: Write the blog post
write_task = Task(
    description="Use the research to write a markdown blog post summarizing the current state of AI in a creative and informative tone.",
    expected_output="A 3-paragraph markdown blog post.",
    agent=writer,
    output_file="blog-posts/ai_blog.md"
)

# 🧠 Crew Setup
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    manager_llm=llm,
    verbose=True
)

# 🚀 Run the CrewAI mission
if __name__ == "__main__":
    os.makedirs("blog-posts", exist_ok=True)
    result = crew.kickoff()
    print("\n✅ Mission Complete! Check your blog at: blog-posts/ai_blog.md\n")
    print(result)
