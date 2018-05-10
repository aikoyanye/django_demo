from .models import User
from rest_framework_mongoengine import serializers as mongo_serializers

# 名字随意
class UserSerializer(mongo_serializers.DocumentSerializer):
    class Meta:
        # 对应类名
        model = User
        # 各个字段，其中id是默认id字段
        fields = ('id', 'name', 'age', 'pwd')