# Machine Learning Playground

This repository is a growing collection of machine learning projects, experiments, and practice work. The goal is to keep each ML method organized in its own folder, with individual projects grouped under the relevant topic.

As new projects are added, this README will be updated to explain what each project does, which techniques it uses, and how to run it.

## Repository Structure

```text
Machine-Learning-Playground/
  linear_regression/
    CR7_Analytics_Engine/
      ronaldo_goals.py
      ronaldo_mock_match_dataset.csv
```

## Current Projects

### Linear Regression

#### CR7 Analytics Engine

Location:

```text
linear_regression/CR7_Analytics_Engine/
```

This project uses a mock Cristiano Ronaldo match dataset to practice a basic linear regression workflow.

It currently includes:

- Loading match data from a CSV file
- Inspecting competition counts
- Encoding categorical competition data with one-hot encoding
- Splitting the data into training and testing sets
- Training a `LinearRegression` model
- Comparing actual goals with predicted goals
- Calculating Mean Absolute Error
- Plotting actual vs predicted goals

Main file:

```text
ronaldo_goals.py
```

Dataset:

```text
ronaldo_mock_match_dataset.csv
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

## How To Run The Current Project

From the repository root:

```powershell
cd linear_regression\CR7_Analytics_Engine
python ronaldo_goals.py
```

## Notes

This repository is mainly for learning, experimentation, and building a structured machine learning portfolio over time.
