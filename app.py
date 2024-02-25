from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

covid_model=pickle.load(open('covid.pkl','rb'))
diabetes_model=pickle.load(open('diabetes.pkl','rb'))
heart_model=pickle.load(open('heart.pkl','rb'))
cancer_model=pickle.load(open('cancer.pkl','rb'))
vector_model=pickle.load(open('vector.pkl','rb'))


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("aboutUs.html")

@app.route("/cancer")
def cancer():
    return render_template("cancer.html")

@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")


@app.route("/covid")
def covid():
    return render_template("covid.html")

@app.route("/vector")
def vector():
    return render_template("vector.html")


@app.route('/heartpred',methods=['POST'])
def heartpred():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=heart_model.predict(final)

    if prediction==1:
        return render_template('heart.html',ans="We regret to inform you that you have been diagnosed with heart disease..")
    else:
        return render_template('heart.html',ans="Great news! You have no signs of heart disease")


@app.route('/diabetespred',methods=['POST'])
def diabetespred():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction_prob = diabetes_model.predict_proba(final)[:, 1]  
    threshold = 0.5
    if prediction_prob > threshold:
        return render_template('diabetes.html', ans="We regret to inform you that you have been diagnosed with diabetes disease.")
    else:
        return render_template('diabetes.html', ans="Great news! You have no signs of diabetes disease.")

@app.route('/covidpred',methods=['POST'])
def covidpred():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=covid_model.predict(final)

    if prediction==1:
        return render_template('covid.html',ans="We regret to inform you that you have been diagnosed with covid disease.")
    else:
        return render_template('covid.html',ans="Great news! You have no signs of covid disease.")

@app.route('/cancerpred',methods=['POST'])
def cancerpred():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction_prob = cancer_model.predict_proba(final)[:, 1]  
    threshold = 0.5
    if prediction_prob > threshold:
        return render_template('cancer.html', ans="We regret to inform you that you have been diagnosed with cancer disease.")
    else:
        return render_template('cancer.html', ans="Great news! You have no signs of cancer disease.")



@app.route('/vectorpred', methods=['POST'])
def vectorpred():
    int_features = [float(x) for x in request.form.values()]
    final = [np.array(int_features)]
    prediction_prob = vector_model.predict_proba(final)

    
    predicted_class_index = prediction_prob.argmax()

    
    class_labels = ["Chikungunya", "Dengue", "Rift Valley fever", "Yellow Fever", "Zika", "Malaria", "Japanese encephalitis", "West Nile fever", "Plague", "Tungiasis", "Lyme disease"]

    
    predicted_class = class_labels[predicted_class_index]

    return render_template('vector.html', ans=f"We regret to inform you that you have been diagnosed with {predicted_class} disease.")


if __name__=='__main__':
   app.run(debug=True)