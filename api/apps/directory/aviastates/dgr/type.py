import strawberry
from asgiref.sync import sync_to_async
from typing import List, Any, Optional
from django.templatetags.static import static
from django.conf import settings
from apps.directory.aviastates.dgr.models import BaseDG, SubDivision, DangerousGood


@strawberry.django.type(BaseDG)
class BaseDGType:
    hazard_class: str
    reason_regulation: str
    description: str
    label: strawberry.Private[str]

    @strawberry.field
    async def resolved_label(self, info) -> str:
        return await resolve_label(self, info)


@sync_to_async
def resolve_label(parent, info):
    if parent.label:
        return parent.label.url if settings.DEBUG else parent.label.url.lstrip(settings.STATIC_URL)
    return ""


@strawberry.django.type(SubDivision)
class SubDivisionType:
    subdivision_number: Optional[str] = None,
    description: Optional[str] = None,
    label: Optional[str] = None,
    base_dg: BaseDGType

    @strawberry.field
    async def resolved_label(self, info) -> str:
        return await resolve_label(self, info)


@sync_to_async
def resolve_label(parent, info):
    if parent.label:
        return parent.label.url if settings.DEBUG else parent.label.url.lstrip(settings.STATIC_URL)
    return ""


@strawberry.django.type(DangerousGood)
class DangerousGoodType:
    UN_number: str
    proper_shipping_name: str
    hazard_class: str
    packing_group: str
    subsidiary_risk: str
    packing_instructions: str
    special_provisions: str
    packaging_instructions: str
    additional_information: str
    subdivisions: List[SubDivisionType]

    async def resolve_subdivisions(self, info) -> List[SubDivisionType]:
        return await sync_to_async(list)(self.subdivisions.all())

    async def resolve_resolved_label(self, info) -> str:
        return await resolve_label(self, info)
