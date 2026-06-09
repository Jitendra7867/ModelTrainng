# Linear Regression on Life Satisfaction Data

This project uses a simple linear regression model to study the relationship between GDP per capita and life satisfaction.

## What the script does
- Loads the dataset from GitHub:
  https://github.com/ageron/data/raw/main/lifesat/lifesat.csv
- Splits the data into:
  - GDP per capita (input)
  - Life satisfaction (target)
- Trains a linear regression model using scikit-learn
- Prints the model accuracy score
- Displays a scatter plot of the dataset

## Required libraries
Install the following Python packages if they are not already available:
- pandas
- numpy
- matplotlib
- scikit-learn

## How to run
Run the script from this folder:

```bash
python linerRegression.py
```

## Expected output
- A printed accuracy score for the model
- A graph showing GDP per capita vs. life satisfaction
