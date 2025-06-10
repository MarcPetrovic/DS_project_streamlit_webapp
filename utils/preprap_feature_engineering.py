from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from utils.data_preprap_transformers import *

def build_pipeline(df):
    column_drop_ROW_ID   = ColumnDrop('ROW_ID')
    column_drop_default  = ColumnDrop('default')
    column_drop_pdays    = ColumnDrop('pdays')
    cat_default          = CategorizeDefault('default')
    cct_target           = CustTrans('y')
    cct_pdays            = CustTransPdays('pdays')

    numerical_features = [c for c in df.columns if df[c].dtype == 'float64']
    categorical_features = ['job', 'marital', 'education', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome']

    num_pipeline = Pipeline([('imputer', SimpleImputer(strategy='mean'))])
    cat_pipeline = Pipeline([
        ('replace_unknowns', ReplaceUnknowns()),
        ('imputer2', SimpleImputer(strategy='most_frequent'))
    ])
    # Pipeline feature default
    cat_drop_default_pipeline = Pipeline(steps=[
        ('cat_default', cat_default ) 
      ,  ('drop_default', column_drop_default ) 
    ])
    
    # Pipeline synthetic feature ROW_ID
    cat_drop_ROW_ID_pipeline = Pipeline(steps=[
        ('drop_row_id', column_drop_ROW_ID ) 
    ])
    
    # Pipeline for target feature
    cct_pipeline = Pipeline(steps=[
        ('custom_trans', cct_target)
    ])
    
    # Pipeline for feature pdays 
    cct_drop_pdays_pipeline = Pipeline(steps=[
        ('custom_trans', cct_pdays ) 
      ,  ('drop_pdays', column_drop_pdays ) 
    ])
    preprocessor = make_column_transformer(
    ( cat_drop_ROW_ID_pipeline, ['ROW_ID'] ) ,
    ( cct_pipeline, ['y'] ) ,
    ( cat_drop_default_pipeline, ['default'] ) ,
    ( cct_drop_pdays_pipeline, ['pdays'] ) ,
    ( numerical_pipeline, numerical_features),
    ( categorical_pipeline, categorical_features)
       ,verbose_feature_names_out=False
       ,remainder='passthrough'  # remain all other features
    )

    return preprocessor
