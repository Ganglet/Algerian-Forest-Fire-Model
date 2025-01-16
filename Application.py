import pickle
import pandas as pd
import numpy as np
from flask import Flask,render_template,jsonify,request

Application= Flask(__name__)
app=Application

Linear_model=pickle.load(open('/Users/angshumansmac/Desktop/Projects/ML_&_NLP_udemy/Resume_Worthy_Projects/Algerian_Forest/Models/Linear.pkl','rb'))
standard_scaler=pickle.load(open('/Users/angshumansmac/Desktop/Projects/ML_&_NLP_udemy/Resume_Worthy_Projects/Algerian_Forest/Models/Scalar.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        DC = float(request.form.get('DC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,DC,ISI,Classes,Region]])
        result=Linear_model.predict(new_data_scaled)

        return render_template('home1.html',results=result[0])
    
    else:
        return render_template('home1.html')

if __name__=="__main__":
    app.run(host='0.0.0.0')
    