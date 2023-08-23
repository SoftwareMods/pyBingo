import json
from pathlib import Path

sessions_file = 'data/sessions.json'

def saveJSONToFile(json_file,json_obj):
    Path(json_file).write_text(json.dumps(json_obj))
    return True

def loadJSONFromFile(json_file):
    return json.loads(Path(json_file).read_text())
