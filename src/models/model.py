import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

class GDPModel:
    def __init__(self):
        self.model = RandomForestRegressor()
    
    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)
    
    def preprocess_data(self):
        # Implement preprocessing steps here
        # For example, handling missing values, feature selection, etc.
        pass
    
    def train(self, features, target):
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        return mse
    
    def predict(self, new_data):
        return self.model.predict(new_data)