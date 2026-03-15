#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import shutil

import gdown
import kaggle
import kagglehub

from fraud_anomaly import config


RAW_DATA_DIR = Path(config.DATA_DIR) / "raw"


def download_ieee_cis_fraud() -> None:
    """Download the IEEE-CIS Fraud Detection competition files from Kaggle."""
    data_dir = RAW_DATA_DIR / "ieee_cis_fraud"
    data_dir.mkdir(parents=True, exist_ok=True)

    print(f"Downloading IEEE-CIS Fraud Detection dataset to {data_dir}")

    kaggle.api.competition_download_files(
        competition="ieee-fraud-detection",
        path=str(data_dir),
    )


def download_credit_card_fraud() -> None:
    """Download the Credit Card Fraud dataset from Kaggle Hub and save it locally."""
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_file = RAW_DATA_DIR / "creditcard.csv"

    print("Downloading Credit Card Fraud dataset from Kaggle Hub")

    downloaded_path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
    source_file = Path(downloaded_path) / "creditcard.csv"

    print(f"Saving Credit Card Fraud dataset to {output_file}")
    shutil.copy2(source_file, output_file)


def download_elliptic() -> None:
    """Download the Elliptic++ dataset from Google Drive."""
    data_dir = RAW_DATA_DIR / "elliptic"
    data_dir.mkdir(parents=True, exist_ok=True)

    folder_url = "https://drive.google.com/drive/folders/1MRPXz79Lu_JGLlJ21MDfML44dKN9R08l"

    print(f"Downloading Elliptic++ dataset to {data_dir}")

    gdown.download_folder(
        url=folder_url,
        output=str(data_dir),
        quiet=False,
        use_cookies=False,
    )


def main() -> None:
    """Download all datasets."""
    download_ieee_cis_fraud()
    download_credit_card_fraud()
    download_elliptic()


if __name__ == "__main__":
    main()
