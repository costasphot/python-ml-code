# ml_04_explore_sklearn_datasets.py
#
# Datasets used:
#  1. Breast Cancer Wisconsin (Diagnostic)
#  2. Wine
#
# On Windows, run with:
#  .venv\Sources\activate
#  python .\ml_04_explore_sklearn_datasets.py

from __future__ import annotations

from typing import Any, cast

from sklearn.datasets import load_breast_cancer as LoadBreastCancer, load_wine as LoadWine
from sklearn.utils import Bunch
import numpy as np


def _PrintBunchInfo(dataset: Bunch) -> None:
  # scikit-learn datasets return a dict-like type called 'Bunch'.
  print("\n\tBunch Info:")
  print(f"- Keys: {list(dataset)}")
  print(f"- data shape: {dataset["data"].shape}")
  print(f"- target shape: {dataset["target"].shape}")
  print(f"- feature_names shape: {len(dataset["feature_names"])}")
  print(f"- target_names: {dataset["target_names"]}")


def ExploreBreastCancer() -> None:
  dataset: Bunch = cast(Bunch, LoadBreastCancer(return_X_y = False))

  print("\n= = = = = 1. Breast Cancer Wisconsin (Diagnostic) = = = = =")
  _PrintBunchInfo(dataset)

  label_names   = dataset["target_names"]   # E.g. ['malignant', 'benign']
  labels        = dataset["target"]         # Can be 0 or 1 for each sample.
  feature_names = dataset["feature_names"]  # 30-char names.
  features      = dataset["data"]           # Matrix of size 569x30.

  print("\n\tLabels:")
  print(f"- label_names: {label_names}")
  print(f"- labels[0:10]: {labels[:10]}")
  print(f"- labels.shape: {labels.shape}")

  # Class distribution

  print("\n\tClass distribution:")
  class_counts = np.bincount(labels)
  for class_index, class_name in enumerate(label_names):
    print(f"{class_name:10s}: {class_counts[class_index]}")

  print("\n\tFeatures:")
  print(f"- feature_names[0:5]: {feature_names[:5]}")
  print(f"- features.shape: {features.shape}")
  print(f"- first sample features[0]: {features[0]}")


def ExploreWine() -> None:
  dataset: Bunch = cast(Bunch, LoadWine(return_X_y = False))

  print("\n= = = = = 2. Wine = = = = =")
  _PrintBunchInfo(dataset)

  label_names   = dataset["target_names"]
  labels        = dataset["target"]
  feature_names = dataset["feature_names"]
  features      = dataset["data"]

  print("\n\tLabels:")
  print(f"- label_names: {label_names}")
  print(f"- labels.shape: {labels.shape}")
  print(f"- features.shape: {features.shape}")
  print(f"- example feature [sample 9, feature 2]: {features[9][2]}")
  print(f"- feature_names[2]: {feature_names[2]}")


def main() -> None:
  ExploreBreastCancer()
  ExploreWine()
  print()


if __name__ == "__main__":
  main()
