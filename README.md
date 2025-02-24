# Income Classification: Gaussian Naïve Bayes vs. Logistic Regression

## Table of Contents
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Methodology](#methodology)
  - [Gaussian Naïve Bayes](#gaussian-naïve-bayes)
  - [Logistic Regression](#logistic-regression)
- [Results and Comparison](#results-and-comparison)
- [Conclusion](#conclusion)
- [How to Run](#how-to-run)

## Problem Statement
The objective of this project is to classify whether a person earns more than $50K per year based on demographic and employment-related attributes. This classification is done using two models:
- **Gaussian Naïve Bayes**
- **Logistic Regression**

## Dataset
The dataset used for this project is the **Adult Income Dataset**, which contains various features such as age, education, occupation, and hours worked per week.

## Methodology
### Gaussian Naïve Bayes
Gaussian Naïve Bayes is a probabilistic classifier based on Bayes' Theorem, assuming that the features follow a normal distribution.

- **Training Accuracy:** 80.67%
- **Test Accuracy:** 80.83%
- **Confusion Matrix:**
  ```
  [[5999 1408]
   [ 465 1897]]
  ```
  - **True Positives (TP):** 5999
  - **True Negatives (TN):** 1897
  - **False Positives (FP):** 1408
  - **False Negatives (FN):** 465

### Logistic Regression
Logistic Regression is a linear model that predicts the probability of a categorical outcome.

- **Training Accuracy:** 84.72%
- **Test Accuracy:** 84.72%
- **Confusion Matrix:**
  ```
  [[6879  528]
   [ 965 1397]]
  ```
  - **True Positives (TP):** 6879
  - **True Negatives (TN):** 1397
  - **False Positives (FP):** 528
  - **False Negatives (FN):** 965

## Results and Comparison
| Model                   | Training Accuracy | Test Accuracy | TP   | TN   | FP   | FN   |
|-------------------------|------------------|--------------|------|------|------|------|
| Gaussian Naïve Bayes    | 80.67%           | 80.83%       | 5999 | 1897 | 1408 |  465 |
| Logistic Regression     | 84.72%           | 84.72%       | 6879 | 1397 |  528 |  965 |

- Logistic Regression outperforms Gaussian Naïve Bayes in terms of accuracy.
- Gaussian Naïve Bayes has a higher False Positive rate compared to Logistic Regression.
- Logistic Regression is more reliable for this classification task due to its higher accuracy and lower FP rate.

## Conclusion
From the results, **Logistic Regression** is the better model for predicting whether a person makes more than $50K, as it achieves higher accuracy and lower misclassification rates.

However, Gaussian Naïve Bayes is a simpler and faster model that can still be useful when dealing with large datasets.

## How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/Ofgeha-Gelana/IncomeNBClassifier.git
   ```
2. Navigate to the project directory:
   ```sh
   cd IncomeNBClassifier
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

   ```
4. Evaluate the results.

## Future Work
- Optimize hyperparameters for better performance.

---

## 🚀 Task - 2

<!-- - **Bayesian Optimization:**   -->
[**Bayesian Optimization**](https://medium.com/@ofgehagelana2019/the-paper-practical-bayesian-optimization-of-machine-learning-algorithms-by-jasper-snoek-hugo-8819a2981f79)  