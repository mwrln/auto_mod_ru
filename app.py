from flask import Flask, request, jsonify

import joblib
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import string
import argparse


DEFAULT_CONFIG = {
    "endpoint": "score",
    "text_field": "text",
    "model_path": "models/log_reg.joblib",
    "vectorizer_path": "models/tfidf_vect.joblib"
}


def preprocess(text):
    return ''.join(c if c not in string.punctuation else f' {c} ' for c in text.lower() )


def get_config(path):
    with open(path, 'r') as f:
        return json.load(f)


app = Flask(__name__)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', help='path to custom config', type=str, required=False)
    args = parser.parse_args()
    DEFAULT_CONFIG = DEFAULT_CONFIG if not args.config_path else get_config(args.config_path)

    @app.get(f"/{DEFAULT_CONFIG['endpoint']}")
    def get_score():
        text = request.args.get(DEFAULT_CONFIG['text_field'])
        text_vec = vect.transform([preprocess(text)])
        return jsonify({
            DEFAULT_CONFIG['text_field']: text,
            "is_toxic": float(clf.predict_proba(text_vec)[:,1])
        })

    clf = joblib.load(DEFAULT_CONFIG['model_path'])
    vect = joblib.load(DEFAULT_CONFIG['vectorizer_path'])
    app.run(debug=True, host='0.0.0.0')
