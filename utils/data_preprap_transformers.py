from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class ReplaceUnknowns(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.replace({'unknown': np.nan})
        
    def get_feature_names_out(self):
        pass


class CategorizeDefault(BaseEstimator, TransformerMixin):
    # BaseEstimator contains the get_params and set_params methods.
    # TransformerMixin contains the method fit_transform.
    
    def __init__(self, column_name):
        self.column_name = column_name   # name of the column to be segmented
        
    def fit(self, X, y = None):  
        return self
    
    def transform(self, X): # Creation of the new column
        X[self.column_name + "_cat"]  = X[self.column_name].replace(['unknown', 'yes'], ['unknown|yes', 'unknown|yes'])
        
        return X 

    def get_feature_names_out(self):
        pass


class CustTrans(BaseEstimator, TransformerMixin):
    def __init__(self, column_name):
        self.column_name = column_name   # name of the column to be segmented
        
    def fit(self, X, y = None):  
        return self
    
    def transform(self, X): 
        X['target']= (     
            X[self.column_name]
            .replace({'no': 0, 'yes': 1})
            #.infer_objects(copy=False)  # optional
            .astype('int64')
        )
        #replace({'no': 0, 'yes': 1}).astype('int64')
        #replace(['no', 'yes'], [0, 1]).astype(int)
        
        return X 

    def get_feature_names_out(self):
        pass  


class ColumnDrop(BaseEstimator, TransformerMixin):
    
    def __init__(self, column_to_drop):
        self.column_to_drop = column_to_drop   # name of the column to remove
        
    def fit(self, X, y= None):  
        return self
    
    def transform(self, X): # Removes the column
        return X.drop(self.column_to_drop, axis = 1)

    def get_feature_names_out(self):
        pass


class CustTransPdays(BaseEstimator, TransformerMixin):
    def __init__(self, column_name):
        self.column_name = column_name   # name of the column to be segmented

    def fit(self, X, y = None):  
        return self
        
    def transform(self, X): 
        X[self.column_name + "_cat"]  = X[self.column_name].replace([999], [0])
            
        return X 
    
    def get_feature_names_out(self):
        pass
