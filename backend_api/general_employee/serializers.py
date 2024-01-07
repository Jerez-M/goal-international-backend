from rest_framework import serializers
from .models import GeneralEmployee
from accounts.serializers import UserSerializer, RetrieveUserSerializer
from accounts.models import User
from django.contrib.auth.models import Group, Permission

class GeneralEmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GeneralEmployee
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        groups_data = user_data.pop('groups', [])
        permissions_data = user_data.pop('user_permissions', [])

        user = User.objects.create(**user_data)
        
        user.role = 'GENERAL EMPLOYEE'
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        total_general_employees = GeneralEmployee.objects.filter(
            user__organisation_id=user_data['organisation']
        ).count()
        new_username = f'{user.username}{total_general_employees}GE'
        user.username = new_username
        user.set_password(new_username)

        try:
            general_employee = GeneralEmployee.objects.create(user=user, **validated_data)
            user.save()

            groups = Group.objects.filter(id__in=[group_data['id'] for group_data in groups_data])
            general_employee.user.groups.set(groups)

            permissions = Permission.objects.filter(id__in=[perm_data['id'] for perm_data in permissions_data])
            general_employee.user.user_permissions.set(permissions)

            general_employee.save()
            return general_employee

        except Exception as e:
            user.delete()  # Delete the user if general_employee creation fails
            raise e  # Re-raise the exception

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        groups_data = user_data.pop('groups', [])
        permissions_data = user_data.pop('user_permissions', [])

        if user_data:
            user = instance.user
            for key, value in user_data.items():
                setattr(user, key, value)
            user.save()

        if groups_data:
            groups = Group.objects.filter(id__in=[group_data['id'] for group_data in groups_data])
            instance.user.groups.set(groups)

        if permissions_data:
            permissions = Permission.objects.filter(id__in=[perm_data['id'] for perm_data in permissions_data])
            instance.user.user_permissions.set(permissions)

        return super().update(instance, validated_data)
    

class GeneralEmployeeRetrieveSerializer(serializers.ModelSerializer):
    user = RetrieveUserSerializer()

    class Meta:
        model = GeneralEmployee
        fields = "__all__"


    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        groups_data = user_data.pop('groups', [])
        permissions_data = user_data.pop('user_permissions', [])

        if user_data:
            user = instance.user
            for key, value in user_data.items():
                setattr(user, key, value)
            user.save()

        if groups_data:
            groups = Group.objects.filter(id__in=[group_data['id'] for group_data in groups_data])
            instance.user.groups.set(groups)

        if permissions_data:
            permissions = Permission.objects.filter(id__in=[perm_data['id'] for perm_data in permissions_data])
            instance.user.user_permissions.set(permissions)

        return super().update(instance, validated_data)