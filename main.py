from flask import Flask,render_template,request
import pickle
import numpy as np
import json,CONFIG




with open(CONFIG.MODEL_PATH,'rb') as file:
    model=pickle.load(file)
with open(CONFIG.ASSET_PATH,'r')as file:
    asset=json.load(file)
col= asset['columns']
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/get_data", methods=["POST","GET"])
def data():
    input_data = request.form
    print(input_data)

    data=np.zeros(len(col))

    #SepalLengthCm=data['html_sepal_length']
    #SepalWidthCm=data['html_sepal_width']
    #PetalLengthCm=data['html_petal_length']
    #PetalWidthCm=data['html_petal_width']

    data[0] = input_data['sepal_length']
    data[1] = input_data['sepal_width']
    data[2] = input_data['petal_length']
    data[3] = input_data['petal_width']

    
    result=model.predict([data])
    print(result)
    if result[0] ==0:
        iris_value = "SETOSA"
    if result[0] ==1:
        iris_value = "VERSICOLOR"
    if result[0] ==2:
        iris_value = "VIRGINICA"
    return str(iris_value)


if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5000)


