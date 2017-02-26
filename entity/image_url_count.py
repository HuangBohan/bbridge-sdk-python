import json


class ImageURLCount(object):
    def __init__(self, image_urls, count):
        """
        :type image_urls: list of str
        :type count: int
        """
        self.__image_urls = image_urls
        self.__count = count

    @property
    def image_urls(self):
        return self.__image_urls

    @property
    def count(self):
        return self.__count

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :return: entity.image_url_count.ImageURLCount
        """
        return ImageURLCount(json_object["image_urls"], json_object["count"])

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :return: entity.image_url_count.ImageURLCount
        """
        return ImageURLCount.from_json(json.loads(json_string))