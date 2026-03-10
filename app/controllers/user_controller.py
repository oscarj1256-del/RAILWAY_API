from app.models.user import User
from app import db 

#  Obtener todos
def get_users():
    users = User.query.all()
    return [user.to_dict() for user in users]

# Obtener uno por ID
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return user.to_dict()

#  Crear
def create_user(data):
    new_user = User(name=data["name"])
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()

#  Editar
def update_user(user_id, data):
    user = User.query.get_or_404(user_id)
    user.name = data.get("name", user.name)
    db.session.commit()
    return user.to_dict()

#   Eliminar
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return {"message": "Usuario eliminado correctamente"}
