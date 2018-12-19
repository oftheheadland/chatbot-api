from flask import Flask

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
chatterbot = ChatBot("Jamie", read_only=False)

@app.route('/chatter/<phrase>', methods=['GET'])
def note_page(phrase):
    response = str((chatterbot.get_response(phrase)))
    return(response)

if __name__ == '__main__':
    app.run(debug=True)
