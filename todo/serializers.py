from django.contrib.auth.models import User, Group
from rest_framework import serializers
from todo.models import Desk, Company
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.authtoken.serializers import AuthTokenSerializer

from django.contrib.auth.models import User

class CompanySerializer(serializers.ModelSerializer):
        class Meta:
            model = Company

            fields = ('name','id')
class DeskSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    company_name=serializers.SlugRelatedField(
        slug_field='name',
        queryset=Company.objects.all()
     )
    class Meta:
        model = Desk
        fields = ('id','company_name','created','done','due_date','task','owner','executor')


    def create(self, validated_data):

        #Create and return a new `Desks` instance, given the validated data.

        return Desk.objects.create(**validated_data)

    def update(self, instance, validated_data):

        #Update and return an existing `Desks` instance, given the validated data.

        instance.due_date = validated_data.get('due_date', instance.title)
        instance.task = validated_data.get('task', instance.code)

        instance.company_name = validated_data.get('company_name', instance.title)
        instance.executor = validated_data.get('executor', instance.code)

        instance.done = validated_data.get('done', instance.code)


        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    desks = serializers.PrimaryKeyRelatedField(many=True, queryset=Desk.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'desks')

class CreateUserSerializer(serializers.ModelSerializer):

    """company1=serializers.StringRelatedField(many=True)
    company2=serializers.StringRelatedField(many=True)
    company3=serializers.StringRelatedField(many=True)
    company4=serializers.StringRelatedField(many=True)"""

    companies=serializers.SlugRelatedField(slug_field='name',
                                           queryset=Company.objects.all())

    class Meta:
        model = User

        fields = ('username', 'email', 'password', 'companies')

class GetUserSerializer(serializers.Serializer):

    list_name_company = serializers.ListField(
        child = serializers.SlugRelatedField(
                        slug_field='name',
                        queryset=Company.objects.all())
    )

    username = serializers.SlugRelatedField(
                        slug_field='username',
                        queryset=User.objects.all())
