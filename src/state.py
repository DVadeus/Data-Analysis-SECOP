import json
import os

STATE_FILE = "data/metadata/state.json"

def load_state():
    # Si no existe el archivo
    if not os.path.exists(STATE_FILE):
        return {"fecha_de_inicio_del_contrato": "2024-12-31T23:59:59"}

    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent = 4)