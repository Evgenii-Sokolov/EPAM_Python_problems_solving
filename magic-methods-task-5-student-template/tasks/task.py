import os
import shutil
import tempfile
from pathlib import Path

class TempDir:
    def __enter__(self):
        self.prev_dir = os.getcwd()
        self.new_dir = tempfile.mkdtemp()
        os.chdir(self.new_dir)
        return self.new_dir

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.prev_dir)
        shutil.rmtree(self.new_dir)

class MockedOSFuncs:
    def __init__(self):
        self._directories = set()

    def os_mkdir_mocked(self, path: str, mode=511, *, dir_fd=None):
        """
        Mocked os.mkdir
        """
        directory = Path(path).resolve().absolute()
        if directory in self._directories:
            raise FileExistsError(f'File exists: \'{directory}\'')
        elif directory.parent not in self._directories:
            raise FileNotFoundError(f'No such file or directory: \'{directory.parent}\'')
        self._directories.add(directory)

    def os_rmdir_mocked(self, path):
        directory = Path(path).resolve().absolute()
        if directory not in self._directories:
            raise FileNotFoundError(f'No such file or directory: \'{directory}\'')
        self._directories.remove(directory)

def mocked_os_decorator():
    mocked_os = MockedOSFuncs()

    return pytest.mark.parametrize(
        'mocked_os',
        [mocked_os],
        indirect=True
    )

@pytest.mark.parametrize(
    'test_dir, expected_existed_directories',
    [
        ('/', {'/'}),
        ('/home', {'/', '/home'}),
        ('/home/user', {'/', '/home', '/home/user'}),
        ('/home/user/Documents', {'/', '/home', '/home/user', '/home/user/Documents'}),
        ('/etc', {'/', '/etc'}),
        ('/root/some_dir', {'/', '/root', '/root/some_dir'}),
        ('/root/.local/lib/python', {'/', '/root', '/root/.local', '/root/.local/lib', '/root/.local/lib/python'}),
    ]
)
@mocked_os_decorator()
def test_tempdir(test_dir, expected_existed_directories, mocked_os):
    os.chdir(test_dir)
    initial_dir = os.getcwd()

    assert initial_dir == test_dir
    assert mocked_os._directories == set()

    with TempDir():
        assert os.getcwd() != initial_dir
        assert mocked_os._directories == expected_existed_directories
