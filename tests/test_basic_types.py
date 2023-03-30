from python_s2_protocol import Commodity, NumberRange, Duration
import pytest


@pytest.mark.parametrize(
    "commodity_name, expected_failiure",
    (["GAS", False],
     ["ELECTRICITY", False],
     ["NOTACOMMODITY", True])
)
def test_commodity(commodity_name, expected_failiure):
    if expected_failiure:
        with pytest.raises(Exception) as e_info:
            c1 = Commodity(commodity_name)

    else:
        c1 = Commodity(commodity_name)


@pytest.mark.parametrize(
    "duration, expected_failiure",
    ([10, False],
     [0.1, False], 
     ["NOTADURATION", True]) # 0.1 -> Duration(__root__=0) -> this float is rounded to int 
)
def test_duration(duration, expected_failiure):
    if expected_failiure:
        with pytest.raises(Exception) as e_info:
            d1 = Duration(__root__ = duration)
    else:
        d2 = Duration(__root__=duration)


def test_number_range():
    # right
    n1 = NumberRange(start_of_range=1, end_of_range=2)

    # wrong type
    with pytest.raises(Exception) as e_info:
        n2 = NumberRange(start_of_range="wrong type", end_of_range=1)
    
    # missing argument
    with pytest.raises(Exception) as e_info:
        n3 = NumberRange(end_of_range=1)

    # serialize
    n3 = NumberRange(start_of_range=1, end_of_range=2)
    n3_serialized = n3.dict()
    assert n3_serialized == dict(start_of_range=1, end_of_range=2)

    # deserialize
    n4 = '{"start_of_range" : 1, "end_of_range" : 2}'
    n4_deserialized = NumberRange.parse_raw(n4)
    assert n4_deserialized.start_of_range == 1
    assert n4_deserialized.end_of_range == 2