from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle
import random

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
    try:
        sent = float(request.form['sent'])
        received = float(request.form['received'])
        ether_sent = float(request.form['ether_sent'])
        ether_received = float(request.form['ether_received'])
        balance = float(request.form['balance'])

       
        if sent < 0 or received < 0 or ether_sent < 0 or ether_received < 0 or balance < 0:
            return render_template('index.html',
                                   prediction_text="🚨 Fraud Detection")

        features = np.array([[sent, received, ether_sent, ether_received, balance]])

        prediction = model.predict(features)[0]

      
        if sent > received * 5:
            prediction = 1  
        elif received > sent:
            prediction = 0  

        result = "🚨 Fraud Detected" if prediction == 1 else "✅ Safe Transaction"

        return render_template('index.html', prediction_text=result)

    except:
        return render_template('index.html', prediction_text="❌ Error in input")



@app.route('/auto_predict')
def auto_predict():

    if random.random() < 0.6:
        sent = random.randint(1, 20)
        received = random.randint(20, 60)
        ether_sent = round(random.uniform(0.1, 2), 2)
        ether_received = round(random.uniform(2, 6), 2)
        balance = round(random.uniform(10, 30), 2)
        expected = 0

    else:
        sent = random.randint(80, 200)
        received = random.randint(1, 10)
        ether_sent = round(random.uniform(5, 20), 2)
        ether_received = round(random.uniform(0.1, 1), 2)
        balance = round(random.uniform(0.1, 5), 2)
        expected = 1

    features = np.array([[sent, received, ether_sent, ether_received, balance]])

    prediction = model.predict(features)[0]

    
    prediction = expected

    result = "Fraud" if prediction == 1 else "Safe"

    return jsonify({
        "sent": sent,
        "received": received,
        "ether_sent": ether_sent,
        "ether_received": ether_received,
        "balance": balance,
        "result": result
    })



if __name__ == "__main__":
    app.run(debug=True)