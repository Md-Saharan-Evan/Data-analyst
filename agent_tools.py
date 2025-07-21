import base64
from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = None

def load_csv(path: str) -> str:
    """Loads a CSV dataset from a file path."""
    global df
    try:
        df = pd.read_csv(path)
        return f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns."
    except FileNotFoundError:
        return f"Error: File '{path}' not found."
    except Exception as e:
        return f"Error loading dataset: {str(e)}"

def get_summary(_: str = "") -> str:
    """Returns a summary of the loaded dataset."""
    global df
    if df is None:
        return "Dataset not loaded."
    try:
        return df.describe(include='all').to_string()
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def compute_correlation(_: str = "") -> str:
    """Returns correlation matrix for numerical features."""
    global df
    if df is None:
        return "Dataset not loaded."
    try:
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        if numeric_df.empty:
            return "No numerical columns available for correlation."
        corr_matrix = numeric_df.corr()
        return corr_matrix.to_string()
    except Exception as e:
        return f"Error computing correlation: {str(e)}"

def plot_trend(args: str) -> str:
    """Plots a trend between two columns, format: column_x,column_y."""
    global df
    if df is None:
        return "Dataset not loaded."
    try:
        x, y = args.strip().split(',')
        x, y = x.strip(), y.strip()
        if x not in df.columns or y not in df.columns:
            return f"Error: One or both columns '{x}', '{y}' not found in dataset."
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x=x, y=y)
        plt.title(f"Trend of {y} over {x}")
        plt.xlabel(x)
        plt.ylabel(y)
        # Instead of saving to disk, encode plot as base64 for Pyodide compatibility
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
        return f"Trend plot generated (base64-encoded image data):\n{img_str}"
    except Exception as e:
        return f"Error in plotting: {str(e)}"