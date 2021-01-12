from flask import Flask, request, url_for, redirect, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
            text_to_translate = request.form["text-to-translate"].lower()
            selected_language = request.form["select-language"]
            translated_text = translator.translate(
                text_to_translate, dest=selected_language)
            text = translated_text.text
         
           return render_template('index.html', translation_result=text)
    return render_template("index.html")


@app.route("/team")
def team():
    return render_template("team.html")


if __name__ == "__main__":
