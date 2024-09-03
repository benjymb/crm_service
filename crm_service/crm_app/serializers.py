from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Customer, CustomUser
from .exceptions import NotFound, InvalidParameters, PermissionDenied
from .image_handling import process_image
from uuid import uuid1
from .permission_handling import validate_permissions
from django.contrib.auth.models import Group


class GroupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)


class CompleteUserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=250)
    last_name = serializers.CharField(max_length=250)
    email = serializers.CharField(max_length=250),
    groups = GroupSerializer(many=True, required=False)

    @staticmethod
    def get_users(user):
        validate_permissions(user)
        users = CustomUser.objects.all()
        serializer = CompleteUserSerializer(users, many=True)
        return serializer.data
    
    @staticmethod
    def get_user(pk, user):
        validate_permissions(user)
        try:
            user = CustomUser.objects.get(pk=pk)
            serializer = CompleteUserSerializer(user, many=False)
            return serializer.data
        except CustomUser.DoesNotExist  as e:
            raise NotFound(f"The user with pk {pk} doesn't exist.")
        except ValidationError as e:
            raise InvalidParameters(f"The identifier {pk} is not in a valid format")
        

    @staticmethod
    def create_user(data, user):
        validate_permissions(user)
        serializer = CompleteUserSerializer(data=data)
        if serializer.is_valid():
            new_user = CustomUser.objects.create(
                **data
            )
            if data['is_admin']:
                new_user.groups.add(Group.objects.get(name='admin_group'))
            return CompleteUserSerializer(new_user).data
        else:
            raise InvalidParameters(serializer.errors)
        

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField(max_length=150)

class CustomerSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=150)
    surname = serializers.CharField(max_length=250)

    updated_by = UserSerializer(many=False, required=False, read_only=True)
    created_by = UserSerializer(many=False, read_only=True)
    photo = serializers.ImageField(required=False)

    @staticmethod
    def get_customers():
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return serializer.data
    

    @staticmethod
    def get_customer(pk):
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customer, many=False)
            return serializer.data
        except Customer.DoesNotExist  as e:
            raise NotFound(f"The customer with pk {pk} doesn't exist.")
        except ValidationError as e:
            raise InvalidParameters(f"The pk {pk} is not in a valid format")
        
    @staticmethod
    def create_customer(data, user):
        photo = None
        data['created_by_id'] = user.id
        if data.get('photo'):
            photo = process_image(data['photo'], uuid1())
            del data['photo']
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            if photo:
                data['photo'] = photo
            new_customer = Customer.objects.create(
                **data
            )
            if photo:
                photo.close()
            return CustomerSerializer(new_customer).data
        else:
            raise InvalidParameters(serializer.errors)
        
    @staticmethod
    def update_customer(data, pk, user):
        data['updated_by_id'] = user.id
        if data.get('photo'):
            data['photo'] = process_image(data['photo'])
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            Customer.objects.filter(pk=pk).update(
                **data
            )
            return CustomerSerializer(Customer.objects.get(pk=pk)).data
        else:
            raise InvalidParameters(serializer.errors)
        
    @staticmethod
    def delete_customer(customer_id):
        try:
            Customer.objects.get(pk=customer_id).delete()
        except Customer.DoesNotExist:
            raise InvalidParameters("The customer with the id was not found.")
