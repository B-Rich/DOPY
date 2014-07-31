import utils

class Key(object):

    def __init__(self, key_data, authentication_token):

        self.id = key_data["id"]
        self.fingerprint = key_data["fingerprint"]
        self.public_key = key_data["public_key"]
        self.name = key_data["name"]
        self.authentication_token = authentication_token 

    @classmethod
    def create_new(cls, key_and_name, authentication_token):

        create_key_response = utils.post_request("account/keys", key_and_name, authentication_token)
        if create_key_response.ok:

            return cls(create_key_response.json()["ssh_key"], authentication_token)

        else:

            raise Exception("Could not create ssh key! See error message: {0}".format(create_key_response.json()["message"]))

    @classmethod
    def from_existing(cls, key_id, authentication_token):

        get_key_response = utils.get_request("account/keys/{0}".format(key_id), authentication_token)
        if get_key_response.ok:

            return cls(get_key_response.json()["ssh_key"], authentication_token)

        else:

            raise Exception("Could not get ssh key information! See error message: {0}".format(get_key_response.json()["message"]))

    def change_name(self, new_name):

        new_name_dict = {"name": new_name}
        change_name_response = utils.put_request("account/keys/{0}".format(self.id), new_name_dict, self.authentication_token)

        if change_name_response.ok:

            self.name = new_name

        else:

            raise Exception("Request to change key name failed! See error message: {0}".format(change_name_response.json()["message"]))

    def destroy(self):

        destroy_key_response = utils.delete_request("account/keys/{0}".format(self.id), self.authentication_token)

        if not destroy_key_response.ok:

            raise Exception("Could not destroy ssh key! See error message: {0}".format(destroy_key_response.json()["message"]))
