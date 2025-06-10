from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class ReplaceUnknowns(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.replace({'unknown': np.nan})

    def get_feature_names_out(self, input_features=None):
        return input_features


class CategorizeDefault(BaseEstimator, TransformerMixin):
    def __init__(self, column_name):
        self.column_name = column_name

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X[self.column_name + "_cat"] = X[self.column_name].replace(['unknown', 'yes'], ['unknown|yes', 'unknown|yes'])
        return X

    def get_feature_names_out(self, input_features=None):
        return input_features + [self.column_name + "_cat"]


class CustTrans(BaseEstimator, TransformerMixin):
    def __init__(self, column_name):
        self.column_name = column_name

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X['target'] = X[self.column_name].replace(['no', 'yes'], [0, 1])
        return X

    def get_feature_names_out(self, input_features=None):
        return input_features + ['target']


class ColumnDrop(BaseEstimator, TransformerMixin):
    def __init__(self, column_to_drop):
        self.column_to_drop = column_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop(self.column_to_drop, axis=1)

    def get_feature_names_out(self, input_features=None):
        if input_features is None:
            return None
        return [f for f in input_features if f != self.column_to_drop]


class CustTransPdays(BaseEstimator, TransformerMixin):
    def __init__(self, column_name):
        self.column_name = column_name

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X[self.column_name + "_cat"] = X[self.column_name].replace([999], [0])
        return X

    def get_feature_names_out(self, input_features=None):
        return input_features + [self.column_name + "_cat"]
