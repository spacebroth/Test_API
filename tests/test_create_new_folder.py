import pytest
import requests

from pages.api import DiskApi


@pytest.mark.parametrize('path', ['?path='])
class TestApiDisk(DiskApi):

    # def teardown(self):
    #     self.delete_file('?path=')

    def test_create_named_folder(self, path):
        try:
            status_code = self.create_named_folder(path).status_code
            self.delete_file(path)
            body = self.create_named_folder(path).json()
            assert ('name', 'API_Folder') in self.get_file_name(path), 'Папка не была создана'
            assert status_code == 201, 'Код ответа не соответствует ожидаемому'
            assert body == self.body, 'Тело ответа не соответствует требованиям'
        finally:
            self.delete_file('?path=')
