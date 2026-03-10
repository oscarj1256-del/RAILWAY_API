import os


def get_database_uri():
    """Obtiene la URI de la base de datos, compatible con Railway PostgreSQL."""
    uri = os.environ.get("DATABASE_URL", "sqlite:///database.db")
    # Railway usa postgres:// pero SQLAlchemy requiere postgresql://
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    return uri


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret")
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
