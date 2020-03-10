# Analysis Outline:

In this project wine quality is predicted using Random Forest Algorithm.
The measured features are 'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density','pH', 'sulphates', 'alcohol'.

The project is conducted using following steps:
1. Data Exploration using Univariate and Bivariate analysis techniques.
2. Data Cleaning
3. Data preparation for model
4. Fitting the base Random Forest (RF) model
5. Improving the model by data transformation(SMOTE oversampling of minority classes) and Fitting RF model again to compare results
6. Improving the model further by reducing the categories by 3 based on their quality (quality of 3&4 -> category 1, quality of 5&6 -> category 2, quality of 7&8 -> category 3) and SMOTE oversampling of minority classes 

# Conclusion:
Grouping data into 3 categories along with oversampling minority classes has improved model performance (overall accuracy of 0.93). 
Using original categories combined with oversampling minority classes resulted in overall accuracy of 0.85 and the base model (using original data without any transformation) had overall accuracy of 0.65 without the ability of predicting minority classes. 
