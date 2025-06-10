# Dummy service
def get_all_events():
    return [{"id": 1, "name": "Concert"}, {"id": 2, "name": "Fair"}]

def create_event(event):
    return {"id": 3, "name": event.name}
