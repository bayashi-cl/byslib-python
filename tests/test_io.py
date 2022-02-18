from io import StringIO

from byslib.core import sinput, int1


def test_sinput_string(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("string\r\n"))
    assert sinput() == "string"


def test_sinput_integer(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("5"))
    assert int(sinput()) == 5


def test_sinput_int1(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("5"))
    assert int1(sinput()) == 4
