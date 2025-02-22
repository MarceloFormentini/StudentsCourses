from flask import Flask
from src.main.routes.event import event_route_bp

app = Flask(__name__)

# registrando o agregador no servidor
app.register_blueprint(event_route_bp)