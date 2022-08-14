import pickle
import os
import pandas as pd
from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance

# load model in memory
model = pickle.load(open('model/Health_Insurance.pkl', 'rb'))

# initialize API
app = Flask(__name__)

# create endpoint
@app.route('/predict', methods=['POST'])
def health_insurance_predict():
    test_json = request.get_json()

    if test_json: #there is data
        if isinstance(test_json, dict): #unique row 
            test_raw = pd.DataFrame(test_json, index = [0])
        else: # multiple rows
            test_raw = pd.DataFrame(test_json, columns = test_json[0].keys()) 
        
        #needed cause test_raw will be overwritten on pipeline
        test_raw_original = test_raw.copy()

        # instantiate HealthInsurance class
        pipeline = HealthInsurance()

        # data cleaning
        #df1 = pipeline.data_cleaning(test_raw)
        #print('df1 done')
        #print(df1.head())
        #print(df1.head().values)
        
        # feature engineering
        df2 = pipeline.feature_engineering(test_raw)
        #print('df2 done')
        #print(df2.head())
        #print(df2.head().values)

        # data preparation
        df3 = pipeline.data_preparation(df2)
        #print('df3 done')
        #print(df3.head())
        #print(df3.head().values)
    
        # prediction
        df_response = pipeline.get_prediction(model, test_raw_original, df3)
        
        #returns a json
        return df_response
       
    else: #if empty:
        return Response('{}', status = 200, mimetype = 'application/json')

if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000 )
    app.run( host = '0.0.0.0', port=port )
