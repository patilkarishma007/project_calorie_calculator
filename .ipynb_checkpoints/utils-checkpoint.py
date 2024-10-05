import pickle
import pandas as pd
import json
import numpy as np
import config
import warnings
warnings.filterwarnings('ignore')

class CaloriesBurned():
    def __init__(self):
        pass

    def __load_data(self):
        with open(r"artifacts/lin_reg_model.pkl",'rb')as f:
            self.model=pickle.load(f)

        with open(r"artifacts/column_data.json",'r')as f:
            self.column_data=json.load(f)

            self.column_name=self.model.feature_names_in_
            self.feature_counts=self.model.n_features_in_

    def get_Predicated_calories_burned(self,Gender,Age,Height,Weight,Duration):

        self.__load_data()
        #Gender = Gender.lower()

        Gender = self.column_data['Gender'][Gender]
        print("Gender", Gender)
        test_array=np.zeros((1,self.feature_counts))
        test_array[0,0]=Gender
        test_array[0,1]=Age
        test_array[0,2]=Height
        test_array[0,3]=Weight
        test_array[0,4]=Duration

        predicated_Calories= np.around(self.model.predict(test_array)[0],3)

        return (predicated_Calories)

def load_Dataset():
    df=pd.read_csv(r"Data/calories_burned_dataset.csv")
    return df