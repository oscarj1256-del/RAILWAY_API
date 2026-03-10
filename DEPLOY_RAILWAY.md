# Desplegar API en Railway

## Proyecto: API_Railway

Tu proyecto Flask está listo para desplegarse en Railway.

---

## Pasos para desplegar desde GitHub

### 1. Sube tu código a GitHub

Si aún no has subido el repositorio:

```bash
git init
git add .
git commit -m "Preparado para Railway"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main
```

### 2. Crea el proyecto en Railway

1. Entra a [railway.app](https://railway.app) e inicia sesión.
2. Haz clic en **"New Project"**.
3. Selecciona **"Deploy from GitHub repo"**.
4. Conecta tu cuenta de GitHub si no lo has hecho.
5. Elige el repositorio de tu API Flask.
6. **Nombra el proyecto: `API_Railway`** (en la configuración del proyecto o servicio).

### 3. Configuración automática

Railway detectará automáticamente:

- **Python** por `requirements.txt`
- **Comando de inicio** por el `Procfile`: `gunicorn --bind 0.0.0.0:$PORT run:app`

### 4. Genera el dominio público

1. En tu servicio, ve a la pestaña **Settings**.
2. En la sección **Networking**, haz clic en **Generate Domain**.
3. Te asignarán una URL como `tu-api.up.railway.app`.

### 5. Variables de entorno (opcional)

En **Variables** del servicio puedes añadir:

| Variable | Descripción |
|----------|-------------|
| `SECRET_KEY` | Clave secreta para Flask (recomendado en producción) |
| `DATABASE_URL` | Si añades PostgreSQL en Railway, se configura sola |

### 6. Base de datos PostgreSQL (opcional)

Para producción, es mejor usar PostgreSQL en lugar de SQLite:

1. En tu proyecto Railway, clic en **+ New**.
2. Elige **Database** → **PostgreSQL**.
3. Railway creará `DATABASE_URL` automáticamente.
4. Conecta la variable al servicio de tu API.
5. Haz un nuevo despliegue.

---

## Tu API estará disponible en:

- **Usuarios**: `https://tu-dominio.up.railway.app/api/users`
- **Clientes**: `https://tu-dominio.up.railway.app/api/clientes`

---

## Archivos de despliegue incluidos

- `Procfile` – Comando de inicio para Railway
- `railway.json` – Configuración de build y deploy
- `requirements.txt` – Incluye `gunicorn` para producción
- `config.py` – Usa `DATABASE_URL` y `SECRET_KEY` de variables de entorno
