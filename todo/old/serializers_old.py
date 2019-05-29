from django.contrib.auth.models import User, Group
from rest_framework import serializers
from todo.models import Desks, CompanyName, Profile
from rest_framework.validators import UniqueTogetherValidator


class DesksSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    company_name=serializers.SlugRelatedField(
        slug_field='name',
        queryset=CompanyName.objects.all()
     )
    class Meta:
        model = Desks
        fields = ('id','company_name','created','done','due_date','task','owner','executor')


    def create(self, validated_data):

        #Create and return a new `Desks` instance, given the validated data.

        return Desks.objects.create(**validated_data)

    def update(self, instance, validated_data):

        #Update and return an existing `Desks` instance, given the validated data.

        instance.due_date = validated_data.get('due_date', instance.title)
        instance.task = validated_data.get('task', instance.code)

        instance.company_name = validated_data.get('company_name', instance.title)
        instance.executor = validated_data.get('executor', instance.code)

        instance.done = validated_data.get('done', instance.code)


        instance.save()
        return instance


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    desks = serializers.PrimaryKeyRelatedField(many=True, queryset=Desks.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'desks')

class CreateUserSerializer(serializers.ModelSerializer):

    """company1=serializers.StringRelatedField(many=True)
    company2=serializers.StringRelatedField(many=True)
    company3=serializers.StringRelatedField(many=True)
    company4=serializers.StringRelatedField(many=True)"""

    company1=serializers.SlugRelatedField(
                slug_field='name',
                queryset=CompanyName.objects.all())
    company2=serializers.SlugRelatedField(
                slug_field='name',
                queryset=CompanyName.objects.all())
    company3=serializers.SlugRelatedField(
                slug_field='name',
                queryset=CompanyName.objects.all())
    company4=serializers.SlugRelatedField(
                slug_field='name',
                queryset=CompanyName.objects.all())

    class Meta:
        model = User

        fields = ('username', 'email', 'password',
                  'company1', 'company2', 'company3', 'company4')

class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile

            fields = ('user','idsession', 'active_company', 'enabled_company')
