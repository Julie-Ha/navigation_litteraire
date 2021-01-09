from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy

nlp = spacy.load("fr_core_news_lg")

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return "hello world"

@app.route('/get-annotated-text')
def getAnnotatedText():
    text = request.args.get('text')

    with open("texts/bovary.txt", "r", encoding="utf-8") as f:
     text = ""
     for line in f.readlines()[50:100]:
          text = text + line

    print(text)

    doc = nlp(text)
    
    locations = []

    for ent in doc.ents:
        if ent.label_ == "LOC":
            if ent.text not in locations:
                locations.append(ent.text)

    return jsonify(locations)


if __name__ == "__main__":
    app.run()