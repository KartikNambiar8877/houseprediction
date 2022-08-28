from logging import exception
import pickle
import numpy as np
from flask import Flask,render_template,request
app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['GET','POST'])
def predict():
    try:
        
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features) 
        output=np.round(prediction[0],2)
        return render_template('index.html',prediction_text='Total house price predicted is {}'.format(output))
    except:
        return render_template('index.html',prediction_text='Please add a valid input')

if __name__=='__main__':
    app.run(debug=True)    