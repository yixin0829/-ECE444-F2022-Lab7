from flask import Flask, request, json, jsonify

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)

# Class for holding the model
class FakeNewsModel(object):
    model = None # where we will keep the model when it's loaded
    vectorizer = None

    @classmethod
    def load_model(self):
        with open('./models/basic_classifier.pkl', 'rb') as fid:
            self.model = pickle.load(fid)

        with open('./models/count_vectorizer.pkl', 'rb') as vd:
            self.vectorizer = pickle.load(vd)

    @classmethod
    def predict(self, text:str):
        """Take a string text as input and call fake news dector model. Return 0 or 1 based on whether it's fake news (1) or not (0)"""
        self.load_model()

        pred = self.model.predict(self.vectorizer.transform([text]))[0]
        return 0 if pred == "REAL" else 1

@application.route('/ping', methods=['GET'])
def hello():
    return "Welcome to your fake news detector tool."

@application.route('/predict', methods=['GET'])
def predict():
    """ Predict whether the payload data is a fake news (1) or not (0)"""
    text = request.args.get('text')

    if text is None:
        resp = jsonify({'error': 'No input text specified to predict result.'})
        resp.status_code = 400
        return resp
    
    # Do the prediction
    pred = FakeNewsModel.predict(text)
    result = {
        "status_code": 200,
        "pred": pred
    }

    return result


if __name__ == '__main__':
    application.run(debug=True)

