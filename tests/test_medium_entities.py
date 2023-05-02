import json

import pytest
from pydantic.error_wrappers import ValidationError

from python_s2_protocol.FRBC.schemas import FRBCOperationModeElement

operation_mode_element_raw = """
    {
        "fill_level_range": {
            "start_of_range": 0.1,
            "end_of_range": 0.1
        },
        "fill_rate":  {
            "start_of_range": 0,
            "end_of_range": 0.1
        },
        "power_ranges": [
            {
                "start_of_range": 5725,
                "end_of_range": 5725,
                "commodity_quantity": "ELECTRIC.POWER.L1"
            }
        ],
        "running_costs": {
            "start_of_range": 0,
            "end_of_range": 0
        }
    }
"""


@pytest.fixture
def operation_mode_element_dict():
    return json.loads(operation_mode_element_raw)


def test_parse_raw():
    operation_mode_element = FRBCOperationModeElement.parse_raw(
        operation_mode_element_raw
    )
    print(operation_mode_element)


def test_change_inner(operation_mode_element_dict):
    operation_mode_element = FRBCOperationModeElement(**operation_mode_element_dict)

    # right inner type
    operation_mode_element.fill_level_range = {"start_of_range": 1, "end_of_range": 1}

    # wrong end type
    with pytest.raises(ValidationError) as e_info:
        operation_mode_element.fill_level_range = {
            "start_of_range": "wrongtype",
            "end_of_range": 1,
        }

    # wrong inner type
    with pytest.raises(ValidationError) as e_info:
        operation_mode_element.fill_level_range = [1, 2]
