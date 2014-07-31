class Region(object):

    def __init__(self, data):

        self.slug = data["slug"]
        self.name = data["name"]
        self.sizes = data["sizes"]
        self.available = data["available"]
        self.features = data["features"]
