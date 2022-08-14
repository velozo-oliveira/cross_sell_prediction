import pickle
import numpy as np
import pandas as pd

class HealthInsurance():
    def __init__(self):

        #local API test needs abs home_path
        self.home_path='/home/rafael/Repos/cross_sell_prediction/health_insurance_app/'
        self.annual_premium_scaler            = pickle.load( open( self.home_path + 'parameter/annual_premium_scaler.pkl', 'rb'))
        self.age_scaler                       = pickle.load( open( self.home_path + 'parameter/age_scaler.pkl', 'rb'))
        self.vintage_scaler                   = pickle.load( open( self.home_path + 'parameter/vintage_scaler.pkl', 'rb'))
        self.gender_target_encoder            = pickle.load( open( self.home_path + 'parameter/gender_target_encoder.pkl', 'rb'))
        self.region_code_target_encoder       = pickle.load( open( self.home_path + 'parameter/region_code_target_encoder.pkl', 'rb'))
        self.policy_sales_freq_encoder        = pickle.load( open( self.home_path + 'parameter/policy_sales_freq_encoder.pkl', 'rb'))


    def feature_engineering (self, df2):
      
        # vehicle age
        dict_vehicle_age = {'> 2 Years':'over_2_years', '1-2 Year':'between_1_2_year', '< 1 Year':'below_1_year'}
        df2['vehicle_age'] = df2['vehicle_age'].map(dict_vehicle_age)

        # vehicle damage
        dict_vehicle_damage = {'Yes': 1, 'No': 0}
        df2['vehicle_damage'] = df2['vehicle_damage'].map(dict_vehicle_damage)

        return df2


    def data_preparation (self, df3):

        # transformations
        df3['annual_premium'] = self.annual_premium_scaler.transform( df3[['annual_premium']].values )
        df3['age'] = self.age_scaler.transform( df3[['age']].values )
        df3['vintage'] = self.vintage_scaler.transform( df3[['vintage']].values )
        #df3.loc[:,'gender'] = df3['gender'].map(self.gender_target_encoder) #was not selected
        df3.loc[:,'region_code'] = df3['region_code'].map(self.region_code_target_encoder)
        df3.loc[:,'policy_sales_channel'] = df3['policy_sales_channel'].map(self.policy_sales_freq_encoder)
        #print(df3.isna().sum())
        df3.loc[:,'policy_sales_channel'] = df3.loc[:,'policy_sales_channel'].fillna(0)
        #vars 'vehicle_damage' and 'vehicle_prev_insured' didn't have trasnformations.

        # feature Selection
        cols_selected = ['vintage', 'annual_premium', 'age', 'region_code', 'vehicle_damage', 'policy_sales_channel', 'previously_insured']
        #cols 'id', 'gender', 'driving_license' and 'vehicle_age' were features not selected.

        return df3[cols_selected]


    def get_prediction( self, model, original_data, test_data ):

        #model prediction
        pred = model.predict_proba( test_data )

        #join prediction into original data and sort
        original_data['score'] = pred[:, 1].tolist()
        original_data = original_data.sort_values('score', ascending=False)

        return original_data.to_json( orient= 'records', date_format = 'iso' )


