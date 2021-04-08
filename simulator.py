# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:44:33 2021

@author: ZhaoQiWu
"""
import os
import requests


# test prediction function
print('-- Start Predicting --')
country='all'
year='2018'
month='01'
day='06'
query = {'country': country,
         'year': year,
         'month': month,
         'day': day}
json_data = {'query': query, 'type': 'dict'}
res = requests.post('http://127.0.0.1:8080/predict', json=json_data)

print('Prediction Result: ', res.text)

# re-train the model
print('-- Re-train the Model --')
data_dir = os.path.join(".","data","cs-train")
query = {'data_dir': data_dir, 'mode': True}
res = requests.post('http://127.0.0.1:8080/train', json=query)
print('Train Condition: ', res.text)
