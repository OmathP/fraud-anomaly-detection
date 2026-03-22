#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from fraud_anomaly import config

from sklearn.model_selection import train_test_split
import pandas as pd

RAW_DATA_DIR = Path(config.DATA_DIR) / "raw"
CREDITCARD_SPLIT_DIR = Path(config.DATA_DIR) / "interim/creditcard"
CREDITCARD_DIR = Path(RAW_DATA_DIR) / "creditcard.csv"



def main() -> None:
    """
    """

    data = pd.read_csv(CREDITCARD_DIR)

    X = data.drop(columns=['Class'])
    y = data['Class']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)


    CREDITCARD_SPLIT_DIR.mkdir(parents=True, exist_ok=True)

    X_train.to_csv(Path(CREDITCARD_SPLIT_DIR) / 'X_train.csv', index=False)
    X_test.to_csv(Path(CREDITCARD_SPLIT_DIR) / 'X_test.csv', index=False)
    y_train.to_csv(Path(CREDITCARD_SPLIT_DIR) / 'y_train.csv', index=False)
    y_test.to_csv(Path(CREDITCARD_SPLIT_DIR) / 'y_test.csv', index=False)

if __name__ == "__main__":
    main()