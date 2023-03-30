import graphene
from graphene_django import DjangoObjectType
from apps.ibase.models.msg_shc_classes import ShcMsgAbbr




  
class ShcMsgAbbrType(DjangoObjectType):
    class Meta:
        model = ShcMsgAbbr


class Query(graphene.ObjectType):
    get_msgcodes = graphene.List(ShcMsgAbbrType)
   
   
    def resolve_get_msgcodes(root, info):
        return (
            ShcMsgAbbr.objects.all()
        )
       


schema = graphene.Schema(query=Query)