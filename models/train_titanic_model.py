# train_titanic_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load data
df = pd.read_csv("data/titanic.csv")

# Basic cleaning
df = df[["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch"]]
df.dropna(inplace=True)

# Encode 'Sex'
df["Sex"] = LabelEncoder().fit_transform(df["Sex"])

# Split features and target
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
with open("streamlit_app/titanic_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved to streamlit_app/titanic_model.pkl")
