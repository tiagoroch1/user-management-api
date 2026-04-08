from flask import Blueprint, request, jsonify
from database.db import db
from models.usuario import Usuario
import uuid

usuario_bp = Blueprint('usuario', __name__)

# GET
@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()

    lista = []
    for u in usuarios:
        lista.append({
            "id": u.id,
            "nome": u.nome,
            "email": u.email
        })

    return jsonify(lista), 200


# POST
@usuario_bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json

    if not data or not data.get("nome") or not data.get("email"):
        return jsonify({"erro": "Nome e email são obrigatórios"}), 400

    usuario = Usuario(
        id=str(uuid.uuid4()),
        nome=data.get("nome"),
        email=data.get("email")
    )

    db.session.add(usuario)
    db.session.commit()

    return jsonify({
        "mensagem": "Usuário criado!",
        "usuario": {
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email
        }
    }), 201


# PUT
@usuario_bp.route('/usuarios/<string:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    data = request.json

    usuario.nome = data.get("nome", usuario.nome)
    usuario.email = data.get("email", usuario.email)

    db.session.commit()

    return jsonify({"mensagem": "Usuário atualizado"})


# DELETE
@usuario_bp.route('/usuarios/<string:id>', methods=['DELETE'])
def deletar_usuario(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({"mensagem": "Usuário deletado"})