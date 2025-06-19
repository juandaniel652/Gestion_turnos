import uuid

def generar_id_turno () :
    
    return str(uuid.uuid4())[:8]  # ID corto y único
