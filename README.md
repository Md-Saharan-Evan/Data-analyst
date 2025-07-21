🌟 LangChain Data Analyst Agent 🌟
🚀 A next-level data analysis tool powered by LangChain! Unleash the power to load, summarize, and visualize datasets with a slick conversational interface. Built with Pandas, Matplotlib, and Seaborn, it’s your go-to for crunching numbers and spotting trends. 🎉

✨ Features

📥 Load CSV: Import datasets from CSV files with ease.
📊 Dataset Summary: Get juicy statistical summaries in a snap.
🔍 Correlation Analysis: Uncover relationships with correlation matrices for numerical columns.
📈 Trend Visualization: Plot stunning trends between columns using line plots.
💬 Conversational Interface: Chat with the agent using natural language queries—yes, it’s that cool! 😎

🛠️ Prerequisites

🐍 Python 3.8+: Make sure your Python game is up to date.
🔑 API Key: Grab a key for Google Generative AI or OpenAI (depending on your LLM vibe).
🌱 .env File: Set up your API keys and LLM config like a pro.

🚀 Installation

Clone the Repo:
git clone https://github.com/Md-Saharan-Evan/Data-analyst.git
cd Data-analyst

Set Up a Virtual Env (optional but recommended):
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

Install Dependencies:Rock the required packages with:
pip install -r requirements.txt

Check out the full list in requirements.txt—it’s packed with goodies like langchain, pandas, and matplotlib!

Configure .env:Create a .env file and add your secrets:
echo "GOOGLE_API_KEY=your_google_api_key" > .env
echo "OPENAI_API_KEY=your_openai_api_key" >> .env
echo "LLM_PROVIDER=google" >> .env
echo "LLM_MODEL=gemini-2.0-flash" >> .env

Swap in your real API keys—keep it secure! 🔒

🎮 Usage

Fire Up the Agent:
python main.py

Chat with the Agent:

Type your commands at the "You: " prompt. Try these:
Load CSV data.csv 🚗
Get Summary 📋
Compute Correlation 🔗
Plot Trend column1,column2 📉

Exit with exit or quit when you’re done. 👋

Example Flow:
You: Load CSV data.csv
Agent: Loaded dataset with 100 rows and 5 columns. 🎉
You: Get Summary
Agent: [Stats magic happens here]
You: Plot Trend age,salary
Agent: Trend plot generated! 📊

🌈 Cool Notes

📂 File Paths: Use valid CSV paths. In Pyodide, try URLs or virtual filesystems for extra flair.
🎨 Plot Output: Plots come as base64 strings—perfect for browser vibes. Add a frontend to show them off!
🤖 LLM Options: Default is Gemini 2.0 Flash. Switch to OpenAI models by tweaking your .env file.
🌐 Pyodide Mode: Running in the browser? We’ve got you covered with base64-encoded plots.

📩 Contact
Got questions? Hit me up at [mdsaharanevan20001@gmail.com] or open an issue on GitHub. Let’s chat! 💬
