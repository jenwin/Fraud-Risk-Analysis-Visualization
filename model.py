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

# Calculate confusion matrix components
# True Positives (TP): Actually fraud and flagged
true_positives = df[(df['Is Fraudulent'] == 1) & (df['Was Flagged Fraudulent'] == 1)].shape[0]
# False Positives (FP): Not fraud but flagged
false_positives = df[(df['Is Fraudulent'] == 0) & (df['Was Flagged Fraudulent'] == 1)].shape[0]
# False Negatives (FN): Actually fraud but NOT flagged
false_negatives = df[(df['Is Fraudulent'] == 1) & (df['Was Flagged Fraudulent'] == 0)].shape[0]
# True Negatives (TN): Not fraud and NOT flagged
true_negatives = df[(df['Is Fraudulent'] == 0) & (df['Was Flagged Fraudulent'] == 0)].shape[0]