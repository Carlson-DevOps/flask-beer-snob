from flask import Flask
import random
from config import FULL_DESCRIPTIONS as desc

app = Flask(__name__)


@app.route('/')
def beer():
   return random.choice(desc)
   #return "Lovely... It's more fresh and floral than just bitter and hops!"

if __name__ == '__main__':
    app.run()
