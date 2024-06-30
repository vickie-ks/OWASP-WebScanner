from .run_scanner import fetch_web_data, preprocess, train_model, predict, evaluate
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def main():
  data = pd.read_csv('/data/synthetic_vulnerability_dataset.csv')

  X_train, X_test, y_train, y_test = preprocess(data)
  model = train_model(X_train, y_train)

  y_pred = predict(model, X_test)
  print("Accuracy:", evaluate(y_test, y_pred))

  test_url = input("Please enter the URL to test for vulnerabilities: ")

  web_data = fetch_web_data(test_url)
  if web_data:
    web_data_vectorized = CountVectorizer().fit_transform([web_data])
    predictions = predict(model, web_data_vectorized)
    print("Predictions for the website:", predictions)
  else:
    print("No scripts found at the provided URL.")

if __name__ == '__main__':
  main()
