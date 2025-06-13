# 🏠 Predicting Boston Housing Prices: A Linear Regression Approach
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
The data and problem were provided by the *Applied Data Science Program* by MIT. The dataset is a **506 × 13** CSV file, where each row represents a residential property in a suburb or town of Boston. It was originally drawn from the **Boston Standard Metropolitan Statistical Area (SMSA) in 1970**.

Each record includes **13 input features** describing property and neighborhood characteristics, and one **target variable**: the median value of owner-occupied homes (in $1000s).

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
The following steps outline the end-to-end process used in this project:

1. **Data Overview**  
   The Boston Housing dataset was loaded into a pandas DataFrame for preliminary inspection. Key characteristics such as data dimensions, data types, presence of duplicates or null values, and the number of unique values per feature were assessed.
   
3. **Exploratory Data Analysis (EDA)**  
   - **Univariate analysis** was conducted to understand the distribution of each feature using histograms and descriptive statistics.  
   - **Bivariate analysis** explored relationships between independent variables and the target (`MEDV`) using scatter plots and correlation heatmaps, helping to identify potential multicollinearity and feature relevance.

4. **Model Building – Linear Regression**  
   - Split the dataset into training and testing sets (typically 80/20).  
   - Examined multicollinearity using correlation matrices and VIF; dropped highly collinear features.  
   - Built an initial linear regression model and evaluated coefficient significance.  
   - Removed statistically insignificant variables to improve model interpretability and re-fit the model.  
   - Verified linear regression assumptions (linearity, normality, homoscedasticity, independence).  
   - Evaluated model performance using **Root Mean Squared Error (RMSE)**, **Mean Absolute Error (MAE)**, and **Mean Absolute Percentage Error (MAPE)**.  
   - Applied **k-fold cross-validation** to assess model generalizability.  
   - Constructed the final linear regression model based on refined features and evaluation metrics.

## 📈 Results

### 🔢 Model Performance Metrics
The linear regression model was evaluated using standard regression metrics on the test set:
| Metric                                    | Value             |
|-------------------------------------------|-------------------|
| R² Score (Coefficient of Determination)   | 0.729 (+/- 0.232) |
| RMSE (Root Mean Squared Error)            | 0.198045          |
| MAE (Mean Absolute Error)                 | 0.151284          |
| MAPE (Mean Absolute Percentage Error)     | 5.257965          |

These results indicate that the model explains approximately 73% of the variance in housing prices and has an average error of 23%.

---

### 📊 Model Coefficients
Below are the learned coefficients for each feature in the model:
| Feature   | Coefficient | Interpretation (qualitative impact)                   |
|-----------|-------------|--------------------------------------------------------|
| const     | 4.649       | Baseline value when all features are 0                |
| CRIM      | -0.0125     | Higher crime rate slightly decreases housing price    |
| CHAS      | +0.1198     | Proximity to Charles River slightly increases price   |
| NOX       | -1.0562     | Higher air pollution (NOx) strongly decreases price   |
| RM        | +0.0589     | More rooms per dwelling increases price               |
| DIS       | -0.0441     | Greater distance from employment centers reduces value|
| RAD       | +0.0078     | Higher accessibility to highways slightly increases price |
| PTRATIO   | -0.0485     | Higher student–teacher ratio reduces price            |
| LSTAT     | -0.0293     | Higher % of lower status population decreases price   |

*Note: The magnitude and sign of coefficients indicate each feature’s relative impact.*

---

### 🧪 Residual Analysis
To assess the model assumptions and quality of fit, the following plots were analyzed:
- ✅ **Residuals vs. Fitted Values** (for linearity & homoscedasticity)
- ✅ **Histogram of Residuals** (for normality)
- ✅ **QQ Plot** (for distribution shape)
- ✅ **Actual vs. Predicted** plot (for overall fit)

![Residuals vs. Fitted Values](residual.png)
![Histogram of Residuals](histogram.png)
![QQ Plot](qq-plot.png)

**Example code (matplotlib)**
```python
# Plot histogram of residuals.
sns.histplot(residuals, kde=True)
# Show the plot.
plt.show()
# Plot q-q plot of residuals
stats.probplot(residuals, dist = "norm", plot = pylab)
# Show the plot.
plt.show()
```

## 💡 Insights & Recommendations
- Actionable insights have been derived for each key variable influencing housing prices.
- Strategic recommendations are provided for stakeholders such as city planners, real estate developers, homeowners, prospective buyers, and realtors to support data-informed decisions.

<a id="technologies-used"></a>
## ⚙️ Technologies Used
- **Python** – General purpose programming
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computations
- **Matplotlib & Seaborn** – Data visualization
- **Scikit-learn** – Model training and evaluation
- **Statsmodels** – Statistical modeling (OLS regression, VIF)
- **SciPy** – Statistical tests and probability distributions
- **Pylab** – Numerical plotting and analysis
- **Warnings** – For suppressing non-critical output

<a id="how-to-run"></a>
## ▶️ How to Run
1. Clone the repo  
2. Install requirements using `pip install -r requirements.txt`  
3. Run the script with `python main.py`
