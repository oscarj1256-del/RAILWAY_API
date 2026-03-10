from app.models.cliente import Cliente
from app import db

def get_all_clientes():
    clientes = Cliente.query.all()
    return [user.to_dict() for user in clientes]

# Obtener uno por ID
def get_client(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    return cliente.to_dict()

#  Crear
def create_cliente(data):
    new_cliente = Cliente(name=data["name"])
    db.session.add(new_cliente)
    db.session.commit()
    return new_cliente.to_dict()

#  Editar
def update_client(user_id, data):
    cliente = Cliente.query.get_or_404(user_id)
    cliente.name = data.get("name", cliente.name)
    db.session.commit()
    return cliente.to_dict()

#   Eliminar
def delete_cliente (cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    return {"message": "Cliente eliminado correctamente"}

