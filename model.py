import pandas as pd

# Load data from csv file
dataset_url = "https://raw.githubusercontent.com/jenwin/Financial_Data/refs/heads/main/financial_data.csv"

# Load data
df = pd.read_csv(dataset_url)

# Clean column names
df.columns = df.columns.str.strip()

# Total transactions
total_transactions = len(df)

# Count of actual fraudulent transactions
actual_frauds = df['Is Fraudulent'].sum()
# Count of transactions flagged as fraudulent
flagged_transactions = df['Was Flagged Fraudulent'].sum()