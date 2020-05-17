# Project Introduction:

Higgs dataset has been produced using Monte Carlo simulations at Physics & Astronomy, Univ. of California Irvine. The dataset can be found at (http://archive.ics.uci.edu/ml/datasets/HIGGS).

It is a classification problem and identifies exotic particles in high-energy physics based on the sensors information(Signal process produces Higgs bosons(label 1) and a background process does not (label 0)).

The first 21 features (columns 2-22) are kinematic properties measured by the particle detectors in the accelerator. The last seven features are functions of the first 21 features which are high-level features derived by physicists to help discriminate between the two classes. For this project, we ignore the last 7 columns and use Featuretools python library (https://www.featuretools.com/) to create new features and compare with previous studies.

# Project Outline:

In this project, Higgs dataset is analyzed in several steps:
1. Data cleaning and preprocessing using Preprocess module.
2. Feature Engineering by creating new features using Featuretools package and feature selection methods. This methodology is done using Features module.
3. Fitting XGBoost, Catboost, and LightGBM models, and using Hyperopt and Optuna optimizers. 
4. Unit testing and integration testing of all the developed libraries using pytest.
5. Comparing of different fitted models and optimization methods against each other and AutoML of GCP.
6. Comparing the results with AutoML of GCP.

# Contributors:

This is a group project and following are the list of contibutors:
Ahmed Al-Baz (https://github.com/albazahm)
Birkamel Kaur
Kshitij Mamgain (https://github.com/kshitijmamgain)
Sasha Hajy Hassani (https://github.com/SHH116)
Tanaby Zibamanzar Mofrad (https://github.com/tanabymofrad)
