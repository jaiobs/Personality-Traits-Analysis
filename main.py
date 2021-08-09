from flask import Flask, request, jsonify, send_from_directory
from lstm_personalitytraits import traits
from model_traits import model_personalitytraits

app = Flask(__name__)



@app.route('/personality', methods=['POST'])
def personality():
    txt = request.form['text']
    df = traits()
    output = model_personalitytraits(df, txt)
    return jsonify({"The personality Trait is ": output})

if __name__ == "__main__":
    app.run(port=5009)


