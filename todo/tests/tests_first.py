from django.test import TestCase
import unittest

#import django
#import os
#os.environ['DJANGO_SETTINGS_MODULE'] = 'tztodo.settings'
#django.setup()

from todo.models import Company, Desk
from todo.views import CompanyDeskList, DeskList
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework import status


class DeskModelTest(TestCase):
    fixtures = ['data_for_test.json']
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Desk.objects.create(company_name=Company.objects.get(id=6),
                            due_date = '2019-10-10',
                            task = 'For testing',
                            executor = User.objects.get(username='admin'),
                            owner = User.objects.get(username='admin'))

    def test_task_label(self):
        desk=Desk.objects.get(task = 'For testing')
        field_label = desk._meta.get_field('task').verbose_name
        self.assertEqual(field_label,'task')

class CompanyViewTest(TestCase):
    #@unittest.skip("demonstrating skipping")
    def test_get_Desks(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='dima')
        view = CompanyDeskList.as_view()
        request = factory.get('/todo/RGD/desks')
        force_authenticate(request, user=user, token=user.auth_token)
        print(request)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_admin_Desks(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='admin')
        view = DeskList.as_view()
        request = factory.get('/todo/desks/')
        force_authenticate(request, user=user)
        print(request)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #@unittest.skip("demonstrating skipping")
    def test_get_Desks_v2(self):
        token = Token.objects.get(user__username='dima')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/todo/Aeroflot/desks')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #assert response.status_code == 200
