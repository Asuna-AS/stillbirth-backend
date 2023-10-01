import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
import json

app = Flask(__name__)
CORS(app, support_credentials=True)
normalFeatures = pickle.load(open('rf_model.pkl','rb'))
advancedFeatures = pickle.load(open('lr_model.pkl','rb'))

@app.route('/normalFeatures',methods=['POST'])
@cross_origin(supports_credentials=True)
def predict():
    data = request.get_json(force=True)
    int_features = [int(x) for x in data.values()]
    final_features = np.array(int_features)
    print(final_features)
    res = normalFeatures.predict([final_features])
    print("----------------------------")
    riski = normalFeatures.predict_proba([final_features])[0]
    print("----------------------------")
    ans = round(riski[1]*100, 2)
    print(ans)
    r = {"result" : float(ans) }
    response = jsonify(r)
    return response

@app.route('/advancedFeatures',methods=['POST'])
@cross_origin(supports_credentials=True)
def predict2():
    data = request.get_json(force=True)
    int_features = [float(x) for x in data.values()]
    final_features = np.array(int_features)
    print(final_features)
    res = advancedFeatures.predict([final_features])
    print("----------------------------")
    riski = advancedFeatures.predict_proba([final_features])[0]
    print("----------------------------")
    ans = round(riski[1]*100, 2)
    print(ans)
    r = {"result" : float(ans)}
    response = jsonify(r)
    return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)

