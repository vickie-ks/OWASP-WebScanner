import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_data():
    X_train = pd.read_csv('../data/X_train.csv')
    y_train = pd.read_csv('../data/y_train.csv').values.ravel()
    return X_train, y_train

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, '../models/model.pkl')

if __name__ == "__main__":
    X_train, y_train = load_data()
    train_model(X_train, y_train)
