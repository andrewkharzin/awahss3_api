import strawberry
from typing import List, Any, Optional
from .type import SHCType
from asgiref.sync import sync_to_async
from strawberry_django_optimizer import optimized_django_field
from apps.directory.aviastates.shc.models import SHC  # Replace 'your_app' with the actual name of your Django app

@strawberry.type
class Query:
    shcodes: List[SHCType] = optimized_django_field()


    # @strawberry.field(description="Fetch a list of impcodes.")
    # async def resolve_impcodes(
    #     self,
    #     code: Optional[str] = None,
    #     page: int = 1,
    #     perPage: int = 10
    # ) -> List[SHCType]:
    #     try:
    #         # Wrap the database query inside sync_to_async
    #         queryset = await sync_to_async(SHC.objects.all)()

    #         if code:
    #             queryset = await sync_to_async(queryset.filter)(code=code)

    #         start = (page - 1) * perPage
    #         end = start + perPage

    #         # Fetch the paginated list of aircrafts asynchronously
    #         codes_records = await sync_to_async(list)(queryset[start:end].values())

    #         # Convert the aircraft records to AircraftType objects
    #         impcodes = [SHCType(
    #             code=SHCType(
    #                 code=record['code']
    #             ),
    #             code=record['code'],

    #         ) for record in codes_records]

    #         return impcodes
    #     except SHC.DoesNotExist:
    #         return []
