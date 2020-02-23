from django.conf import settings
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import joblib
import os


def get_ml_predictions(state, factor, start_year, end_year):
    #df = joblib.load("./processed_data.joblib")
    df = joblib.load(os.path.join(settings.BASE_DIR, "research/processed_data.joblib"))

    t = df[df['State'] == state].sort_values(by='Year')

    clf = LinearRegression()
    clf.fit(t[['Year']], t[factor])
    years = np.arange(start_year, end_year+1, 1)

    return clf.predict(years.reshape(-1, 1))