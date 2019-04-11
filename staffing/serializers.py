from rest_framework import serializers
from .models import Company, Profile, Role_Type, Employee, Role_Log, CustomUser, Profile

class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role_Type
        fields = ('title', )
