from rest_framework.serializers import ModelSerializer
from .models import Superuser
from accounts.serializers import UserSerializer, RetrieveUserSerializer
from accounts.models import User
from django.contrib.auth.models import Group, Permission

class SuperuserSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Superuser
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        groups_data = user_data.pop('groups', [])
        permissions_data = user_data.pop('user_permissions', [])

        user = User.objects.create(**user_data)
        
        user.role = 'SUPERUSER'
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        total_superusers = Superuser.objects.filter(
            user__organisation_id=user_data['organisation']
        ).count()
        new_username = f'{user.username}{total_superusers}SU'
        user.username = new_username
        user.set_password(new_username)

        try:
            superuser = Superuser.objects.create(user=user, **validated_data)
            user.save()

            groups = Group.objects.filter(id__in=[group_data['id'] for group_data in groups_data])
            superuser.user.groups.set(groups)

            permissions = Permission.objects.filter(id__in=[perm_data['id'] for perm_data in permissions_data])
            superuser.user.user_permissions.set(permissions)

            superuser.save()
            return superuser

        except Exception as e:
            user.delete()  # Delete the user if superuser creation fails
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
    

class SuperuserRetrieveSerializer(ModelSerializer):
    user = RetrieveUserSerializer()

    class Meta:
        model = Superuser
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