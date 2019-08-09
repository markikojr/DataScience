import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#CREATING AN INSTANCE OF THE FLASK CLASS
app = Flask(__name__)

#LOADING THE MODEL
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

#DECORATOR (WHERE THE URL IS '/predict', AND HANDLE POST REQUESTS)
@app.route('/predict',methods=['POST'])
def predict():
    '''
    Function for rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

#DECORATOR (WHERE THE URL IS '/predict_api', AND HANDLE POST REQUESTS)
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    Function for direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)