from flask import Flask
from flask_cors import CORS
from app.routes import api
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)