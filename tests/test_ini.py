from config import config_from_ini, config_from_dict
import tempfile

INI = """
[section1]
key1 = True

[section2]
key1 = abc
key2 = def
key3 = 1.1

[section3]
key1 = 1
key2 = 0
"""

DICT = {
    "section1.key1": True,
    "section2.key1": "abc",
    "section2.key2": "def",
    "section2.key3": 1.1,
    "section3.key1": 1,
    "section3.key2": 0,
}


def test_load_ini():  # type: ignore
    cfg = config_from_ini(INI)
    assert cfg == config_from_dict(dict((k, str(v)) for k, v in DICT.items()))


def test_load_ini_file():  # type: ignore
    with tempfile.NamedTemporaryFile() as f:
        f.file.write(INI.encode())
        f.file.flush()
        cfg = config_from_ini(open(f.name, 'rt'), read_from_file=True)

    assert cfg == config_from_dict(dict((k, str(v)) for k, v in DICT.items()))


def test_load_ini_filename():  # type: ignore
    with tempfile.NamedTemporaryFile() as f:
        f.file.write(INI.encode())
        f.file.flush()
        cfg = config_from_ini(f.name, read_from_file=True)

    assert cfg == config_from_dict(dict((k, str(v)) for k, v in DICT.items()))
