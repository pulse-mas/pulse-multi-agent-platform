import os
from dotenv import load_dotenv
from executor_agent import executor, create_executor_task, post_to_facebook_simulator

load_dotenv()

from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Set up the custom API configuration
api_key = os.getenv("api_key")
base_url = "https://optollm.optomatica.com"

# IMPORTANT: Set environment variables for LiteLLM (used by CrewAI internally)
os.environ["OPENAI_API_KEY"] = api_key
os.environ["OPENAI_API_BASE"] = base_url

# --- LLM Configuration ---
# Use LangChain's ChatOpenAI with custom base_url for the proxy
custom_llm = ChatOpenAI(
    model="openai/deepseek-r1-32b",
    api_key=api_key,
    base_url=base_url,
    temperature=0.5,
    max_tokens=2000
)

# --- Agent Definitions ---

# Agent 1: The Strategic Planner
planner = Agent(
    role='Social Media Planner for IEEE Zewail City',
    goal='Create a detailed content plan for a given topic. The plan must be engaging for engineering students and align with IEEE\'s professional standards.',
    backstory=(
        "You are an expert social media strategist specializing in technical student communities. "
        "You know how to grab the attention of busy engineering students at Zewail City. "
        "Your plans are clear, structured, and designed for maximum engagement on Facebook."
    ),
    verbose=True,
    allow_delegation=False,
    llm=custom_llm
)

# Agent 2: The Creative Content Writer
content_creator = Agent(
    role='Content Creator for IEEE Zewail City Facebook Page',
    goal='Write a compelling and informative Facebook post based on the content plan provided by the Planner.',
    backstory=(
        "You are a skilled copywriter for the IEEE Zewail City branch. You can turn any technical topic "
        "into an exciting and easy-to-read social media post. You are fluent in using emojis like 🚀, 💻, and 🎓 "
        "to make posts more engaging, and you always maintain a professional yet approachable tone."
    ),
    verbose=True,
    allow_delegation=False,
    llm=custom_llm
)

# Agent 3: The Critical Reviewer
reviewer = Agent(
    role='Quality Assurance Editor for IEEE Zewail City',
    goal='Review the generated Facebook post for accuracy, clarity, and adherence to IEEE ZC brand guidelines. Provide a final, polished version.',
    backstory=(
        "You have a keen eye for detail and are the guardian of the IEEE Zewail City brand voice. "
        "You check for grammatical errors, ensure the technical details are correct, and verify that the tone is "
        "perfectly balanced—professional, educational, and exciting for students. You add the final polish."
    ),
    verbose=True,
    allow_delegation=False,
    llm=custom_llm
)

# --- Task Definitions ---

# The user's initial brief for the crew
user_brief = (
    "We need a Facebook post to announce a new 3-day online workshop on 'Machine Learning with TensorFlow'. "
    "It's for beginners. The goal is to get students to sign up via a registration link. "
    "Mention that it will boost their practical skills for their graduation projects."
)

# Task 1: The Planning Task
planning_task = Task(
    description=f"Create a content plan for a Facebook post about a new workshop. Here is the brief: {user_brief}",
    expected_output=(
        "A detailed plan including:\n"
        "1. A catchy hook to start the post.\n"
        "2. 3-4 key value points for students.\n"
        "3. A section mentioning its relevance for graduation projects.\n"
        "4. A strong call-to-action (CTA).\n"
        "5. A list of relevant hashtags."
    ),
    agent=planner
)

# Task 2: The Content Creation Task
creation_task = Task(
    description="Generate a full Facebook post based on the provided content plan. Ensure the language is engaging and clear for university students.",
    expected_output="A complete, well-written Facebook post draft including text and suggested emojis.",
    agent=content_creator,
    context=[planning_task]
)

# Task 3: The Reviewing Task
reviewing_task = Task(
    description="Review the draft Facebook post. Check for errors, clarity, and brand voice alignment. Add relevant hashtags and provide the final, ready-to-publish version.",
    expected_output="The final, polished version of the Facebook post, free of errors and perfectly aligned with the IEEE ZC brand.",
    agent=reviewer,
    context=[creation_task]
)

# --- Assemble the Crew ---

ieeezc_crew = Crew(
    agents=[planner, content_creator, reviewer],
    tasks=[planning_task, creation_task, reviewing_task],
    process=Process.sequential,
    verbose=True
)

# --- Kick off the Process ---

if __name__ == "__main__":
    print("🚀 Crew is ready. Kicking off the content creation process...")
    result = ieeezc_crew.kickoff()
    
    print("\n\n✅ Process Complete! Here is the final result:")
    print("================================================")
    print(result)