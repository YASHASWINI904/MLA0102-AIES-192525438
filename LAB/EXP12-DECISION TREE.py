import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Income': ['Low', 'Low', 'Medium', 'Medium', 'High',
               'High', 'Medium', 'Low', 'High', 'Medium'],

    'Credit_Score': ['Poor', 'Good', 'Good', 'Excellent', 'Good',
                     'Excellent', 'Poor', 'Poor', 'Excellent', 'Good'],

    'Employment': ['No', 'Yes', 'Yes', 'Yes', 'Yes',
                   'No', 'Yes', 'No', 'Yes', 'Yes'],

    'Loan_Approved': ['No', 'No', 'Yes', 'Yes', 'Yes',
                      'Yes', 'No', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

# Encode categorical data
encoder = LabelEncoder()

for column in df.columns:
    df[column] = encoder.fit_transform(df[column])

# Separate input and output
X = df[['Income', 'Credit_Score', 'Employment']]
y = df['Loan_Approved']

# Create Decision Tree Classifier
model = DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)

# Train the model
model.fit(X, y)

# Predict loan for a new customer
new_customer = [[0, 0, 1]]

prediction = model.predict(new_customer)

# Display result
if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")

# Display Decision Tree
plt.figure(figsize=(12, 8))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=['Rejected', 'Approved'],
    filled=True
)

plt.show()
