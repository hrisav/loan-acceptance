import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


df = pd.read_csv('loan_acceptance_data.csv')

df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Married'] = df['Married'].fillna(df['Married'].mode()[0])
df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].median())
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])
df['Credit_History'] = df['Credit_History'].astype(int)

df['Total_Income'] = df['ApplicantIncome'] + df['CoapplicantIncome']


dummies = pd.get_dummies(df['Gender'])
merged = pd.concat([df,dummies], axis = 'columns')
df = merged.drop(['Gender','Female'], axis = 'columns')

cols = ['Married','Dependents','Education','Self_Employed','Property_Area','Loan_Status']
le = LabelEncoder()
for i in cols:
    df[i] = le.fit_transform(df[i])


df=df.drop(['Loan_ID','ApplicantIncome','CoapplicantIncome'], axis = 1)

X = df.drop(['Loan_Status'], axis=1)
y = df['Loan_Status']

model = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=20)
model.fit(X_train, y_train)

file = open('loan_approval.pkl', 'wb')
pickle.dump(model, file)
