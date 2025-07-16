import os

from dotenv import load_dotenv
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from agent_tools import compute_correlation, get_summary, load_csv, plot_trend

load_dotenv()

tools = [
    Tool(name="Load CSV", func=load_csv, description="Loads a CSV dataset from a file path."),
    Tool(name="Get Summary", func=get_summary, description="Returns a summary of the loaded dataset."),
    Tool(name="Compute Correlation", func=compute_correlation, description="Returns correlation between numerical features."),
    Tool(name="Plot Trend", func=plot_trend, description="Plot a trend between two columns, format: column_x,column_y")
]

#llm = ChatOpenAI(temperature=0, model="gpt-4")
#llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
# llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
# You can use gpt-3.5-turbo too

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
    response = agent.run(query)
    print(f"Agent: {response}")
