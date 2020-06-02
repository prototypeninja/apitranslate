from flask import Flask, render_template, url_for, request
from mtranslate import translate
app = Flask(__name__)
@app.route('/')
def meteo():
    text = request.args.get('text')
    to_translate = text
    return translate(to_translate, 'fr')
if __name__ == "__main__":
    app.run()