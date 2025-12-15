# executor_agent.py
import os
from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- LLM Configuration ---
api_key = os.getenv("api_key")
base_url = "https://optollm.optomatica.com"

custom_llm = ChatOpenAI(
    model="openai/deepseek-r1-32b",
    api_key=api_key,
    base_url=base_url,
    temperature=0.5,
    max_tokens=2000
)

# --- Executor Agent Definition ---
executor = Agent(
    role='Social Media Executor for IEEE Zewail City',
    goal='Execute approved Facebook posts by simulating or performing real actions like posting or scheduling.',
    backstory=(
        "You are responsible for executing the final, approved social media posts. "
        "You can post directly, schedule them, or save them for approval. "
        "You ensure the post is properly formatted and record the action taken."
    ),
    verbose=True,
    allow_delegation=False,
    llm=custom_llm
)

# --- Simulated Posting Tool ---
def post_to_facebook_simulator(post_text: str):
    """
    Simulates posting to Facebook.
    In a real scenario, this would call Facebook's Graph API.
    """
    print("\n📡 Simulating Facebook Post...")
    print("------------------------------------------------")
    print(post_text)
    print("------------------------------------------------")
    print("✅ Post successfully 'published' to Facebook (simulation).")
    return "Post published successfully (simulation)."

# --- Executor Task Factory ---
def create_executor_task(reviewing_task):
    """
    Creates the execution task linked to the reviewing agent's output.
    """
    return Task(
        description="Take the final reviewed Facebook post and publish it using available tools or simulation.",
        expected_output="A confirmation message indicating the post was published or scheduled.",
        agent=executor,
        context=[reviewing_task]
    )
