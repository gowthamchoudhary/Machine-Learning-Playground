# Machine Learning Playground

This repository is a growing collection of machine learning projects, experiments, and practice work. Each topic is organized into its own folder, with individual projects grouped under the relevant technique.

The current focus is regression: building small, hands-on projects that load datasets, prepare features, train models, evaluate predictions, and visualize results.

## Repository Structure

```text
ML-playGround/
  linear_regression/
    CR7_Analytics_Engine/
      ronaldo_goals.py
      ronaldo_mock_match_dataset.csv
    PolyRegression/
      icecreamsellingpred.py
      Ice_cream selling data.csv
```

## Current Projects

### Linear Regression

#### CR7 Analytics Engine

Location:

```text
linear_regression/CR7_Analytics_Engine/
```

This project uses a mock Cristiano Ronaldo match dataset to practice a basic linear regression workflow for predicting goals from match statistics.

It includes:

- Loading match data from a CSV file
- Inspecting competition counts
- Encoding categorical competition data with one-hot encoding
- Splitting the data into training and testing sets
- Training a `LinearRegression` model
- Reviewing model intercepts and feature coefficients
- Comparing actual goals with predicted goals
- Calculating Mean Absolute Error
- Plotting actual vs. predicted goals

Run it from the project folder:

```powershell
cd linear_regression\CR7_Analytics_Engine
python ronaldo_goals.py
```

### Polynomial Regression

#### Ice Cream Sales Prediction

Location:

```text
linear_regression/PolyRegression/
```

This project uses temperature and ice cream sales data to practice polynomial regression. It models the relationship between temperature and sales using polynomial features and a linear regression model.

It includes:

- Loading an ice cream sales dataset from CSV
- Exploring the dataset with summary methods
- Checking for missing values
- Visualizing feature relationships with Seaborn
- Creating polynomial features with `PolynomialFeatures`
- Training a `LinearRegression` model
- Evaluating predictions with `r2_score`
- Plotting the polynomial regression curve

Run it from the project folder:

```powershell
cd linear_regression\PolyRegression
python icecreamsellingpred.py
```

## Requirements

The projects use Python and common machine learning/data analysis libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Install the dependencies with:

```powershell
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Planned Additions

Future folders may include projects for:

- Logistic Regression
- Decision Trees
- Random Forest
- K-Nearest Neighbors
- Support Vector Machines
- Clustering
- Neural Networks

## Notes

This repository is mainly for learning, experimentation, and building a structured machine learning portfolio over time.
