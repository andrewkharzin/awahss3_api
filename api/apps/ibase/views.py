from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShcMsgAbbrSerializer
from apps.ibase.models.msg_shc_classes import ShcMsgAbbr

class MsgShcClassesList(APIView):
    def get(self, request):
        msg_shc_classes = ShcMsgAbbr.objects.all()
        serializer = ShcMsgAbbrSerializer(msg_shc_classes, many=True)
        return Response(serializer.data)