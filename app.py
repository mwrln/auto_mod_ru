from flask import Flask, request, jsonify

import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import string


def preprocess(text):
    return ''.join(c if c not in string.punctuation else f' {c} ' for c in text.lower() )


app = Flask(__name__)


@app.get("/score")
def get_score():
    text = request.args.get("text")
    text_vec = vect.transform([preprocess(text)])
    return jsonify({
        "text": text,
        "is_toxic": float(clf.predict_proba(text_vec)[:,1])
    })


if __name__ == '__main__':
    clf = joblib.load("logreg_clf.joblib")
    vect = joblib.load("count_vect.joblib")
    app.run(debug=True, host='0.0.0.0')
