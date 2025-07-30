import pandas as pd

# Load data from csv file
dataset_url = "https://raw.githubusercontent.com/jenwin/Financial_Data/refs/heads/main/financial_data.csv"

# Load data
df = pd.read_csv(dataset_url)

# Clean column names
df.columns = df.columns.str.strip()
df['Flagged'] = df['Flagged'].astype(str).str.strip()

# Convert to binary: "Yes" to 1, "No" to 0
df['FlaggedBinary'] = (df['Flagged'] == 'Yes').astype(int)

# Count fraud transactions by type
transfer_fraud_count = df[(df['Transaction Type'] == 'TRANSFER') & (df['Is Fraudulent'] == 1)].shape[0]
cash_out_fraud_count = df[(df['Transaction Type'] == 'CASH OUT') & (df['Is Fraudulent'] == 1)].shape[0]

# Total transactions
total_transactions = len(df)

# Count of transactions flagged as fraudulent
flagged_transactions = df['FlaggedBinary'].sum()

# Calculate confusion matrix components
# True Positives (TP): Actually fraud and flagged
true_positives = df[(df['Is Fraudulent'] == 1) & (df['FlaggedBinary'] == 1)].shape[0]   # Fraud and flagged
false_positives = df[(df['Is Fraudulent'] == 0) & (df['FlaggedBinary'] == 1)].shape[0]  # Not fraud but flagged
false_negatives = df[(df['Is Fraudulent'] == 1) & (df['FlaggedBinary'] == 0)].shape[0]  # Fraud but not flagged
true_negatives = df[(df['Is Fraudulent'] == 0) & (df['FlaggedBinary'] == 0)].shape[0]   # Not fraud and not flagged

# Calculate fraud rates
transfer_fraud_total = transfer_fraud_count / total_transactions
cash_out_fraud_total = cash_out_fraud_count / total_transactions
sum_transfer_cash_out_fraud = transfer_fraud_total + cash_out_fraud_total

# flagging/detection rate
flagging_rate = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0

# Percentages for reporting
transfer_fraud_total_percent = transfer_fraud_total * 100 
cash_out_fraud_total_percent = cash_out_fraud_total * 100
sum_transfer_cash_out_fraud_percent = sum_transfer_cash_out_fraud * 100
flagging_rate_percent = round(flagging_rate * 100)

# Print the summary
print("Fraud Flagging Performance Summary:")
print(f"Total Transactions: {total_transactions}")
print(f"Correctly Flagged Frauds: {true_positives}")
print(f"Transfer Fraud Rate: {transfer_fraud_total_percent:.2f}%")
print(f"Cash out Fraud Rate: {cash_out_fraud_total_percent:.2f}%")
print(f"Total Fraud Rate: {sum_transfer_cash_out_fraud_percent:.2f}%")
print(f"Flagging (Detection) Rate: {flagging_rate_percent:.0f}%")

# Print confusion matrix components
print("\nConfusion Matrix Components:")
print(f"True Positives (TP): {true_positives}")
print(f"False Positives (FP): {false_positives}")
print(f"False Negatives (FN): {false_negatives}")
print(f"True Negatives (TN): {true_negatives}")