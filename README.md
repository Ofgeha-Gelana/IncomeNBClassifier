# Income Prediction using Gaussian Naive Bayes Classifier

This project predicts whether a person makes more than 50K a year based on various features such as age, workclass, education, etc., using a Gaussian Naive Bayes classifier.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Model Evaluation](#model-evaluation)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)

## Project Overview
This project uses the **Adult Income Dataset** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/adult). The goal is to predict whether a person earns more than 50K a year based on different demographic features. A Gaussian Naive Bayes classifier is used for classification, and model performance is evaluated using accuracy, confusion matrix, and other metrics.

## Dataset
The dataset used is the **Adult Income Dataset**, which contains the following columns:

- `age`: Age of the person.
- `workclass`: The type of employment.
- `fnlwgt`: Final weight.
- `education`: The highest level of education.
- `education_num`: Numeric representation of the education level.
- `marital_status`: Marital status.
- `occupation`: Type of occupation.
- `relationship`: Type of relationship.
- `race`: Race of the person.
- `sex`: Gender of the person.
- `capital_gain`: Capital gain in dollars.
- `capital_loss`: Capital loss in dollars.
- `hours_per_week`: Hours worked per week.
- `native_country`: Country of origin.
- `income`: Target variable (<=50K or >50K).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/IncomeNBClassifier.git
   cd IncomeNBClassifier
