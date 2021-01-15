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
    textFile = request.args.get('text')
    line = request.args.get('line', default=0, type=int)
    print(request.args.get('line'))

    with open("texts/bovary.txt", "r", encoding="utf-8") as f:
     text = ""
     for l in f.readlines()[line:line+50]:
          text = text + l

    doc = nlp(text)
    
    locations = []

    annotations = "<p>"
    for token in doc:
        if token.ent_type_ == "LOC":
            annotations = annotations + ' ' + '<span class="loc">' + token.text + '</span>'
            locations.append(token.text)
        elif token.text == "," or token.text == "." or token.text == ";":
            annotations = annotations + token.text 
        elif token.text == "—":
            annotations = annotations + '<br>' + token.text 
        else:
            annotations = annotations + ' ' + token.text 
    annotations = annotations + "</p>"

    data = {}
    data['locations'] = locations
    data['text'] =  annotations
    json_data = json.dumps(data)

    return json_data

@app.route('/get-locations')
def getLocations():
    textFile = request.args.get('text')

    # text = []
    # with open("texts/bovary.txt", "r", encoding="utf-8") as f:
    #     text = f.readlines()

    text = open("texts/bovary.txt", 'r', encoding="utf-8").read()

    doc = nlp(text)
    
    locations = []

    for ent in doc.ents:
        if ent.label_ == "LOC":
            if ent.text not in locations:
                locations.append(ent.text)

    return jsonify(locations)

if __name__ == "__main__":
    app.run()