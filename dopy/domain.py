import utils

class Domain(object):

        def __init__(self, data, authentication_token):

            self.name = data["name"]
            self.ttl = data["ttl"]
            self.zone_file = data["zone_file"]
            self.authentication_token = authentication_token

        @classmethod
        def create_new(cls, name, ip_address, authentication_token):

            data = {"name": name, "ip_address": ip_address}
            create_domain_response = utils.post_request("domains", data, authentication_token)
            if not create_domain_response.ok:

                raise Exception("Domain not successfully created! See error message: {0}".format(create_domain_response.json()["message"]))

            return cls(create_domain_response.json()["domain"], authentication_token)

        @classmethod
        def from_existing(cls, domain_name, authentication_token):

            get_domain_response = utils.get_request("domains/{0}".format(domain_name), authentication_token)
            if not get_domain_response.ok:

                raise Exception("Failed to retrieve data for domain! See error message: {0}".format(get_domain_response.json()["message"]))

            return cls(get_domain_response.json()["domain"], authentication_token)

        def delete(self):

            delete_domain_response = utils.delete_request("domains/{0}".format(self.name), self.authentication_token)
            if not delete_domain_response.ok:

                raise Exception("Failed to delete domain! See error message: {0}".format(delete_domain_response.json()["message"]))
