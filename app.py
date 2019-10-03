from flask import Flask, render_template
from Data import AlienLanguage
from log import setup_logging
from string import punctuation

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/translator/<statement>')
def translate(statement):
    # logger = setup_logging('/Users/Christopher/PycharmProjects/Care-Advisors-Test/translation_app')
    alien = AlienLanguage()

    if any(p in statement for p in punctuation):  # make sure no punctuation present in string
        string = "Invalid String"
    if statement.islower():  # make sure string is all lowercase
        dorbdorb = alien.english_to_dorbdorb(statement)
        gorbyoyo = alien.dorbdorb_to_gorbyoyo(dorbdorb)
        verified_gorbyoyo = alien.verify_translation(gorbyoyo)
        string = alien.contacenate(verified_gorbyoyo)
    else:
        string = "Invalid String"
    return render_template("translate.html", string=string)

if __name__=="__main__":
    app.run(debug=True)