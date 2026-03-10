from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()   # Crea las tablas en la base de datos si no existen
    # ORM (Object Relational Mapping): Permite interactuar con la base de datos usando objetos en lugar de escribir SQL directamente.

if __name__ == "__main__":
    app.run(debug=True)
