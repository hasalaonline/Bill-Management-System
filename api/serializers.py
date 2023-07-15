from rest_framework.serializers import ModelSerializer
from app.models import CEB, NWSDB

class CEBSerializer(ModelSerializer):
    class Meta:
        model = CEB
        fields = '__all__'

class NWSDBSerializer(ModelSerializer):
    class Meta:
        model = NWSDB
        fields = '__all__'