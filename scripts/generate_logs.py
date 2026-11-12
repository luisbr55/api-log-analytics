import csv
import random
import uuid
from datetime import datetime, timedelta, timezone

NUM_ROWS = 10_000


ENDPOINTS = ["/api/users", "/api/orders", "/api/products", "/api/login", "/api/admin"]


METHODS = ["GET", "POST", "PUT","DELETE"]


def generate_row():
    
    request_id = str(uuid.uuid4())[:12]
    
    ahora = datetime.now()
    hace_7_dias = ahora - timedelta(days=7)

    inicio = int(hace_7_dias.timestamp())
    fin = int(ahora.timestamp())

    ts_aleatorio = random.randint(inicio,fin)
    timestamp = datetime.fromtimestamp(ts_aleatorio, tz= timezone.utc).isoformat()

   
    # TODO 5: elige un endpoint y un método al azar
    random_endpoint = random.choice(ENDPOINTS)
    random_method = random.choice(METHODS)


    # TODO 6: elige un status_code (¿todos con la misma probabilidad?)
    # TODO 7: genera un response_time_ms (¿debería ser igual para todos los endpoints?)
    # TODO 8: genera un client_id
    return {"request_id": request_id,
            "timestamp": timestamp,
            "endpoint": random_endpoint,
            "method": random_method
            }


def main():
    print(generate_row())
    print(generate_row())
    pass


if __name__ == "__main__":
    main()