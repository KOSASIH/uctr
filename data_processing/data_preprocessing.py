import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def preprocess_data(df, target_column, test_size=0.2, random_state=42):
    # Split data into features and target
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Scale/normalize features
    X_train = (X_train - X_train.min()) / (X_train.max() - X_train.min())
    X_test = (X_test - X_train.min()) / (X_train.max() - X_train.min())

    return X_train, X_test, y_train, y_test
