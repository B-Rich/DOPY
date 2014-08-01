from action import Action
import utils

class Droplet(object):

    def __init__(self, droplet_data, authentication_token):

        self.id = droplet_data["id"]
        self.name = droplet_data["name"]
        self.region = droplet_data["region"]
        self.image = droplet_data["image"]
        self.kernel = droplet_data["kernel"]
        self.size = droplet_data["size"]
        self.created_at = droplet_data["created_at"]
        self.networks = droplet_data["networks"]
        self.features = droplet_data["features"]
        self.authentication_token = authentication_token

    @classmethod
    def create_new(cls, data, authentication_token):

        create_droplet_response = utils.post_request("droplets", data, authentication_token)
        if not create_droplet_response.ok:

            raise Exception("Droplet Not Successfully Created! Message Returned {0}".format(create_droplet_response.json()["message"]))

        return cls(create_droplet_response.json()["droplet"], authentication_token)


    @classmethod
    def from_existing(cls, droplet_id, authentication_token):

        droplet = utils.get_request("droplets/{0}".format(droplet_id), authentication_token)
        if not droplet.ok: 
    
            raise Exception("Droplet not Created as Could Retrieve Data of Existing Node! Message Returned: {0}".format(droplet.json()["message"]))

        return cls(droplet.json()["droplet"], authentication_token)

    def delete(self):

        response = utils.delete_request("droplets/{0}".format(self.id), self.authentication_token)
        if not response.ok:

            raise Exception("Failed to Delete Droplet! Message Returned: {0}".response.json()["message"])

    def _execute_droplet_action(self, data):

        request_response = utils.post_request("droplets/{0}/actions".format(self.id), data, self.authentication_token)

        if not request_response.ok:

            raise Exception("Failed on attempt to {0}! See error message: {1}".format(data["type"], request_response.json()["message"]))

        return request_response

    def change_kernel(self, kernel_id):

        data = {"type": "change_kernel", "kernel": kernel_id}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def enable_IPv6(self):

        data = {"type": "enable_ipv6"}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def enable_private_networking(self):

        data = {"type": "enable_private_networking"}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def disable_backups(self):

        data = {"type": "disable_backups"}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def power_cycle(self):

        data = {"type": "power_cycle"}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def password_reset(self):

        data = {"type": "password_reset"}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def power_off(self):

        data = {"type": "power_off"}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def power_on(self):

        data = {"type": "power_on"}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def reboot(self):

        data = {"type": "reboot"}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def rebuild(self, image_id):

        data = {"type": "rebuild", "image": image_id}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def rename(self, name):

        data = {"type": "rename", "name": name}
        response = self._execute_droplet_action(data)
        self.name = name
        return Action(response.json()["action"])

    def resize(self, size_id):

        data = {"type": "resize", "size": size_id}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def restore(self, image_id):

        data = {"type": "restore", "image": image_id}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def shutdown(self):

        data = {"type": "shutdown"}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def take_snapshot(self, name):

        data = {"type": "snapshot", "name": name}
        response = self._execute_droplet_action(data)
        return Action(response.json()["action"])

    def get_action(self, action_id):

        get_action_response = utils.get_request("droplets/{0}/actions/{1}".format(self.id, action_id), self.authentication_token)

        if not response.ok:
    
            raise Exception("Failed to get action! See error message: {0}".format(response.json()["message"]))

        return Action(response.json()["action"])

    def _get_data(self, type_of_data):

        response = utils.get_request("droplets/{0}/{1}".format(self.id, type_of_data), self.authentication_token)
        return response.json()

    def get_actions(self):

        actions = self._get_data("actions").json()["actions"]
        return [Action(action) for action in actions]

    def get_kernels(self):

        return self._get_data("kernels")

    def get_snapshots(self):

        return self._get_data("snapshots")

    def get_backups(self):

        return self._get_data("backups")
