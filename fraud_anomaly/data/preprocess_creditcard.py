#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pathlib import Path
from fraud_anomaly import config


from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib

CREDITCARD_SPLIT_DIR = Path(config.DATA_DIR) / "interim/creditcard"
CREDITCARD_PROCESSED_DIR = Path(config.DATA_DIR) / "processed/creditcard"



def main() -> None:
    """
    """


    X_train = pd.read_csv(Path(CREDITCARD_SPLIT_DIR) / 'X_train.csv')
    y_train = pd.read_csv(Path(CREDITCARD_SPLIT_DIR) / 'y_train.csv')
    X_test = pd.read_csv(Path(CREDITCARD_SPLIT_DIR) / 'X_test.csv')
    y_test = pd.read_csv(Path(CREDITCARD_SPLIT_DIR) / 'y_test.csv')


    X_train = X_train.drop(columns=["Time"])
    X_test = X_test.drop(columns=["Time"])

    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(
        scaler.fit_transform(X_train),
        columns=X_train.columns,
        index=X_train.index,
    )
    X_test_scaled = pd.DataFrame(
        scaler.transform(X_test),
        columns=X_test.columns,
        index=X_test.index,

        
    )

    CREDITCARD_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    X_train.to_csv(Path(CREDITCARD_PROCESSED_DIR) / 'X_train.csv', index=False)
    X_test.to_csv(Path(CREDITCARD_PROCESSED_DIR) / 'X_test.csv', index=False)
    y_train.to_csv(Path(CREDITCARD_PROCESSED_DIR) / 'y_train.csv', index=False)
    y_test.to_csv(Path(CREDITCARD_PROCESSED_DIR) / 'y_test.csv', index=False)
    joblib.dump(scaler, CREDITCARD_PROCESSED_DIR / "scaler.joblib")


if __name__ == "__main__":
    main()
