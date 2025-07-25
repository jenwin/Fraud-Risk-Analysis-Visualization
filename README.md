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