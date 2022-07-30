import requests
import pytest


class DiskApi:
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               'Authorization': 'OAuth AQAAAABT9VeCAADLW0bQ9vKZJ0F-gPZd_iNluYc'}
    file_name = 'API_Folder'
    resources_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    body = {'href': 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2FAPI_Folder', 'method': 'GET',
            'templated': False}

    def create_named_folder(self, path: str):
        return requests.put(f'{self.resources_url}{path}{self.file_name}', headers=self.headers)

    def delete_file(self, path: str):
        return requests.delete(f'{self.resources_url}{path}{self.file_name}', headers=self.headers)

    def get_file_name(self, path: str):
        res = requests.get(f'{self.resources_url}{path}{self.file_name}', headers=self.headers).json()
        return res.items()
