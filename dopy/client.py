from domain import Domain
from droplet import Droplet
from image import Image
from key import Key
from region import Region
from size import Size
import utils

class Client(object):

    def __init__(self, authentication_token):

        self.authentication_token = authentication_token 

    def _get_list_of_data(self, class_of_data, name_of_data):

        response = utils.get_request(name_of_data, self.authentication_token)

        if not response.ok:

            raise Exception("Error when retrieving list of {0}! See error message: {1}".format(name_of_data, response.json()["message"]))

        return [class_of_data(data_object, self.authentication_token) for data_object in response.json()[name_of_data]]

    def get_droplets(self):

        return self._get_list_of_data(Droplet, "droplets")

    def create_droplet(self, name, region="sfo1", size="512mb", image=3448641):

        data = {"name": name, "region": region, "size": size, "image": image}
        return Droplet.create_new(data, self.authentication_token)

    def get_droplet(self, droplet_id):

        return Droplet.from_existing(droplet_id, self.authentication_token)

    def get_images(self):

        return self._get_list_of_data(Image, "images")

    def get_image(self, image_id):

        return Image.from_existing(image_id, self.authentication_token)
    
    def get_keys(self):

        get_keys_response = utils.get_request("account/keys", self.authentication_token)
        if not get_keys_response.ok:

            raise Exception("Could not get ssh keys! See error message: {0}".format(get_keys_response.json()["message"]))

        return [Key(key_data, self.authentication_token) for key_data in get_keys_response.json()["ssh_keys"]]

    def create_key(self, key, name):

        data = {"name": name, "public_key": key}
        return Key.create_new(data, self.authentication_token)

    def get_key(self, key_id):

        return Key.from_existing(key_id, self.authentication_token)

    def get_regions(self):

        get_regions_response = utils.get_request("regions", self.authentication_token)
        if not get_regions_response.ok:

            raise Exception("Could not get regions! See error message: {0}".format(get_regions_response.json()["message"]))

        return [Region(region_data) for region_data in get_regions_response.json()["regions"]]

    def get_sizes(self):

        get_sizes_response = utils.get_request("sizes", self.authentication_token)
        if not get_sizes_response.ok:

            raise Exception("Could not get sizes! See error message: {0}".format(get_sizes_response.json()["message"]))

        return [Size(size_data) for size_data in get_sizes_response.json()["sizes"]]

    def create_domain(self, name, ip_address):

        return Domain.create_new(name, ip_address, self.authentication_token)

    def get_domain(self, domain_name, authentication_token):

        return Domain.from_existing(domain_name, authentication_token)

    def get_domains(self):

        get_domains_response = utils.get_request("domains", self.authentication_token)
        if not get_domains_response.ok:

            raise Exception("Could not get domains! See error message: {0}".format(get_domains_response.json()["message"]))

        return [Domain(domain_data) for domain_data in get_domains_response.json()["domains"]]
