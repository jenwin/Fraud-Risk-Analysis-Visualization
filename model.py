import pandas as pd

# Load data from csv file
dataset_url = "https://raw.githubusercontent.com/jenwin/Financial_Data/refs/heads/main/financial_data.csv"

# Load data
df = pd.read_csv(dataset_url)