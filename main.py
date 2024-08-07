from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=31)

# Train the logistic regression model
model = RandomForestClassifier(
        n_estimators=100, random_state=31)
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f'Accuracy: {accuracy}')

# Save the trained model to a file
joblib.dump(model, 'model.pkl')
print('Model saved as model.pkl')
