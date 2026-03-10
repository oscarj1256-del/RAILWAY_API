from flask import Blueprint, render_template, request, redirect, url_for , jsonify
from app.controllers.cliente_controller import (
    get_all_clientes,
    get_client,
    create_cliente,
    update_client,
    delete_cliente
)

cliente_bp = Blueprint("clientes", __name__)

@cliente_bp.route("/" \
"", methods=["GET"])
def list_clients():
    # Llamamos al controlador para obtener todos los usuarios
    users = get_all_clientes()    
    # Retornamos la lista en formato JSON con código HTTP 200 (OK)
    return jsonify(users), 200


#  Obtener un usuario por ID
# Ruta: GET /api/users/<cliente_id>
@cliente_bp.route("/<int:cliente_id>", methods=["GET"])
def get_single_client(cliente_id):
    try:
        # Buscamos el usuario por ID
        user = get_client(cliente_id)
    except:
        return jsonify({"error": "El ID buscado no existe"}), 400    
    # Retornamos el usuario encontrado con código 200
    return jsonify(user), 200


#  Crear un nuevo usuario
# Ruta: POST /api/users
@cliente_bp.route("/", methods=["POST"])
def add_client():
    # Obtenemos los datos enviados en el body (JSON)
    data = request.get_json()
    # Validamos que existan datos y que venga el campo "name"
    if not data or "name" not in data:
        # Si no cumple la validación, retornamos error 400 (Bad Request)
        return jsonify({"error": "Nombre es obligatorio"}), 400
    # Llamamos al controlador para crear el usuario
    new_client = create_cliente(data)    
    # Retornamos el usuario creado con código 201 (Created)
    return jsonify(new_client), 201

#  Editar un usuario existente
# Ruta: PUT /api/users/<cliente_id>
@cliente_bp.route("/<int:cliente_id>", methods=["PUT"])
def edit_client(cliente_id):
    # Obtenemos los datos enviados en el body
    data = request.get_json()
    # Validamos que los datos no estén vacíos
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400
    # Llamamos al controlador para actualizar el usuario
    updated_client = update_client(cliente_id, data)
    
    # Retornamos el usuario actualizado con código 200 (OK)
    return jsonify(updated_client), 200


#   Eliminar un usuario
# Ruta: DELETE /api/users/<cliente_id>
@cliente_bp.route("/<int:cliente_id>", methods=["DELETE"])
def remove_client(cliente_id):
    # Llamamos al controlador para eliminar el usuario
    delete_cliente(cliente_id)
    
    # Retornamos código 204 (No Content)
    # 204 significa que la operación fue exitosa pero no hay contenido que devolver
    return "", 204

