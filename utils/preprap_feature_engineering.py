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
        ('imputer', SimpleImputer(strategy='most_frequent'))
    ])

    preprocessor = make_column_transformer(
        (Pipeline([('drop_row_id', column_drop_ROW_ID)]), ['ROW_ID']),
        (Pipeline([('custom_trans', cct_target)]), ['y']),
        (Pipeline([('cat_default', cat_default), ('drop_default', column_drop_default)]), ['default']),
        (Pipeline([('custom_trans', cct_pdays), ('drop_pdays', column_drop_pdays)]), ['pdays']),
        (num_pipeline, numerical_features),
        (cat_pipeline, categorical_features),
        remainder='passthrough',
        verbose_feature_names_out=False
    )

    return preprocessor
