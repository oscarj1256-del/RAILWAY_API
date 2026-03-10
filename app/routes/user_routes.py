# Importamos herramientas necesarias de Flask:
# - Blueprint: para modularizar las rutas
# - request: para obtener datos enviados en la petición
# - jsonify: para devolver respuestas en formato JSON
from flask import Blueprint, request, jsonify

# Importamos las funciones del controlador (lógica del negocio)
# Estas funciones interactúan con la base de datos
from app.controllers.user_controller import (
    get_users,
    get_user,
    create_user,
    update_user,
    delete_user
)

# Creamos un Blueprint llamado "users"
# __name__ ayuda a Flask a ubicar correctamente el módulo
user_bp = Blueprint("users", __name__)


# 🔍 Obtener todos los usuarios
# Ruta: GET /api/users
@user_bp.route("/", methods=["GET"])
def list_users():
    # Llamamos al controlador para obtener todos los usuarios
    users = get_users()
    
    # Retornamos la lista en formato JSON con código HTTP 200 (OK)
    return jsonify(users), 200


#  Obtener un usuario por ID
# Ruta: GET /api/users/<user_id>
@user_bp.route("/<int:user_id>", methods=["GET"])
def get_single_user(user_id):

    try:
        # Buscamos el usuario por ID
        user = get_user(user_id)
    except:
        return jsonify({"error": "El ID buscado no existe"}), 400
    
    # Retornamos el usuario encontrado con código 200
    return jsonify(user), 200


#  Crear un nuevo usuario
# Ruta: POST /api/users
@user_bp.route("/", methods=["POST"])
def add_user():
    # Obtenemos los datos enviados en el body (JSON)
    data = request.get_json()

    # Validamos que existan datos y que venga el campo "name"
    if not data or "name" not in data:
        # Si no cumple la validación, retornamos error 400 (Bad Request)
        return jsonify({"error": "Nombre es obligatorio"}), 400

    # Llamamos al controlador para crear el usuario
    new_user = create_user(data)
    
    # Retornamos el usuario creado con código 201 (Created)
    return jsonify(new_user), 201


#  Editar un usuario existente
# Ruta: PUT /api/users/<user_id>
@user_bp.route("/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    # Obtenemos los datos enviados en el body
    data = request.get_json()

    # Validamos que los datos no estén vacíos
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    # Llamamos al controlador para actualizar el usuario
    updated_user = update_user(user_id, data)
    
    # Retornamos el usuario actualizado con código 200 (OK)
    return jsonify(updated_user), 200


#   Eliminar un usuario
# Ruta: DELETE /api/users/<user_id>
@user_bp.route("/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    # Llamamos al controlador para eliminar el usuario
    delete_user(user_id)
    
    # Retornamos código 204 (No Content)
    # 204 significa que la operación fue exitosa pero no hay contenido que devolver
    return "", 204

