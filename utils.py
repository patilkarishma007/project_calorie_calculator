import pickle 
import pandas as pd
import json
import os
import numpy as np
import config
import warnings
warnings.filterwarnings('ignore')

class CaloriesBurned():
    def __init__(self):
        pass

    def __load_data(self):
        path_to_model = os.path.join("artifacts", "lin_reg_model.pkl")
        path_to_json = os.path.join("artifacts", "column_data.json")

        with open(path_to_model,'rb')as f:
            self.model=pickle.load(f)

        with open(path_to_json,'r')as f:
            self.column_data = json.load(f)


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
    path_to_csv = os.path.join("Data", "calories_burned_dataset.csv")
    df = pd.read_csv(path_to_csv)
   
    return df

#if __name__ == "__main__":
    #Cal_Burn=CaloriesBurned()
    #Cal_Burn.load_data()