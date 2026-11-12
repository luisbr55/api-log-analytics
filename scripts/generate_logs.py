import csv
import random
import uuid
from datetime import datetime, timedelta, timezone

NUM_ROWS = 10_000

# TODO 1: define una lista de endpoints (por ejemplo "/api/users", "/api/orders"...)
ENDPOINTS = []

# TODO 2: define los métodos HTTP posibles
METHODS = []


def generate_row():
    # TODO 3: genera un request_id único (pista: uuid.uuid4())
    # TODO 4: genera un timestamp aleatorio dentro de los últimos 7 días
    # TODO 5: elige un endpoint y un método al azar
    # TODO 6: elige un status_code (¿todos con la misma probabilidad?)
    # TODO 7: genera un response_time_ms (¿debería ser igual para todos los endpoints?)
    # TODO 8: genera un client_id
    pass


def main():
    # TODO 9: abre data/logs.csv con csv.DictWriter, escribe el encabezado
    #         y luego NUM_ROWS filas llamando a generate_row()
    pass


if __name__ == "__main__":
    main()