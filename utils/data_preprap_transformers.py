from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class ReplaceUnknowns(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None): return self
    def transform(self, X): return X.replace({'unknown': np.nan})

class CategorizeDefault(BaseEstimator, TransformerMixin):
    def __init__(self, column_name): self.column_name = column_name
    def fit(self, X, y=None): return self
    def transform(self, X): 
        X[self.column_name + "_cat"] = X[self.column_name].replace(['unknown', 'yes'], ['unknown|yes', 'unknown|yes'])
        return X

class CustTrans(BaseEstimator, TransformerMixin):
    def __init__(self, column_name): self.column_name = column_name
    def fit(self, X, y=None): return self
    def transform(self, X): 
        X['target'] = X[self.column_name].replace(['no', 'yes'], [0, 1])
        return X

class ColumnDrop(BaseEstimator, TransformerMixin):
    def __init__(self, column_to_drop): self.column_to_drop = column_to_drop
    def fit(self, X, y=None): return self
    def transform(self, X): return X.drop(self.column_to_drop, axis=1)

class CustTransPdays(BaseEstimator, TransformerMixin):
    def __init__(self, column_name): self.column_name = column_name
    def fit(self, X, y=None): return self
    def transform(self, X): 
        X[self.column_name + "_cat"] = X[self.column_name].replace([999], [0])
        return X
