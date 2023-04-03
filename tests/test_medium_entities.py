from python_s2_protocol.FRBC.schemas import FRBCOperationModeElement

example_operation_mode_element = """
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




if __name__ == '__main__':
    operation_mode_element = FRBCOperationModeElement.parse_raw(example_operation_mode_element)
    print(operation_mode_element)



# import pytest

# def f(commodity_name, expected_failiure):
    
#     if expected_failiure:
#         with pytest.raises(Exception) as e_info:
#             c1 = Commodity(commodity_name)

#     else:
#         c1 = Commodity(commodity_name)