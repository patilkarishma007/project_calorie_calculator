from flask import Flask,render_template,request,jsonify
from utils import CaloriesBurned,load_Dataset
import config
import pandas as pd
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
Cal_Burn=CaloriesBurned()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/Gender")
def Gender():
    df=load_Dataset()
    df['Gender'] = df['Gender'].apply(lambda x : x.lower())
    
    return jsonify(list(df['Gender'].unique()))



@app.route('/prediction', methods=['POST'])
def prediction():
    data=request.form
    print("Data :",data)

    Gender=data['Gender']
    Age=data['Age']
    Height=data['Height']
    Weight=data['Weight']
    Duration=data['Duration']

    
    pred_Calories=Cal_Burn.get_Predicated_calories_burned(Gender,Age,Height,Weight,Duration)
    print(f"Predicated Calories :,{ pred_Calories}")

    return jsonify({'Predicated_Calories':pred_Calories})


if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)    
    
   

