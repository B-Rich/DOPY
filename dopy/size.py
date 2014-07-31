class Size(object):

    def __init__(self, data):

        self.slug = data["slug"]
        self.memory = data["memory"]
        self.vcpus = data["vcpus"]
        self.disk = data["disk"]
        self.transfer = data["transfer"]
        self.price_monthly = data["price_monthly"]
        self.price_hourly = data["price_hourly"]
        self.regions = data["regions"]
