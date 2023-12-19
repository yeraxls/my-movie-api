
# Crear entorno virtual

python -m venv venv

# Activar entorno virtual
venv/Scripts/activate

# Correr api
uvicorn main:app --reload


# Correr api con reload y puerto concreto
uvicorn main:app --reload --port 5000


# Correr api con reload y puerto concreto disponible para todos los dispositivos de la red
uvicorn main:app --reload --port 5000 --host 0.0.0.0


pip install sqlalchemy