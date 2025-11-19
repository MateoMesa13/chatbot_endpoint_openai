from flask import Flask
from flasgger import Swagger
from .agents.main_agent import MainAgent
from .utils.sessions import Sessions

app = Flask(__name__)
main_agent = MainAgent()
main_agent.create_agent()
sessions = Sessions()
swagger = Swagger(app)

from app.routes import health, chat