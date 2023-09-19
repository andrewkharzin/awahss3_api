import strawberry
from typing import List, Any, Optional, Union
from .type import BaseDGType, SubDivisionType, DangerousGoodType
from asgiref.sync import sync_to_async
from strawberry_django_optimizer import optimized_django_field
# Replace 'your_app' with the actual name of your Django app
from apps.directory.aviastates.dgr.models import BaseDG, SubDivision, DangerousGood


@strawberry.type
class Query:
    dg_classes: List[BaseDGType] = optimized_django_field()
    # dg_classes: BaseDGType
    get_subdivision: List[SubDivisionType] = optimized_django_field()
    get_dangerous_good: List[DangerousGoodType] = optimized_django_field()

    @strawberry.field
    async def resolve_dg_classes(self, info) -> List[BaseDGType]:
        base_dgs = await sync_to_async(BaseDG.objects.all)()
        return [BaseDGType(hazard_class=base_dg.hazard_class) for base_dg in base_dgs]

  
        

    # @strawberry.field
    # async def get_dangerous_good(self, info) -> Union[DangerousGoodType, None]:
    #     dangerous_good = await sync_to_async(DangerousGood.objects.first)()
    #     if dangerous_good:
    #         return DangerousGoodType(
    #             UN_number=dangerous_good.UN_number,
    #             proper_shipping_name=dangerous_good.proper_shipping_name,
    #             hazard_class=dangerous_good.hazard_class,
    #             packing_group=dangerous_good.packing_group,
    #             subsidiary_risk=dangerous_good.subsidiary_risk,
    #             packing_instructions=dangerous_good.packing_instructions,
    #             special_provisions=dangerous_good.special_provisions,
    #             packaging_instructions=dangerous_good.packaging_instructions,
    #             additional_information=dangerous_good.additional_information,
    #             label=dangerous_good.label
    #         )
    #     else:
    #         return None
