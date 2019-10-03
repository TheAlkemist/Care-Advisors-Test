from flask import Flask,render_template
from Data import AlienLanguage
from log import setup_logging

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("translation.html")

@app.route('/translator/<statement>')
def translate(statement):
    logger = setup_logging('/Users/Christopher/PycharmProjects/Care-Advisors-Test/translation_app')
    alien = AlienLanguage(logger)
    if statement.islower():
        dorbdorb = alien.english_to_dorbdorb(statement)
        gorbyoyo = alien.dorbdorb_to_gorbyoyo(dorbdorb)
        verified_gorbyoyo = alien.verify_translation(gorbyoyo)
        string = alien.contacenate(verified_gorbyoyo)
    else:
        return "Invalid String"
    return string

if __name__=="__main__":
    app.run(debug=True)