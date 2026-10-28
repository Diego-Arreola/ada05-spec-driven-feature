import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

def load_customers() -> list[dict]:
    """
    Carga y retorna la lista de clientes desde data.json.
    """
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    
    