import pytest
import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from ml.model import train_model, inference, compute_model_metrics
from ml.data import process_data

# Load a small sampleset of test data stored in the test_data_census.csv
project_path = os.getcwd()
test_data_path = os.path.join(project_path, "data", "test_data_census.csv")
print(test_data_path)
data = pd.read_csv(test_data_path) 

categorical_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

X, y, _, _ = process_data(
    data,
    categorical_features=categorical_features,
    label="salary",
    training=True,
)


def test_one():
    """
    # Test that train_model returns a RandomForestClassifier instance.
    """
    model = train_model(X, y)
    
    assert isinstance(model, RandomForestClassifier)


def test_two():
    """
    # Test that inference returns predictions with the same length as input.
    """
    model = train_model(X, y)
    preds = inference(model, X)
    
    assert len(preds) == len(X)
    assert isinstance(preds, np.ndarray)


def test_three():
    """
    # Test that compute_model_metrics returns float values.
    """
    model = train_model(X, y)
    preds = inference(model, X)
    precision, recall, fbeta = compute_model_metrics(y, preds)
    
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)
