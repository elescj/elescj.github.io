# 📌 Predicting Boston Housing Prices: A Linear Regression Approach
This project applies linear regression to forecast Boston housing prices based on key property features.

## 📂 Table of Contents
- [Overview](#-overview)
- [Dataset](#-dataset)
- [Problem Statement](#-problem-statement)
- [Methodology](#-methodology)
- [Results](#-results)
- [Insights & Recommendations](#-insights--recommendations)
- [Technologies Used](#technologies-used)
- [How to Run](#how-to-run)

## 🧠 Overview
This project implements a supervised learning pipeline to predict housing prices in the Boston metropolitan area using the classic Boston Housing dataset. It models the relationship between housing prices and a range of explanatory variables including crime rate, average number of rooms, accessibility to highways, and more. The pipeline includes data preprocessing, exploratory data analysis (EDA), feature selection, model training, and evaluation using regression metrics such as RMSE and 𝑅2. The objective is to assess the effectiveness of linear regression in modeling continuous housing price data and to interpret the influence of individual predictors on pricing outcomes.

## 📊 Dataset
The data and problem were provided by the Applied Data Science Program by MIT. The dataset is a 506 × 13 CSV file, where each row represents a residential property in a suburb or town of Boston. It was originally drawn from the Boston Standard Metropolitan Statistical Area (SMSA) in 1970.

Each record includes 13 input features describing property and neighborhood characteristics, and one target variable: the median value of owner-occupied homes (in $1000s).

Detailed feature descriptions are listed in the table below:
| Feature   | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| `CRIM`    | Per capita crime rate by town                                               |
| `ZN`      | Proportion of residential land zoned for lots over 25,000 sq.ft.           |
| `INDUS`   | Proportion of non-retail business acres per town                            |
| `CHAS`    | Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)       |
| `NOX`     | Nitric Oxide concentration (parts per 10 million)                          |
| `RM`      | The average number of rooms per dwelling                                    |
| `AGE`     | Proportion of owner-occupied units built before 1940                        |
| `DIS`     | Weighted distances to five Boston employment centers                        |
| `RAD`     | Index of accessibility to radial highways                                   |
| `TAX`     | Full-value property-tax rate per $10,000                                    |
| `PTRATIO` | Pupil-teacher ratio by town                                                 |
| `LSTAT`   | Percentage of lower status population                                       |
| `MEDV`    | Median value of owner-occupied homes in $1000s (target variable)            |

## ❓ Problem Statement
Accurately estimating housing prices is a persistent challenge due to the numerous and often interrelated factors that influence real estate markets — particularly the issue of multicollinearity among predictors. This project aims to develop a linear regression model to predict housing prices in Boston using key features from the dataset. The objective is to minimize prediction error while identifying the most influential variables, offering a foundational, interpretable baseline for housing price modeling and further machine learning applications.

## 🔎 Methodology
Steps of data cleaning, model building, evaluation...

## 📈 Results
Key performance metrics, accuracy, visuals...

## 💡 Insights & Recommendations
What did you learn? What actions can be taken?

<a id="technologies-used"></a>
## ⚙️ Technologies Used
List tools and libraries: Python, Pandas, Scikit-learn, etc.

<a id="how-to-run"></a>
## ▶️ How to Run
1. Clone the repo  
2. Install requirements using `pip install -r requirements.txt`  
3. Run the script with `python main.py`
