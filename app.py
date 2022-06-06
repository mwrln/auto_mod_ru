from flask import Flask, request, jsonify

import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import string


DEFAULT_CONFIG = {
    "endpoint": "score",
    "text_field": "text",
    "model_path": "models/log_reg.joblib",
    "vectorizer_path": "models/tfidf_vect.joblib"
}


def preprocess(text):
    return ''.join(c if c not in string.punctuation else f' {c} ' for c in text.lower() )


app = Flask(__name__)


if __name__ == '__main__':

    @app.get(f"/{DEFAULT_CONFIG['endpoint']}")
    def get_score():
        text = request.args.get("text")
        text_vec = vect.transform([preprocess(text)])
        return jsonify({
            "text": text,
            "is_toxic": float(clf.predict_proba(text_vec)[:,1])
        })

    clf = joblib.load(DEFAULT_CONFIG['model_path'])
    vect = joblib.load(DEFAULT_CONFIG['vectorizer_path'])
    app.run(debug=True, host='0.0.0.0')
