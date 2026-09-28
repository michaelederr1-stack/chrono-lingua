import pytest
from src.parser import ChronoParser

def test_parser_initialization():
    parser = ChronoParser()
    assert parser.default_encoding == "utf-8"

def test_transform_uppercase():
    parser = ChronoParser()
    res = parser.transform("hello", mode="uppercase")
    assert res["transformed"] == "HELLO"
    assert res["mode"] == "uppercase"

def test_transform_reverse():
    parser = ChronoParser()
    res = parser.transform("chrono", mode="reverse")
    assert res["transformed"] == "onorhc"

def test_transform_token_map():
    parser = ChronoParser()
    res = parser.transform("test core", mode="token_map")
    assert res["transformed"] == "tok(test).tok(core)"

def test_empty_input():
    parser = ChronoParser()
    res = parser.transform("", mode="standard")
    assert res["transformed"] == ""
    assert res["length"] == 0
