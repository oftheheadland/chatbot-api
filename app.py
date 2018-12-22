from flask import Flask
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

app = Flask(__name__)
chatterbot = ChatBot("Jamie",
                     storage_adapter="chatterbot.storage.SQLStorageAdapter",
                     read_only=False,
                     database_uri=os.environ['DATABASE_URL']
                     )


# To train with default english corpus

# chatterbot.set_trainer(ChatterBotCorpusTrainer)

# chatterbot.train(
#     "chatterbot.corpus.english"
# )

###

@app.route('/chatter/<phrase>', methods=['GET'])
def note_page(phrase):
    try:
        response = str((chatterbot.get_response(phrase)))
        return(response)
    except:
        return("error getting response")


if __name__ == '__main__':
    app.run(debug=True)
