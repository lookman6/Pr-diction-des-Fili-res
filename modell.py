import pandas as pd
import dill

from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

df = pd.read_excel('data_decision_tree.xlsx')
df.head()
feature_cols = ['ginf1',	'gstr1',	'gsea1',	'ginf2',	'gind1',	'gstr2',	'g3ei1',	'gsea2',	'gind2',	'g3ei2']
X = df[feature_cols] # Features
y = df.filiere # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test
# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
x_testing = [[0, 25	,75	,25	,25	,0	,0	,25,	75,	75
]]
y_test = clf.predict(x_testing)
print(y_test)

with open('model2.pkl', 'wb') as file:
    dill.dump(clf, file)
