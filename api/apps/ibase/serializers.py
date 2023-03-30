from rest_framework import serializers
from apps.ibase.models.msg_shc_classes import ShcMsgAbbr

class ShcMsgAbbrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShcMsgAbbr
        fields = '__all__'