from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
import json

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

    doc = nlp(text)
    
    locations = []

    annotations = "<p>"
    for token in doc:
        if token.ent_type_ == "LOC":
            annotations = annotations + '<span class="loc">' + token.text + '</span>'+ ' '
            locations.append(token.text)
        else:
            annotations = annotations + token.text + ' '
    annotations = annotations + "</p>"

    # for ent in doc.ents:
    #     if ent.label_ == "LOC":
    #         if ent.text not in locations:
    #             locations.append(ent.text)

    data = {}
    data['locations'] = locations
    data['text'] =  annotations
    json_data = json.dumps(data)

    return json_data


if __name__ == "__main__":
    app.run()