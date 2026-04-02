import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Create folder
os.makedirs("model", exist_ok=True)

# Load data
data = pd.read_csv("house_data.csv")

# Convert categorical
data = pd.get_dummies(data, columns=['location'])

# Features & target
X = data.drop("price", axis=1)
y = data["price"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Better model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Save
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Better model trained!")