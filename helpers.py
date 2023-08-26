import json
from pathlib import Path

sessions_file = 'data/sessions.json'
game_types_file = 'data/game_types.json'

def saveJSONToFile(json_file,json_obj):
    Path(json_file).write_text(json.dumps(json_obj))
    return True

def loadJSONFromFile(json_file):
    return json.loads(Path(json_file).read_text())

def getNewId(mylist):
    """ Get unused or new id """
    ids = []

    if len(mylist) == 0:
        return 1

    # Get all used ids
    for e in mylist:
        ids.append(e['id'])

    # Put them in order so we can get the last
    # one later if needed
    ids.sort()

    # Get list of missing ids within range of list
    missing_ids = [ele for ele in range(1,max(ids) + 1) if ele not in ids]

    # If there are missing ids, get the first one missing
    # else get the last used id and increase by 1
    if len(missing_ids) > 0:
        this_id = missing_ids[0]
    else:
        this_id = ids[-1] + 1

    return this_id

