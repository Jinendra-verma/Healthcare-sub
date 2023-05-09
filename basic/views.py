from django.shortcuts import render
from django.conf import settings

import numpy as np    
import pandas as pd
import openai


openai.api_key = settings.OPENAI_API_KEY

def Welcome(request):
    return render(request, 'index.html' ,)

from joblib import load
model = load('./MLmodel/model.joblib')

features = pd.read_csv("./features.csv")
# features = features.drop(["Unnamed: 133"],axis=1)
features = features.drop(["prognosis"],axis=1)
feature_names = features.columns.tolist()


def Disease_predict(request):
    symptom = request.POST.getlist('symp')
    N= len(symptom)
    X_input = np.zeros((1,132))

    for i in symptom:
        print(i)
        X_input[0,int(i)] = 1
    
    # for i in range(132):
    #      print(X_input[0][i] , " ")

    df = pd.DataFrame(X_input, columns=feature_names)     

    disease = model.predict(df)
    print(disease)

    # disease = 'Malaria'

    return render(request, 'disease.html' , {'disease' : disease} )

# def view_detail(request):
#     if request.method == "POST":
#         search_word = request.POST['data']

# def example_view(request, variable):
#     print(variable)

def what_is(input):
        return f'what is {input} ?'    

def Disease_info(request):
    result = ''
    if request.method == "POST":
        disease = request.POST.get('disease_name')
        my_disease = str(disease)[1:-1]
        print(type(disease))
        print("disease=",disease)
        

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=what_is(disease),
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.6,
        )
        # print(response)
        result = response.choices[0].text.replace('\n', '<br>')
        # print(result)

    return render(request, 'disease.html', {'result': result , 'disease' : my_disease})




