class Action(object):

    def __init__(self, data):

        self.id = data["id"]
        self.status = data["status"]
        self.type = data["type"]
        self.started_at = data["started_at"]
        self.completed_at = data["completed_at"]
        self.resource_id = data["resource_id"]
        self.resource_type = data["resource_type"]
        self.region = data["region"]
