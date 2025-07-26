# Fraud Risk Analysis & Visualization

## Business Problem
How can a financial institution accurately detect fraudulent transactions in real-time to minimize financial losses and protect customers?

Understanding the factors behind fraudulent transactions allows financial institutions to:

- Minimize financial losses due to fraud
- Protect customers and build trust
- Design better fraud prevention and monitoring systems

## The Dataset

| Attribute     | Description                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------|
| `step`             | Time step of the transaction. Each step represents an hour.                                     |
| `type`             | Type of transaction: PAYMENT, CASH_OUT, TRANSFER, DEBIT                                  |
| `amount`           | Amount of money involved in the transaction                                                    |
| `nameOrig`         | Customer ID of the originator (sender)                                                         |
| `oldbalanceOrg`    | Account balance of the originator before the transaction                                       |
| `newbalanceOrig`   | Account balance of the originator after the transaction                                        |
| `nameDest`         | Customer ID of the destination (receiver)                                                     |
| `oldbalanceDest`   | Account balance of the destination before the transaction                                      |
| `newbalanceDest`   | Account balance of the destination after the transaction                                       |
| `isFraud`          | Indicates if the transaction is fraudulent (1) or not fraudulent (0)                               |
| `isFlaggedFraud`   | Indicates if the transaction was flagged as fraudulent (1) or not fraudulent (0) by the system                   |

## Approach

### Tools & Technologies Used
- **Excel** – For data cleaning and validation.

### Data Cleaning and Validation

1. **Rename Columns**

| Original Column      | New Column                      |
|----------------------|---------------------------------|
| `step`               | Time Step (Hour)                |
| `type`               | Transaction Type                |
| `amount`             | Amount                          |
| `nameOrig`           | Origin Account                  |
| `oldbalanceOrg`      | Origin Balance Before           |
| `newbalanceOrig`     | Origin Balance After            |
| `nameDest`           | Destination Account             |
| `oldbalanceDest`     | Destination Balance Before      |
| `newbalanceDest`     | Destination Balance After       |
| `isFraud`            | Is Fraudulent                   |
| `isFlaggedFraud`     | Was Flagged Fraudulent          |

2. **Add Day Column**

| Column      | Conversion (Hour to Day) | Purpose                         |
|-------------|--------------------------|---------------------------------|
| `step`      | Time in hours (0, 1, 2)  | Shows data by hour              |
| `Day` (new) | Time in days (0, 1, 2)   | Groups data into full days      |

3. Checked for blanks: None found.

4. Checked that all values in the Transaction Type column are in uppercase.

5. Dropped columns: 
  - `Origin Account`
  - `Destination Account`
  
These columns only identify user accounts and don’t provide useful information for detecting fraud.

6. Checked for any negative and zero values in `Amount` column.

7. Add `Fraudulent Status` column: From `Is Fraudulent`, convert `0` to `No` and `1` to `Yes`.

| Is Fraudulent | Fraudulent Status|
|--------------|-------------------|
| 0            | No                |
| 1            | Yes               |

8. Add `Flagged Status` column: From `Was Flagged Fraudulent`, convert `0` to `No` and `1` to `Yes`.

| Was Flagged Fraudulent | Flagged Status|
|------------------------|---------------|
| 0                      | No            |
| 1                      | Yes           |

9. Verified columns contain numeric values:
  - `Time Stamp`
  - `Amount`
  - `Origin Balance Before`  
  - `Origin Balance After`  
  - `Destination Balance Before`  
  - `Destination Balance After`
  - `Is Fraudulent`
  - `Was Flagged Fraudulent`