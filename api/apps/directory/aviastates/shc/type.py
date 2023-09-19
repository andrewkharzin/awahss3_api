import strawberry
from apps.directory.aviastates.shc.models import SHC


@strawberry.django.type(SHC)
class SHCType:
    category: str
    code: str
    description: str
