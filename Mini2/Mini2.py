
import logging
from fastapi import FastAPI
from datetime import datetime
import uvicorn
import pytz

with open("log/Mini2.log", "w") as file:
    file.write("Fecha de inicio del servidor: " + str(datetime.now()) + "\n")

logging.basicConfig(
    filename='log/Mini2.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)



logger = logging.getLogger(__name__)

app = FastAPI()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/")
def read_root():
    logger.info("Se ha accedido a la raíz del servidor")
    return {"message": "Hello, World!"}

@app.get("/time")
def get_time():
    chile_tz = pytz.timezone('America/Santiago')
    current_time = datetime.now(chile_tz).strftime("%H:%M:%S")
    logger.info(f"Se ha accedido a la hora actual de Chile: {current_time}")
    return {"La hora actual en Chile es": current_time}
