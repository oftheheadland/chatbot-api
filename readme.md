# Chatbot API

API for my my discord bot, [Jamie-Bot](https://discordbotlist.com/bots/494325818605043724), to use. But others are welcome to use it.
Uses [Chatterbot](https://pypi.org/project/ChatterBot/) to return intelligent responses to your input - and learns as it goes.

## Example 

Example GET Request

```python
import requests
from urllib.parse import quote

query = 'insert your text here'
url = "https://jamie-chatter.herokuapp.com/chatter/" + quote(query)

response = requests.request("GET", url)

print(response.text)
```

## Getting Started

- Clone the repo
- pip install -r requirements.txt 
- flask run

## Authors

* **Andrew VanNess** - [oftheheadland](https://github.com/oftheheadland)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
