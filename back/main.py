from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
import json
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os

nlp = spacy.load("fr_core_news_lg")

app = Flask(__name__)
cors = CORS(app)
#execute in out the return folder back
#directory = './back/texts'
# execute in the return folder back
directory = './texts'
app.config['UPLOAD_FOLDER'] =directory

@app.route('/')
def index():
    return "hello world"

@app.route('/get-annotated-text')
def getAnnotatedText():
    textFile = request.args.get('text')
    line = request.args.get('line', default=0, type=int)
    print(request.args.get('line'))

    with open("texts/"+textFile+".txt", "r", encoding="utf-8") as f:
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

    doc = nlp(text) #100 000 premiers caractères à la place de tout le texte
    
    locations = []

    for ent in doc.ents:
        if ent.label_ == "LOC":
            if ent.text not in locations:
                locations.append(ent.text)

    return jsonify(locations)
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():  
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'fichier téléchargé avec succès'


@app.route('/getList')
def liste():
    list_of_files = {}
    liste=[]
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        name=filename.rsplit('.', 1)[0].lower()
        print(name)
        filess=app.config['UPLOAD_FOLDER']
        filles=filess.rsplit('/', 1)[1].lower()
        
        list_of_files["value"] = filles+'/'+filename
        list_of_files["text"] = name
        print(list_of_files)
        liste.append(list_of_files.copy())
    json_data = json.dumps(liste)
    return json_data

@app.route('/delete')
def deletefiles():
    files = request.args.get('filles')
    if os.path.exists(files):
        os.remove(files)
        return 'fichier supprimé avec succès'
    else:
        return "Le fichier n'existe pas"

@app.route('/listeChamp')
def listeCh():
    filename= "texts/bovary.txt"
    string_to_search="I\n"
    line_number = 0
    list_of_results = []

    filehandle = open(filename, 'r',)
    with open("texts/bovary.txt", "r", encoding="utf-8") as f:
        text = ""
        for l in f.readlines()[0:1]:
            text = text + l
    with open(filename, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if string_to_search in line:
                list_of_results.append((line_number, line.rstrip()))
    
        
    data = {}
    data['titre'] = text
    data['chapitre '] =  list_of_results
    json_data = json.dumps(data)
    return json_data

if __name__ == "__main__":
    app.run()