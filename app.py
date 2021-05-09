from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('loan_approval.pkl', 'rb'))  # opening pickle file in read mode

app = Flask(__name__)  # initializing Flask app


@app.route("/",methods=['GET'])
def hello():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        d1 = request.form['Married']
        if d1 == 'No':
            d1 = 0
        else:
            d1 = 1
        d2 = request.form['Gender']
        if (d2 == 'Male'):
            d2 = 1
        else:
            d2 = 0
        d3 = request.form['Education']
        if (d3 == 'Graduate'):
            d3 = 0
        else:
            d3 = 1
        d4 = request.form['Self_Employed']
        if (d4 == 'No'):
            d4 = 0
        else:
            d4 = 1
        d5 = request.form['ApplicantIncome']
        d6 = request.form['CoapplicantIncome']
        d7 = d5 + d6
        d8 = request.form['LoanAmount']
        d9 = request.form['Loan_Amount_Term']
        d10 = request.form['Credit_History']
        if (d10 == 'All debts paid'):
            d10 = 1
        else:
            d10 = 0
        d11 = request.form['Property_Area']
        if (d11 == 'Urban'):
            d11 = 2
        elif (d11 == 'Rural'):
            d11 = 0
        else:
            d11 = 1
        d12 = request.form['Dependents']
        if (d12 == '3+'):
            d12 = 3
        else:
            d12 = d12
        arr = np.array([[d1, d12, d3, d4, d8, d9, d10, d11, d7, d2]])
        pred = model.predict(arr)
        if pred == 0:
            return render_template('index.html', prediction_text="Sorry! You are not eligible for Loan.")
        else:
            return render_template('index.html', prediction_text="Congrats! You are eligible for Loan.")
    else:
        return render_template('index.html')


#app.run(host="0.0.0.0")            # deploy
app.run(debug=True)                # run on local system
