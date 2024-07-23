import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
import joblib

def load_data():
    X_test = pd.read_csv('../data/X_test.csv')
    y_test = pd.read_csv('../data/y_test.csv').values.ravel()
    return X_test, y_test

def evaluate_model(X_test, y_test):
    model = joblib.load('../models/model.pkl')
    y_pred = model.predict(X_test)
    
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    X_test, y_test = load_data()
    evaluate_model(X_test, y_test)
