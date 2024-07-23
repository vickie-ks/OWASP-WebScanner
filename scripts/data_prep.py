import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os

def load_data(file_path):
    data = pd.read_csv(file_path)
    print("Columns in the dataset:", data.columns)
    return data

def preprocess_data(data):
    # Example preprocessing steps, modify according to your dataset
    label_encoder = LabelEncoder()
    
    # Ensure the column name is correct
    target_column = 'vuln_type'  # Update this to the correct column name
    if target_column not in data.columns:
        raise KeyError(f"Column '{target_column}' not found in the dataset.")
    
    data[target_column] = label_encoder.fit_transform(data[target_column])

    X = data.drop(target_column, axis=1)
    y = data[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test, label_encoder

if __name__ == "__main__":
    # Get the absolute path of the data directory
    base_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(base_path, '../data/OWASP_Client_side_Sheet3.csv')
    
    data = load_data(file_path)
    X_train, X_test, y_train, y_test, label_encoder = preprocess_data(data)
    
    X_train.to_csv(os.path.join(base_path, '../data/X_train.csv'), index=False)
    X_test.to_csv(os.path.join(base_path, '../data/X_test.csv'), index=False)
    y_train.to_csv(os.path.join(base_path, '../data/y_train.csv'), index=False)
    y_test.to_csv(os.path.join(base_path, '../data/y_test.csv'), index=False)
