# generated by datamodel-codegen:
#   filename:  s2-cem.yaml
#   timestamp: 2023-03-30T21:07:36+00:00

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel, Extra, Field

from . import ID, CommodityQuantity, Duration, NumberRange


class PowerEnvelopeElement(BaseModel):
    class Config:
        extra = Extra.forbid

    duration: Duration = Field(..., description='The duration of the element')
    upper_limit: float = Field(
        ...,
        description='Upper power limit according to the commodity_quantity of the containing PEBC.PowerEnvelope. The lower_limit must be smaller or equal to the upper_limit. The Resource Manager is requested to keep the power values for the given commodity quantity equal to or below the upper_limit. The upper_limit shall be in accordance with the constraints provided by the Resource Manager through any PEBC.AllowedLimitRange with limit_type UPPER_LIMIT.',
    )
    lower_limit: float = Field(
        ...,
        description='Lower power limit according to the commodity_quantity of the containing PEBC.PowerEnvelope. The lower_limit must be smaller or equal to the upper_limit. The Resource Manager is requested to keep the power values for the given commodity quantity equal to or above the lower_limit. The lower_limit shall be in accordance with the constraints provided by the Resource Manager through any PEBC.AllowedLimitRange with limit_type LOWER_LIMIT.',
    )


class PowerEnvelopeLimitType(Enum):
    UPPER_LIMIT = 'UPPER_LIMIT'
    LOWER_LIMIT = 'LOWER_LIMIT'


class PowerEnvelopeConsequenceType(Enum):
    VANISH = 'VANISH'
    DEFER = 'DEFER'


class AllowedLimitRange(BaseModel):
    class Config:
        extra = Extra.forbid

    commodity_quantity: CommodityQuantity = Field(
        ..., description='Type of power quantity this PEBC.AllowedLimitRange applies to'
    )
    limit_type: PowerEnvelopeLimitType = Field(
        ...,
        description='Indicates if this ranges applies to the upper limit or the lower limit',
    )
    range_boundary: NumberRange = Field(
        ...,
        description='Boundaries of the power range of this PEBC.AllowedLimitRange. The CEM is allowed to choose values within this range for the power envelope for the limit as described in limit_type. The start of the range shall be smaller or equal than the end of the range. ',
    )
    abnormal_condition_only: bool = Field(
        ...,
        description='Indicates if this PEBC.AllowedLimitRange may only be used during an abnormal condition',
    )


class PowerEnvelope(BaseModel):
    class Config:
        extra = Extra.forbid

    id: ID = Field(
        ...,
        description='Identifier of this PEBC.PowerEnvelope. Must be unique in the scope of the Resource Manager, for at least the duration of the session between Resource Manager and CEM.',
    )
    commodity_quantity: CommodityQuantity = Field(
        ..., description='Type of power quantity this PEBC.PowerEnvelope applies to'
    )
    power_envelope_elements: List[PowerEnvelopeElement] = Field(
        ...,
        description='The elements of this PEBC.PowerEnvelope. Shall contain at least one element. Elements must be placed in chronological order.',
        max_items=288,
        min_items=1,
    )