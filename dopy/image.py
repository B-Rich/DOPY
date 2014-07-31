from action import Action
import utils

class Image(object):

    def __init__(self, image_data, authentication_token):

        self.id = image_data["id"]
        self.name = image_data["name"]
        self.distribution = image_data["distribution"]
        self.slug = image_data["slug"]
        self.public = image_data["public"]
        self.regions = image_data["regions"]
        self.created_at = image_data["created_at"]

    @classmethod
    def from_existing(cls, image_id, authentication_token):

        get_image_response = utils.get_request("images/{0}".format(image_id), authentication_token)

        if not get_image_response.ok:

            raise Exception("Could not retrieve specified Image! See error message: {0}".format(get_image_response.json()["message"]))

        return cls(get_image_response.json()["image"], authentication_token)

    def change_name(self, new_name):

        data = {"name": new_name}
        change_name_response = utils.put_request("images/{0}".format(self.id), data, self.authentication_token)

        if not change_name_response.ok:

            raise Exception("Request to change image name failed! See error message: {0}".format(change_name_response.json()["message"]))

        self.name = new_name

    def destroy(self):

        destroy_image_response = utils.delete_request("images/{0}".format(self.id), self.authentication_token)

        if not destroy_image_response.ok:

            raise Exception("Could not destroy image! See error message: {0}".format(destroy_image_response.json()["message"]))

    def transfer(self, new_region):

        data = {"type": "transfer", "region": new_region}
        transfer_region_response = utils.post_request("images/{0}/actions".format(self.id), data, self.authentication_token)

        if not transfer_region_response.ok:

            raise Exception("Failed to transfer region of image! See error message: {0}".format(transfer_region_response.json()["message"]))

        self.regions = [new_region]
        return Action(transfer_region_response.json()["action"])
    
    def get_action(self, action_id):

        get_action_response = utils.get_request("images/{0}/actions/{1}".format(self.id, action_id), self.authentication_token)

        if not response.ok:
    
            raise Exception("Failed to get action! See error message: {0}".format(response.json()["message"]))

        return Action(get_action_response.json()["action"])
