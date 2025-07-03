from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class MonthTrans(BaseEstimator, TransformerMixin):
  def __init__(self, column_name):
    self.column_name = column_name   # name of the column to be segmented

  def fit(self, X, y = None):
    return self

  def transform(self, X): 
    X[self.column_name + "_numeric"] = X[self.column_name].replace(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
                                                                           , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    return X

  def get_feature_names_out(self):
    pass  

class WeekdayTrans(BaseEstimator, TransformerMixin):
  def __init__(self, column_name):
    self.column_name = column_name

  def fit(self, X, y = None):
    return self

  def transform(self, X):
    X[self.column_name + "_numeric"] = X[self.column_name].replace(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
                                                                           , [1, 2, 3, 4, 5, 6, 7])

    return X

  def get_feature_names_out(self):
    pass  




class CustTransDummyMarital(BaseEstimator, TransformerMixin):
  def __init__(self, column_name):
    self.column_name = column_name

  def fit(self, X, y = None):
    return self

  def transform(self, X):
    X[self.column_name + "_dummy"]  = X[self.column_name].apply(lambda x: 1 if x == 'single' else 0)

    return X

  def get_feature_names_out(self):
    pass


class CustTransDummyPoutcome(BaseEstimator, TransformerMixin):
  def __init__(self, column_name):
    self.column_name = column_name

  def fit(self, X, y = None):
    return self

  def transform(self, X):
    X[self.column_name + "_dummy"]  = X[self.column_name].apply(lambda x: 1 if x == 'success' else 0)

    return X

  def get_feature_names_out(self):
    pass


class CustTransEffectJob(BaseEstimator, TransformerMixin):
  def __init__(self, column_name):
    self.column_name = column_name

  def fit(self, X, y=None):
    return self

  def transform(self, X):
    if not isinstance(X, pd.DataFrame):
      raise ValueError("Input must be a pandas DataFrame")

    def categorize(value):
      if value in ['admin', 'retired', 'unemployed', 'student']:
        return 1
      elif value in ['technician', 'management', 'self-employed']:
        return 0
      else:
        return -1
        
    X[self.column_name + "_effect"]  = X[self.column_name].apply(categorize)
      return X

  def get_feature_names_out(self):
    pass


class CustTransDummyPrevious(BaseEstimator, TransformerMixin):
  def __init__(self, column_name):
    self.column_name = column_name

  def fit(self, X, y = None):
    return self

  def transform(self, X):
    X[self.column_name + "_dummy"]  = X[self.column_name].apply(lambda x: 1 if x >= 1 else 0)

    return X 

  def get_feature_names_out(self):
    pass

class CustTransEffectAge(BaseEstimator, TransformerMixin):
  def __init__(self, column_name):
    self.column_name = column_name

  def fit(self, X, y=None):
    return self

  def transform(self, X):
    if not isinstance(X, pd.DataFrame):
      raise ValueError("Input must be a pandas DataFrame")

    def categorize2(value):
      if value <=25:
        return 1
      elif value <=35:
        return 0
      elif value <=55:
        return -1
      else:
        return 1

    X[self.column_name + "_effect"]  = X[self.column_name].apply(categorize2)
      return X

  def get_feature_names_out(self):
    pass


class CustTransEffectEducation(BaseEstimator, TransformerMixin):
  def __init__(self, column_name):
    self.column_name = column_name

  def fit(self, X, y=None):
    return self

  def transform(self, X):
    if not isinstance(X, pd.DataFrame):
      raise ValueError("Input must be a pandas DataFrame")

    def categorize3(value):
      if value in ['basic.6y', 'basic.9y']:
        return -1
      elif value in ['basic.4y', 'professional.course', 'high.school']:
        return 0
      else:
        return 1

    X[self.column_name + "_effect"]  = X[self.column_name].apply(categorize3)
      return X

  def get_feature_names_out(self):
    pass


class CustTransEffectEuribor(BaseEstimator, TransformerMixin):
  def __init__(self, column_name):
    self.column_name = column_name

  def fit(self, X, y = None):
    return self

  def transform(self, X):
    X[self.column_name + "_effect"]  = X[self.column_name].apply(lambda x: 1 if x <= 1.2991789 else (0 if x <= 4.1910304 else -1))

    return X

  def get_feature_names_out(self):
    pass


class CustTransDummyNrEmployed(BaseEstimator, TransformerMixin):
  def __init__(self, column_name):
    self.column_name = column_name

  def fit(self, X, y = None):
    return self

  def transform(self, X):
    X[self.column_name + "_dummy"]  = X[self.column_name].apply(lambda x: 1 if x <= 5099.10 else 0)

    return X

  def get_feature_names_out(self):
    pass
