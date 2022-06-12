# Traffic Prediction

## Problem Statement

Traffic prediction means forecasting the volume and
density of traffic flow, usually for the purpose of managing vehicle movement, reducing congestion, and generating the optimal (least time or energy-consuming) route. The task of detecting traffic for the next day, week etc.

## Dataset

The dataset contains 4 components (DateTime, Junction, Vehicles, id)
across 48120 rows. The DateTime column shows the timestamp along with the respective date.

- **DateTime** - It shows the date and timestamp
- **Junction** - It tells the junction number for which vehicles are present
- **Vehicles** - It tells the number of vehicles
- **id** - It tells the id number of a timestamp

Link to the dataset: [traffic.csv](https://github.com/ayushabrol13/Traffic-Prediction---PRML-Course-Project/blob/master/traffic.csv)

## Implemented the following algorithms

- **Decision Tree Regressor**
  Decision tree builds regression or classification models in
  the form of a tree structure. It breaks down a dataset into smaller and smaller subsets
  while at the same time an associated decision tree is incrementally developed. The final
  result is a tree with decision nodes and leaf nodes.
- **Linear Regression**
  Linear regression performs the task to predict a dependent
  variable value (y) based on a given independent variable (x). So, this regression
  technique finds out a linear relationship between x (input) and y(output)
- **Random Forest Regressor**
  A Random Forest is an ensemble technique capable of
  performing both regression and classification tasks with the use of multiple decision
  trees and a technique called Bootstrap and Aggregation, commonly known as bagging.
  The basic idea behind this is to combine multiple decision trees in determining the final
  output rather than relying on individual decision trees.
- **XGBoost Regressor**
  Extreme Gradient Boosting, or XGBoost for short, is an ef icient
  ensemble learning algorithm via gradient boosting. It provides a parallel implementation of decision trees that are created in a sequential form, where weights play an important role.
- **LightGBM Regressor**
  Light GBM is a gradient boosting framework that uses
  tree-based learning algorithms. Light GBM grows trees vertically while other algorithms grow trees horizontally meaning that Light GBM grows trees leaf-wise while other algorithms grow level-wise. It will choose the leaf with max delta loss to grow. When growing the same leaf, a Leaf-wise algorithm can reduce more loss than a level-wise algorithm.
- **GridSearchCV for Hyperparameter Tuning**
  For tuning the hyperparameters, We have used Grid Search CV, which uses a different combination of all the specified hyperparameters and their values and calculates the performance for each combination and selects the best value for the hyperparameters.

## Traffic Flow across different junctions according to time-period

![Traffic Flow](https://raw.githubusercontent.com/ayushabrol13/Traffic-Prediction---PRML-Course-Project/master/plots/traffic_flow.png "Traffic Flow across Junctions")

## Contributors

[Ayush Abrol](https://github.com/ayushabrol13)

[Aryan Tiwari](https://github.com/AryanTiwarii)

[Neehal Prakash Bajaj ]()
