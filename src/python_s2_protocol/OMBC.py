# generated by datamodel-codegen:
#   filename:  s2-cem.yaml
#   timestamp: 2023-03-30T21:07:36+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from . import ID, NumberRange, PowerRange


class OperationMode(BaseModel):
    class Config:
        extra = Extra.forbid

    id: ID = Field(
        ...,
        description='ID of the OBMC.OperationMode. Must be unique in the scope of the Resource Manager, for at least the duration of the session between Resource Manager and CEM.',
    )
    diagnostic_label: Optional[str] = Field(
        None,
        description='Human readable name/description of the OMBC.OperationMode. This element is only intended for diagnostic purposes and not for HMI applications.',
    )
    power_ranges: List[PowerRange] = Field(
        ...,
        description='The power produced or consumed by this operation mode. The start of each PowerRange is associated with an operation_mode_factor of 0, the end is associated with an operation_mode_factor of 1. In the array there must be at least one PowerRange, and at most one PowerRange per CommodityQuantity.',
        max_items=10,
        min_items=1,
    )
    running_costs: Optional[NumberRange] = Field(
        None,
        description='Additional costs per second (e.g. wear, services) associated with this operation mode in the currency defined by the ResourceManagerDetails , excluding the commodity cost. The range is expressing uncertainty and is not linked to the operation_mode_factor.',
    )
    abnormal_condition_only: bool = Field(
        ...,
        description='Indicates if this OMBC.OperationMode may only be used during an abnormal condition.',
    )