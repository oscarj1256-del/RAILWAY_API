from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
 
    # Método personalizado para convertir el objeto User en un diccionario
    # Esto es útil para retornar datos en formato JSON en una API REST
    def to_dict(self):
        return {
            "id": self.id,      # Devuelve el id del usuario
            "name": self.name   # Devuelve el nombre del usuario
        }
