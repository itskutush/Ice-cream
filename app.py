import pickle
import numpy as np
from flask import Flask,render_template,request

app = Flask(__name__)
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app.static_folder = 'static'
#url
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def predict():
    temperature_str = request.form.get('temperature')
    temperature = float(temperature_str)
    temperatur_array = np.array([[temperature]])
    prediction = model.predict(temperatur_array)
    output = round(prediction[0],2)
    print(output)
    return render_template('index.html',prediction_text=f'Total revenue generated is Rs.{output}/-')

if __name__ == '__main__':
    app.run(debug=True)
