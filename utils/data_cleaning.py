from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

class RemoveDuplicates(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X.drop_duplicates()

class ColumnDrop(BaseEstimator, TransformerMixin):
    def __init__(self, columns_to_drop):
        self.columns_to_drop = columns_to_drop
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X.drop(columns=self.columns_to_drop)

def get_cleaning_pipeline(columns_to_drop):
    return Pipeline(steps=[
        ('remove_duplicates', RemoveDuplicates()),
        ('drop_column', ColumnDrop(columns_to_drop))
    ])
