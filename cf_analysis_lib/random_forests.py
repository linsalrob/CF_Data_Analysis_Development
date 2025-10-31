"""
Random Forests and Gradient Boosted Random Forests for classification and regression

This was cut from the GBRF jupyter notebook so we can use it elsewhere.

"""
import sys

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error


def get_appropriate_n_estimators(X, y):
    """
    Get the appropriate number of estimators for the model
    :param X: the features
    :param y: the target
    :return: the optimal number of estimators for this model
    """
    # Split dataset
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    # Initialize model with early stopping
    model = GradientBoostingClassifier(n_estimators=100, validation_fraction=0.2,
                                       n_iter_no_change=10, random_state=42)

    # Fit model (automatically stops when validation loss stops improving)
    model.fit(X_train, y_train)

    # Get the optimal number of trees
    return model.n_estimators_

def gb_classifier_model(X, y, n_estimators=1000, n_iter_no_change=20):
    """
    Build a classifier and return the model. 
    This is abstracted so we can access it directly
    """

    if set(y.cat.categories) == {0.0, 1.0}:
        mapped_counts = y.value_counts().rename({0.0: "no", 1.0: "yes"}).to_dict()
    else:
        mapped_counts = y.value_counts().to_dict()
    print(f"The data for the classifier is {mapped_counts} variables", file=sys.stderr)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = GradientBoostingClassifier(
        max_features="sqrt",
        validation_fraction=0.2,
        n_iter_no_change=n_iter_no_change,
        random_state=42,  # fixes randomness
        n_estimators=n_estimators,
        learning_rate=0.005,
        min_samples_leaf=5,
        max_depth=5
    )

    """
    n_estimators=200,       # number of trees
    learning_rate=0.1,      # shrinkage
    max_depth=3,            # tree depth
    max_features='sqrt',    # random subset of features at each split
    min_samples_leaf=5,     # minimum samples per leaf
    random_state=42         # for reproducibility
    n_iter_no_change=10,    # early stopping after 10 iterations without improvement
    validation_fraction=0.2 # use 20% of the training data as hold-out for early stopping
    """

    model.fit(X_train, y_train)

    if model.n_estimators_ < n_estimators:
        print(f"WARNING: Early stopping after only {model.n_estimators_} estimators were built to avoid overfitting", file=sys.stderr)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)

    # Feature importance
    feature_importances = pd.DataFrame(model.feature_importances_, index=X.columns, columns=['importance'])
    feature_importances_sorted = feature_importances.sort_values(by='importance', ascending=False)
    return model, mse, feature_importances_sorted


def gb_classifier(X, y, n_estimators=1000, n_iter_no_change=20):
    """
    Run a classifier for categorical data and return the mean squared error and the feature importances
    """

    model, mse, feature_importances_sorted = gb_classifier_model(X, y, n_estimators, n_iter_no_change)
    return mse, feature_importances_sorted


def gb_regressor_model(X, y, n_estimators=1000, n_iter_no_change=20):
    """
    Abstract out the regression so we can access the model
    """

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = GradientBoostingRegressor(
        max_features="sqrt",
        n_estimators=n_estimators,
        validation_fraction=0.2,
        random_state=42,  # fixes randomness
        n_iter_no_change=n_iter_no_change,
    )
    model.fit(X_train, y_train)

    if model.n_estimators_ < n_estimators:
        print(f"WARNING: Early stopping after only {model.n_estimators_} estimators were built to avoid overfitting",
              file=sys.stderr)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)

    # Feature importance
    feature_importances = pd.DataFrame(model.feature_importances_, index=X.columns, columns=['importance'])
    feature_importances_sorted = feature_importances.sort_values(by='importance', ascending=False)
    return model, mse, feature_importances_sorted


def gb_regressor(X, y, n_estimators=1000, n_iter_no_change=20):
    """
    Run a regressor for continuous data and return the mean squared error and the feature importances
    """
    model, mse, feature_importances_sorted = gb_regressor_model(X, y, n_estimators, n_iter_no_change)
    return mse, feature_importances_sorted


def random_forest_regression(X, y, n_estimators=1000):
    """
    Run a regressor for continuous data and return the mean squared error and the feature importances
    """

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train a RandomForestRegressor model
    model = RandomForestRegressor(random_state=42, n_estimators=n_estimators)  # You can adjust hyperparameters
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)

    # Feature importance
    feature_importances = pd.DataFrame(model.feature_importances_, index=X.columns, columns=['importance'])
    feature_importances_sorted = feature_importances.sort_values(by='importance', ascending=False)
    return mse, feature_importances_sorted


def random_forest_classifier(X, y, n_estimators=1000):
    """
    Run a classifier for categorical data and return the mean squared error and the feature importances
    """

    if set(y.cat.categories) == {0.0, 1.0}:
        mapped_counts = y.value_counts().rename({0.0: "no", 1.0: "yes"}).to_dict()
    else:
        mapped_counts = y.value_counts().to_dict()
    print(f"The data for the classifier is {mapped_counts} variables", file=sys.stderr)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train a RandomForestRegressor model
    model = RandomForestClassifier(random_state=42, n_estimators=n_estimators)  # You can adjust hyperparameters
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)

    # Feature importance
    feature_importances = pd.DataFrame(model.feature_importances_, index=X.columns, columns=['importance'])
    feature_importances_sorted = feature_importances.sort_values(by='importance', ascending=False)
    return mse, feature_importances_sorted

