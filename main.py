import os

from dotenv import load_dotenv
from langchain.agents import AgentType, Tool, initialize_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from agent_tools import compute_correlation, get_summary, load_csv, plot_trend

load_dotenv()

# LLM configuration from environment variable
llm_model = os.getenv("LLM_MODEL", "gemini-2.0-flash")
llm_provider = os.getenv("LLM_PROVIDER", "google")

if llm_provider.lower() == "openai":
    llm = ChatOpenAI(
        temperature=0,
        model=llm_model,
        max_retries=2,
    )
else:
    llm = ChatGoogleGenerativeAI(
        model=llm_model,
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

tools = [
    Tool(
        name="Load CSV",
        func=load_csv,
        description="Loads a CSV dataset from a file path. Example: 'data.csv'",
    ),
    Tool(
        name="Get Summary",
        func=get_summary,
        description="Returns a statistical summary of the loaded dataset.",
    ),
    Tool(
        name="Compute Correlation",
        func=compute_correlation,
        description="Returns correlation matrix for numerical features.",
    ),
    Tool(
        name="Plot Trend",
        func=plot_trend,
        description="Plots a trend between two columns, format: 'column_x,column_y'. Both columns must exist in the dataset.",
    ),
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

print("🧠 Welcome to LangChain Data Analyst Agent")
print("Type 'exit' to quit")

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break
    try:
        response = agent.run(query)
        print(f"Agent: {response}")
    except Exception as e:
        print(f"Agent: Error processing query: {str(e)}")