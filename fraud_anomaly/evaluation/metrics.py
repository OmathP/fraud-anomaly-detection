#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.metrics import roc_auc_score
from sklearn.metrics import average_precision_score
import numpy as np


def evaluate(y_true, y_scores)->None:
    """
    """

    roc = roc_auc_score(y_true, y_scores)
    print(f"ROC-AUC: {roc}")

    pr_auc = average_precision_score(y_true, y_scores)
    print(f"PR-AUC: {pr_auc}")


    k = int(0.01 * len(y_scores))  # top 1%
    top_k_idx = np.argsort(y_scores)[-k:]

    recall_top_k = y_true.iloc[top_k_idx].sum() / y_true.sum()
    print(f"Recall in top 1%: {recall_top_k}")



def main() -> None:
    """
    """

    evaluate()





if __name__ == "__main__":
    main()