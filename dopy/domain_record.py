import utils

class DomainRecord(object):

    def __init__(self, data, authentication_token):

        self.id = data["id"]
        self.type = data["type"]
        self.name = data["name"]
        self.data = data["data"]
        self.priority = data["priority"]
        self.port = data["port"]
        self.weight = data["weight"]
        self.domain_name = data["domain_name"]

    @classmethod
    def create_new(cls, domain_name, data, authentication_token):

        create_domain_record_response = utils.post_request("domains/{0}/records".format(domain_name), data, authentication_token)
        if not create_domain_record_response.ok:

            raise Exception("Failed to create domain record! See error message: {0}".format(create_domain_record_response.json()["message"]))

        domain_record = create_domain_record_response.json()["domain_record"]
        domain_record["domain_name"]  = domain_name
        return cls(domain_record, authentication_token)

    @classmethod
    def from_existing(cls, domain_name, record_id, authentication_token):

        get_domain_record_response = utils.get_request("domains/{0}/records/{1}".format(domain_name, record_id), authentication_token)
        if not get_domain_record_response.ok:

            raise Exception("Failed to get domain record! See error message: {0}".format(get_domain_record_response.json()["message"]))

        domain_record = get_domain_record_response.json()["domain_record"]
        domain_record["domain_name"]  = domain_name
        return cls(domain_record, authentication_token)

    def delete(self):

        delete_domain_record_response = utils.delete_request("domains/{0}/records/{1}".format(self.domain_name, self.id), self.authentication_token)
        if not delete_domain_record_response.ok:

            raise Exception("Failed to delete domain record! See error message: {0}".format(delete_domain_record_response.json()["message"]))

    def change_name(self, new_name):

        data = {"name": new_name}
        change_name_response = utils.put_request("domains/{0}/records/{1}".format(self.domain_name, self.id))
        if not change_name_response.ok:

            raise Exception("Failed to change name of domain record! See error message: {0}".format(change_name_response.json()["message"]))

        self.name = new_name
