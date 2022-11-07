import pytest
from pages.api import DiskApi


@pytest.mark.parametrize('path', ['?path='])
class TestApiDisk(DiskApi):
    def test_create_named_folder(self, path):
        try:
            res = self.create_named_folder(path)
            assert ('name', 'API_Folder') in self.get_file_name(path), 'Папка не была создана'
            assert res.status_code == 201, 'Код ответа не соответствует ожидаемому'
            assert res.json() == self.body, 'Тело ответа не соответствует требованиям'
        finally:
            self.delete_file('?path=')
