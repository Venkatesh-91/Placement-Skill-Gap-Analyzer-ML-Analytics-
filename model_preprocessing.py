import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("placement_data.csv")
X = df.drop("Placed", axis=1)
y = df["Placed"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)
