from .models import Customer
from .serializers import CustomerSerializer, CompleteUserSerializer as UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .exceptions import NotFound, InvalidParameters, PermissionDenied

class CustomerView(APIView):

    def get(self, request, pk, format=None):
        try:
            return Response(CustomerSerializer.get_customer(pk))
        except NotFound as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND) 
        except InvalidParameters as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST) 


    def post(self, request, format=None):
        try:
            response = CustomerSerializer.create_customer(
                data=request.data, user=request.user
            )
            return Response(response, status=status.HTTP_201_CREATED)
        except InvalidParameters as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            response = CustomerSerializer.update_customer(
                data=request.data, pk=pk, user=request.user
            )
            return Response(response, status=status.HTTP_202_ACCEPTED)
        except InvalidParameters as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        try:
            response = CustomerSerializer.delete_customer(
                pk
            )
            return Response(response, status=status.HTTP_202_ACCEPTED)
        except InvalidParameters as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)



class CustomersView(APIView):

    def get(self, request, format=None):
        return Response(CustomerSerializer.get_customers())
    

class UsersView(APIView):

    def get(self, request, format=None):
        try:
            return Response(UserSerializer.get_users(request.user))
        except PermissionDenied as e:
            return Response(str(e), status=status.HTTP_401_UNAUTHORIZED)
    

class UserView(APIView):

    def get(self, request, pk, format=None):
        try:
            return Response(UserSerializer.get_user(pk, request.user))
        except PermissionDenied as e:
            return Response(str(e), status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        try:
            response = UserSerializer.create_user(
                data=request.data, user=request.user
            )
            return Response(response, status=status.HTTP_201_CREATED)
        except InvalidParameters as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            response = UserSerializer.update_user(
                data=request.data, pk=pk, user=request.user
            )
            return Response(response, status=status.HTTP_202_ACCEPTED)
        except InvalidParameters as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        try:
            response = UserSerializer.delete_user(
                pk
            )
            return Response(response, status=status.HTTP_202_ACCEPTED)
        except InvalidParameters as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)