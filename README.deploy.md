# 🚀 Despliegue en Render – Proyecto `beauty_shop`

Este archivo documenta los pasos necesarios para desplegar tu tienda online Django en [Render](https://render.com) sin usar Docker.

---

## 🌐 1. Prepara tu repositorio

Asegúrate de tener estos archivos en tu repositorio (ya están en tu caso):

- `requirements.txt`
- `Procfile`
- `.env.example` (Render lo usará como guía)
- `config/wsgi.py`
- `config/settings/production.py`

---

## ⚙️ 2. Crear el servicio en Render

1. Ve a [https://render.com](https://render.com) y crea una cuenta o inicia sesión.
2. Clic en **"New +" > Web Service**
3. Elige tu repositorio: `Yeison23Rodriguez09/beauty_shop`
4. Completa así:

| Opción                  | Valor                                                        |
|-------------------------|--------------------------------------------------------------|
| Name                    | `beauty-shop` o el nombre que desees                         |
| Runtime Environment     | Python                                                       |
| Build Command           | `pip install -r requirements.txt`                            |
| Start Command           | `gunicorn config.wsgi:application`                           |
| Environment             | `Python 3`                                                   |
| Region                  | La más cercana a tus clientes                                |
| Branch                  | `main`                                                       |
| Environment Variables   | Define desde la interfaz (ver abajo)                         |

---

## 🔐 3. Variables de entorno (`.env`)

Agrega en Render > Environment:

```env
DJANGO_ENV=production
DJANGO_ALLOWED_HOSTS=beauty-shop.onrender.com
SECRET_KEY=tu_clave_secreta
POSTGRES_DB=nombre_db
POSTGRES_USER=usuario_db
POSTGRES_PASSWORD=contraseña_db
POSTGRES_HOST=hostname_render_postgres
POSTGRES_PORT=5432

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=contraseña_app
DEFAULT_FROM_EMAIL=tu_email@gmail.com

CORS_ALLOWED_ORIGINS=https://beauty-shop.onrender.com
