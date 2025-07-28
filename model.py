import pandas as pd

# Load data from csv file
dataset_url = "https://raw.githubusercontent.com/jenwin/Financial_Data/refs/heads/main/financial_data.csv"

# Load data
df = pd.read_csv(dataset_url)

# Clean column names
df.columns = df.columns.str.strip()

# Create a new column to simulate fraud flagging based on Amount
df['SimulatedFlagged'] = (df['Amount'] > 200000).astype(int)

# Total transactions
total_transactions = len(df)

# Count of actual fraudulent transactions
actual_frauds = df['Is Fraudulent'].sum()
# Count of transactions flagged as fraudulent
flagged_transactions = df['SimulatedFlagged'].sum()

# Calculate confusion matrix components
# True Positives (TP): Actually fraud and flagged
true_positives = df[(df['Is Fraudulent'] == 1) & (df['SimulatedFlagged'] == 1)].shape[0]
# False Positives (FP): Not fraud but flagged
false_positives = df[(df['Is Fraudulent'] == 0) & (df['SimulatedFlagged'] == 1)].shape[0]
# False Negatives (FN): Actually fraud but NOT flagged
false_negatives = df[(df['Is Fraudulent'] == 1) & (df['SimulatedFlagged'] == 0)].shape[0]
# True Negatives (TN): Not fraud and NOT flagged
true_negatives = df[(df['Is Fraudulent'] == 0) & (df['SimulatedFlagged'] == 0)].shape[0]

# Calculate rates
flagging_rate = (flagged_transactions / total_transactions) * 100 if total_transactions else 0
detection_rate = (true_positives / actual_frauds) * 100 if actual_frauds else 0

# Print the summary
print("Fraud Flagging Performance Summary:")
print(f"Total Transactions: {total_transactions}")
print(f"Actual Fraudulent Transactions: {actual_frauds}")
print(f"Flagged Transactions (Simulated): {flagged_transactions}")
print(f"Correctly Flagged Frauds (True Positives): {true_positives}")
print(f"Overall Flagging Rate (% of all transactions): {flagging_rate:.2f}")
print(f"Fraud Detection Rate (% of actual frauds caught): {detection_rate:.2f}")

# Print confusion matrix components
print("\nConfusion Matrix Components:")
print(f"True Positives (TP): {true_positives}")
print(f"False Positives (FP): {false_positives}")
print(f"False Negatives (FN): {false_negatives}")
print(f"True Negatives (TN): {true_negatives}")