# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model is a Random Forest Classifier trained on the UCI Census Income dataset. The goal of the model is to predict whether someone earns more than $50K per year based on different demographic features. I used scikit-learn, pandas, and numpy to build and train the model.

## Intended Use

The model is meant for academic and learning purposes as part of the Udacity Machine Learning DevOps Nanodegree. It’s not meant to be used in production or for making real HR or financial decisions.

## Training Data

The model was trained using the Census Income dataset, which has 14 demographic and work-related features. Some of these include workclass, education, marital-status, occupation, relationship, race, sex, and native-country. The target column was salary, and I used an 80/20 split for training and testing.


## Evaluation Data

I evaluated the model using 20% of the original data (the test split). I didn’t use any data augmentation or synthetic data.

## Metrics

I used standard classification metrics to evaluate how well the model performs:

- **Precision**: 0.7419  
- **Recall**: 0.6384  
- **F1 Score**: 0.6863

## Ethical Considerations

This model should not be used in a real-world setting. It might make biased predictions, and it hasn’t gone through any official validation or fairness testing.

## Caveats and Recommendations

This model was trained on a small, fixed dataset, so it might not perform well on data from different groups or time periods.
