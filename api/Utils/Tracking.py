import uuid

#generates tracking numbers

def generate_tracking_number():
    return str(uuid.uuid4()).split("-")[0].upper()