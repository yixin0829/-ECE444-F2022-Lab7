from flask import Flask, request
from flask_restful import Resource, Api

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)
api = Api(application)

# Class for holding the model
class FakeNewsModel(Resource):
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
        pred = self.model.predict(self.vectorizer.transform([text]))[0]
        return 0 if pred == "REAL" else 1

class MlService(Resource):
    def post(self):
        return {'hello': 'world'}

api.add_resource(MlService, '/')

if __name__ == '__main__':
    application.run(debug=True)

