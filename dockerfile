# Use a Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt file to the container
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code to the container

COPY códigobbdd.py ./
COPY df_bbdd.py ./
COPY df_esperanza_vida.py ./
COPY df_proximo_viaje.py ./
COPY df_tipos_viaje.py ./
COPY df_suma_puntos.py ./
COPY script.py ./

# Command to run the script when the container starts
ENTRYPOINT ["python","./df_bbdd.py","./df_espezanza_vida.py", "./df_proximo_viaje.py", "./df_tipos_viaje.py", "./script.py"]
