import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask, render_template
from config import Config
from api_usuarios.database.db import db
from api_usuarios.routes.usuario_routes import usuario_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# REGISTRA ROTAS
app.register_blueprint(usuario_bp)

# ROTA DA INTERFACE (SÓ UMA!)
@app.route('/')
def home():
    return render_template('index.html')

# CRIA BANCO
with app.app_context():
    db.create_all()

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)