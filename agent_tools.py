import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = None

def load_csv(path: str) -> str:
    global df
    df = pd.read_csv(path)
    return f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns."

def get_summary(_: str = "") -> str:
    global df
    if df is None:
        return "Dataset not loaded."
    return df.describe(include='all').to_string()

def compute_correlation(_: str = "") -> str:
    global df
    if df is None:
        return "Dataset not loaded."
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    return numeric_df.corr().to_string()
    #return df.corr().to_string()

def plot_trend(args: str) -> str:
    global df
    if df is None:
        return "Dataset not loaded."
    try:
        x, y = args.strip().split(',')
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x=x.strip(), y=y.strip())
        plt.title(f"Trend of {y.strip()} over {x.strip()}")
        plot_path = "trend_plot.png"
        plt.savefig(plot_path)
        plt.close()
        return f"Plot saved at {plot_path}"
    except Exception as e:
        return f"Error in plotting: {str(e)}"
