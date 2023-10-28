import importlib.metadata

import test_py_cookie as m


def test_version():
    assert importlib.metadata.version("test_py_cookie") == m.__version__
