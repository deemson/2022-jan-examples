import pytest

from e06frozendict.frozendict import FrozenDict


def test_basic_functionality():
    d = FrozenDict({"key1": 1, "key2": 2})
    assert d["key1"] == 1
    assert d["key2"] == 2
    assert len(d) == 2
    assert {"key1", "key2"} == set(d)


def test_hash():
    d1 = FrozenDict({"key1": 1, "key2": 2})
    d2 = FrozenDict({"key1": 1, "key2": 2})
    assert hash(d1) == hash(d2)
    dict_with_frozen_dict_key = {d1: "value"}
    assert dict_with_frozen_dict_key[d2] == "value"


def test_cannot_modify():
    d = FrozenDict({"key": "value"})
    with pytest.raises(TypeError) as exc_info:
        d["other key"] = "other value"
    assert str(exc_info.value) == "'FrozenDict' object does not support item assignment"
