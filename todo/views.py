from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from django.contrib.auth.models import User
from todo.serializers import UserSerializer, CreateUserSerializer
from todo.serializers import DeskSerializer, CompanySerializer, GetUserSerializer
from todo.models import Desk, Company

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions
from rest_framework.permissions import IsAdminUser
from guardian.shortcuts import assign_perm
from guardian.shortcuts import remove_perm

"""New classes:"""
class CompanyClassView(generics.GenericAPIView):
    def custom_check_permission(self, company, request):
        token_obj = Token.objects.get(user__username=request.user)
        try:
            company_obj=Company.objects.get(token=token_obj.key,
                                            name=company)
        except Company.DoesNotExist:
            self.permission_denied(self.request,
                                    message='Your profile does not have access to this company')

"""For admin views:"""
class SetUserPermission(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def post(self, request, *args, **kwargs):
        serializer = GetUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.data['username'])
        list_name_company=serializer.data['list_name_company']
        for company in Company.objects.filter(name__in=list_name_company):
            assign_perm('can_work_this_obj', user, company)

        return Response({
            'user': serializer.data['username'],
            'name_company': serializer.data['list_name_company'],
        })

class UserList(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CompanyList(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DeskList(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Desk.objects.all()
    serializer_class = DeskSerializer


"""For users views:"""
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, name_company, *args, **kwargs):
        try:
            company = Company.objects.get(name=name_company)
        except Company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.has_perm('can_work_this_obj', company):
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                pass
            else:
                token.delete()
            token = Token.objects.create(user=user)
            company.token.add(token)
            return Response({
                            'token': token.key,
                            'user_id': user.pk,
                            'email': user.email,
                            })
        else:
            return Response('Your profile does not have access to this company',
                             status=status.HTTP_403_FORBIDDEN)

class CompanyDeskList(mixins.ListModelMixin, CompanyClassView):
    permission_classes = (IsAuthenticated, )
    serializer_class = DeskSerializer

    def get(self, request, *args, **kwargs):
        company=self.kwargs.get('name_company')
        self.custom_check_permission(company, request)
        self.queryset=Desk.objects.filter(company_name__name=company)
        return self.list(request, *args, **kwargs)

class CompanyDateList(mixins.ListModelMixin, CompanyClassView):
    permission_classes = (IsAuthenticated, )
    serializer_class = DeskSerializer

    def get(self, request, *args, **kwargs):
        company=self.kwargs.get('name_company')
        due_date=self.kwargs.get('date')
        self.custom_check_permission(company, request)
        self.queryset=Desk.objects.filter(company_name__name=company,
                                          due_date=due_date)
        return self.list(request, *args, **kwargs)

"""class SessionUser(generics.RetrieveAPIView):
    def get_object(self):
        filter={'name' : self.kwargs.get('company'),
                'permission_users' : self.request.user.id}
        try:
            company_obj = Company.objects.get(**filter)
        except Company.DoesNotExist:
            raise Http404('No MyModel matches the given query.')
        user_session_obj=Session.objects.get(username=self.request.user.id)
        user_session_obj.update(company_obj)
        return (user_session_obj)
    serializer_class = SessionSerializer

class RegistrationUser(generics.CreateAPIView):
    def get_object(self):
        user_obj=User.objects.create_user(self.request.query_params.get('username'),
                                 self.request.query_params.get('email'),
                                 self.request.query_params.get('password'))

        return (user_obj)

    serializer_class = CreateUserSerializer"""

"""Registration users"""



"""    def get_queryset(self):
        user = self.request.user
        return (Profile.objects.filter(user=user.id))
    serializer_class = ProfileSerializer

class CompanyList(generics.ListAPIView):
    #queryset = Profile.objects.all()
    def get_queryset(self):
        user = self.request.user
        return (Profile.objects.filter(user=user.id))
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveAPIView):
    def get_queryset(self):
        return (Profile.objects.filter(user=self.kwargs.get('pk')))
    serializer_class = ProfileSerializer

class TestDetail(generics.ListAPIView):
    def get_queryset(self):
        userid= self.request.query_params.get('userid')
        return (Profile.objects.filter(user=userid))
    serializer_class = ProfileSerializer"""
