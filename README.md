# Fraud Risk Analysis & Visualization

## Business Problem
How can a financial institution accurately detect fraudulent transactions in real-time to minimize financial losses and protect customers?

Understanding the factors behind fraudulent transactions allows financial institutions to:

- Minimize financial losses due to fraud
- Protect customers and build trust
- Design better fraud prevention and monitoring systems

## The Dataset

| Attribute          | Description                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------|
| `step`             | Time step of the transaction. Each step represents an hour.                                     |
| `type`             | Type of transaction: PAYMENT, CASH_OUT, TRANSFER, DEBIT                                         |
| `amount`           | Amount of money involved in the transaction                                                     |
| `nameOrig`         | Customer ID of the originator (sender)                                                          |
| `oldbalanceOrg`    | Account balance of the originator before the transaction                                        |
| `newbalanceOrig`   | Account balance of the originator after the transaction                                         |
| `nameDest`         | Customer ID of the destination (receiver)                                                       |
| `oldbalanceDest`   | Account balance of the destination before the transaction                                       |
| `newbalanceDest`   | Account balance of the destination after the transaction                                        |
| `isFraud`          | Indicates if the transaction is fraudulent (1) or not fraudulent (0)                            |
| `isFlaggedFraud`   | Indicates if the transaction was flagged as fraudulent (1) or not fraudulent (0) by the system  |

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

| Column             | Conversion (Hour to Day) | Purpose                         |
|--------------------|--------------------------|---------------------------------|
| `Time Step (Hour)` | Time in hours (1,2,3,4)  | Shows data by hour              |
| `Day` (new)        | Time in days (1,2,3,4)   | Groups data into full days      |

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

10. **Removed Underscores in Transaction Types**

| Transaction Type Column    | New Transaction Type Column |
|----------------------------|-----------------------------|
| CASH_OUT                   | CASH OUT                    |
| CASH_IN                    | CASH IN                     |

## Results
- `TRANSFER` transaction type had the highest amount of fraud — $681,598,379.85 million.
- `CASH OUT` transaction type was the next runner-up — $680,383,860.58 million.
- `CASH IN`, `PAYMENT`, and `DEBT` had zero fraud.
- Fraud Rate per Transaction Type / Total Transaction Count:
  - `TRANSFER`: 0.0006
  - `CASH OUT`: 0.0005
  - Total Fraud Occurrence: 0.0011
- Fraud rate by count is less than 1%, but the fraud amounts are large. 
- Fraud spikes tend to happen unpredictably, indicating coordinated activity rather than random occurrences.
- Fraud is not evenly distributed over time. Certain hours have heavier fraud activity.

## Key Business Insights
- Fraud is highly targeted. Fraud only occurred in `TRANSFER` and `CASH OUT` transaction types.
- Since `TRANSFER` and `CASH OUT` contain fraudulent activity, they may occur together in fraudulent schemes.
- `TRANSFER` and `CASH OUT` are high risk concentration zones even though they make up a small percentage of transactions.
- Fraud transactions are not frequent. When they occur, they often involve very large amounts with high bursts of high-value transaction attempts.
 
- `CASH IN`, `PAYMENT`, and `DEBT` had zero fraudulent transactions, but this could translate to false positives. 

## Summary of Recommendations Based on Findings

**Fraud Surveillance Across Transaction Types**
- Focus fraud detection on `TRANSFER` and `CASH OUT` transaction types.
- Maintain fraud checks for `CASH IN`, `PAYMENT`, and `DEBT` transaction types.
  
**Enhance Real-Time Rules for Suspicious Behavior/Patterns**
  - Implement flags across scenarios: 
    - When funds are transferred and cashed out immediately.
    - Large values over $50,000 should be flagged.

**Observe Event Timing and Frequency**
  - Limit the number of transfers and cash outs per account within a day or hourly to detect unusual activity.
  - Lock accounts when time-based bursts are detected.
  - Utilize dashboards to monitor hourly fluctuations in transaction activities for both fraudulent and non-fraudulent transactions.
  - A sudden rise in fraud amounts can be an early sign of a new scam starting.

**Monitor Account Balance Changes**
  - Watch for patterns where funds are transferred from empty accounts.
  - Watch for accounts that are quickly depleted right after receiving money.

**Add Behavioral Modeling**
   - Train fraud detection models on `TRANSFER` and `CASH OUT` transaction types.
   - Add and enforce verification steps for `TRANSFER` and `CASH OUT` transaction types for new accounts or shortly after transfers.

## Author
Jennifer Nguyen