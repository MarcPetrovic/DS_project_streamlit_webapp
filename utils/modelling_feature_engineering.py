from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from utils.data_preprap_transformers import ColumnDrop
from utils.data_modelling_transformers import *

def build_pipeline(df):
    cct_month = MonthTrans('month')
    column_drop_month   = ColumnDrop( 'month')
    cct_dayofweek = WeekdayTrans('day_of_week')
    column_drop_dayofweek   = ColumnDrop( 'day_of_week')
    effect_age = CustTransEffectAge( 'age')
    drop_age   = ColumnDrop( 'age')
    effect_education = CustTransEffectEducation('education')
    drop_education   = ColumnDrop( 'education')
    effect_job = CustTransEffectJob( 'job')
    drop_job   = ColumnDrop( 'job')
    dummy_marital = CustTransDummyMarital( 'marital' )
    drop_marital   = ColumnDrop( 'marital')
    effect_euribor3m = CustTransEffectEuribor( 'euribor3m' )
    drop_euribor3m   = ColumnDrop( 'euribor3m')
    dummy_nr_employed = CustTransDummyNrEmployed ( 'nr.employed' )
    drop_nr_employed   = ColumnDrop( 'nr.employed')

    # Pipeline euribor3m
    effect_drop_euribor3m_pipeline = Pipeline(steps=[
        ('effect_euribor3m', effect_euribor3m )
      ,  ('drop_euribor3m', drop_euribor3m )
    ])

    # Pipeline nr.employed
    effect_drop_nremployed_pipeline = Pipeline(steps=[
        ('dummy_nr_employed', dummy_nr_employed )
      ,  ('drop_nr_employed', drop_nr_employed )
    ])

    # Pipeline month
    cct_drop_month_pipeline = Pipeline(steps=[
        ('cct_month', cct_month ) 
      ,  ('drop_month', column_drop_month ) 
    ])


    # Pipeline day_of_week
    cct_drop_dayofweek_pipeline = Pipeline(steps=[
        ('cct_dayofweek', cct_dayofweek )
      ,  ('drop_dayofweek', column_drop_dayofweek )
    ])

    # Pipeline job
    effect_drop_job_pipeline = Pipeline(steps=[
        ('effect_job', effect_job ) 
      ,  ('drop_job', drop_job )
    ])

    # Pipeline age
    effect_drop_age_pipeline = Pipeline(steps=[
        ('effect_age', effect_age ) 
      ,  ('drop_age', drop_age )
        ])
    
    # Pipeline education 
    effect_drop_education_pipeline = Pipeline(steps=[
        ('effect_education', effect_education )
      ,  ('drop_education', drop_education )
    ])

    # Pipeline marital
    dummy_drop_marital_pipeline = Pipeline(steps=[
        ('dummy_marital', dummy_marital )
        ,  ('drop_marital', drop_marital )
    ])

    processor_X2nd = make_column_transformer(
    ( effect_drop_job_pipeline, ['job'] ) ,
    ( effect_drop_education_pipeline, ['education'] ) ,
    ( effect_drop_age_pipeline, ['age'] ) ,
    ( dummy_drop_marital_pipeline, ['marital'] ) ,
    ( effect_drop_euribor3m_pipeline, ['euribor3m'] ),
    ( effect_drop_nremployed_pipeline, ['nr.employed'] )
   ,( NumericalPipeline_X, ['emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'campaign', 'pdays_cat', 'previous'])
   ,( CategorialPipeline_X, ['default_cat', 'housing', 'loan', 'contact', 'poutcome'])
   ,( cct_drop_month_pipeline, ['month'] )
   ,( cct_drop_dayofweek_pipeline, ['day_of_week'] ) 
      ,verbose_feature_names_out=False
      ,remainder='passthrough'  
    )

    return processor_X2nd
