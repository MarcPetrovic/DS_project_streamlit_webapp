from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

class CyclicalEncoder(BaseEstimator, TransformerMixin):
    """
    Transformiert zyklische numerische Spalten (z.B. Monat, Wochentag) in Sin/Cos Features.
    """
    def __init__(self, variables, max_values=None, drop_original=True):
        self.variables = variables
        self.max_values = max_values
        self.drop_original = drop_original
    
    def fit(self, X, y=None):
        if self.max_values is None:
            self.max_values_ = {var: X[var].max() for var in self.variables}
        else:
            self.max_values_ = self.max_values
        return self
    
    def transform(self, X):
        X = X.copy()
        for var in self.variables:
            max_val = self.max_values_[var]
            X[f"{var}_sin"] = np.sin(2 * np.pi * X[var] / max_val)
            X[f"{var}_cos"] = np.cos(2 * np.pi * X[var] / max_val)
            if self.drop_original:
                X.drop(columns=var, inplace=True)
        return X
    
    def get_feature_names_out(self, input_features=None):
        feature_names = []
        for var in self.variables:
            feature_names.extend([f"{var}_sin", f"{var}_cos"])
        return feature_names
