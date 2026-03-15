# Financial Anomaly Detection

This repository contains experiments and utilities for studying **anomaly detection in financial datasets**, including fraud detection in credit card transactions, e-commerce payments, and blockchain activity.

The project focuses on building reproducible pipelines for:

- Financial fraud detection
- Anomaly detection algorithms
- Comparative evaluation of models
- Future extensions to **deep anomaly detection** and **federated learning**

---

## Datasets

The project currently supports the following datasets:

### Credit Card Fraud Detection
European credit card transactions dataset commonly used in fraud detection research.

Source:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Characteristics:

- 284,807 transactions
- 492 fraud cases
- Highly imbalanced dataset
- 28 anonymized PCA features

---

### IEEE-CIS Fraud Detection
Large-scale dataset of e-commerce transactions provided as a Kaggle competition.

Source:
https://www.kaggle.com/c/ieee-fraud-detection

Characteristics:

- ~590,000 transactions
- Hundreds of features
- Identity and device information
- Complex real-world fraud patterns

---

### Elliptic++ Bitcoin Dataset
Blockchain dataset used for anti-money laundering (AML) and illicit transaction detection.

Source:
https://github.com/git-disl/EllipticPlusPlus

Characteristics:

- Bitcoin transaction graph
- Wallet and transaction features
- Multiple graph representations
- Suitable for graph anomaly detection

---

## Installation

Clone the repository:

```bash
git clone <repo-url>
cd fraud-anomaly-detection
