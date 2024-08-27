
import logging
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from datetime import datetime, timedelta
import pytz

app = FastAPI()
chile_tz = pytz.timezone('America/Santiago')
# Crear archivo de log y vaciarlo en cada inicializacion
with open("log/Mini1.log", "w") as file:
    file.write("Fecha de inicio del servidor Mini1: " + str(datetime.now(chile_tz)) + "\n")


# Configuracion de logging
logging.basicConfig(
    filename='log/Mini1.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# Desactivar logging de watchfiles
logging.getLogger('watchfiles').setLevel(logging.WARNING)
# Crear logger
logger = logging.getLogger(__name__)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Variables globales
access_counter = 0
reset_time = datetime.now(chile_tz).replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)



@app.get("/")
def read_root():

    global access_counter, reset_time
    # Chequea si ya paso un dia
    if datetime.now(chile_tz) >= reset_time:
        access_counter = 0
        reset_time = datetime.now(chile_tz).replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        logger.info("Se ha reiniciado el contador de ingresos")

    # Incrementa el contador
    access_counter += 1
    logger.info(f"Ingresos totales hoy: {access_counter}")
    return {"Se ha ingresado a la pagina": f"{access_counter} veces hoy"}

