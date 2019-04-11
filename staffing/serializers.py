from rest_framework import serializers
from .models import Company, Profile, Role_Type, Employee, Role_Log, CustomUser, Profile

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    role_log = serializers.HyperlinkedRelatedField(
        view_name='employee_detail',
        many=True,
        read_only=True
    )
    +   class Meta:
+       model = Company
+       fields = ('id', 'photo_url', 'nationality', 'name', 'songs')