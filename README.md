# Microblog API

Una aplicación simple de microblog construida con Django y Django REST Framework.

## Requisitos previos

- Python 3.8 o superior
- Git
- PostgreSQL 12 o superior

## Configuración de la base de datos

1. Crea el esquema en PostgreSQL:
   ```sql
   CREATE SCHEMA IF NOT EXISTS api_microblog_db;
   ```

2. Asegúrate de que el usuario tenga permisos en el esquema:
   ```sql
   GRANT ALL PRIVILEGES ON SCHEMA api_microblog_db TO postgres;
   ```

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd microblog
   ```

2. Crea un entorno virtual:

   ```bash
   python -m venv env
   ```

3. Activa el entorno virtual:

   - En Windows:
     ```bash
     env\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta las migraciones de la base de datos:

   ```bash
   python manage.py migrate
   ```

6. Ejecuta el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

   El servidor estará disponible en `http://127.0.0.1:8000/`.

## Uso

La API proporciona endpoints para gestionar posts en el microblog. Puedes usar herramientas como Postman o el archivo `rest_test/posts.http` para probar los endpoints.

### Endpoints principales

- `GET /api/posts/` - Lista todos los posts
- `POST /api/posts/` - Crea un nuevo post

