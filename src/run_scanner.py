import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import requests
from bs4 import BeautifulSoup

def fetch_web_data(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  scripts = soup.find_all('script')
  return ' '.join(script.text for script in scripts)

def preprocess(data):
  vectorizer = CountVectorizer()
  X = vectorizer.fit_transform(data['Code_Snippet'])
  y = data['label']
  return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
  model = RandomForestClassifier(n_estimators=100)
  model.fit(X_train, y_train)
  return model

def predict(model, X):
  return model.predict(X)

def evaluate(y_test, y_pred):
  return accuracy_score(y_test, y_pred)
