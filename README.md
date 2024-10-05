## PROJECT OVERVIEW
This project predicts the number of calories burned during exercise based on user input such as Gender, Age, Height, Weight, and Duration. The application uses machine learning models to estimate calorie burn based on this input data.

#### OBJECTIVE
The goal of this project is to create an easy-to-use web interface that allows users to predict the number of calories they are  burning during exercise, based on their body measurements and workout duration. 
  The model behind the web application is trained on  a dataset that includes several health-related metrics.

   Features:

   1.User Input Form: A simple and interactive form t input personal details like gender, age, height, weight, Duration and exercise duration.

   2.Machine Learning Model: A linear regression mode trained to predict calories burned based on input variables.

   3.Real-time Predictions: The form provides prediction on calories burned as soon as the user submits the data.

#### DATA DESCRIPTION 
   1.Gender: The biological sex of the individual, can be either Male or Female.
   
   2.Age: Age of the individual in years.This indicates the age of the person performing the exercise.
   
   3.Height (cm): Height of the individual in centimeters.Used to calculate BMI and other factors affecting calorie burn.
   
   4.Weight (kg): Weight of the individual in kilograms. This is a crucial factor in determining how many calories a person burns during an exercise session.
   
   5.Duration (mins):The duration of the exercise session in minutes. The longer the duration, the more calories are burned.
   
   6.Calories Burned: The target variable representing the total number of calories burned during the exercise session.
     This is calculated based on the individual's characteristics (age, weight, height) and the duration of the exercise.

Data source : https://www.kaggle.com/mirichoi0218/insurance

## How to RUN project
#### 1. Install Required Libraries

```
pip install -r requirements.txt
```

#### 2. RUN main file
```python
python main.py
```
