from app import db  # Importamos la instancia de SQLAlchemy

# Definimos el modelo User que representa la tabla "users" en la base de datos
class Cliente(db.Model):

    __tablename__ = "clientes"  # Nombre explícito de la tabla en la base de datos

    # Columna id:
    # - Tipo entero
    # - Es la clave primaria
    # - Se autoincrementa automáticamente
    id = db.Column(db.Integer, primary_key=True)

    # Columna name:
    # - Tipo string con máximo 100 caracteres
    # - No puede ser nulo (campo obligatorio)
    name = db.Column(db.String(100), nullable=False)

    # Método personalizado para convertir el objeto User en un diccionario
    # Esto es útil para retornar datos en formato JSON en una API REST
    def to_dict(self):
        return {
            "id": self.id,      # Devuelve el id del usuario
            "name": self.name   # Devuelve el nombre del usuario
        }
