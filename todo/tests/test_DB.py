from django.test import TestCase, TransactionTestCase
import unittest

import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'tztodo.settings'
django.setup()

from todo.models import Company, Desk
from todo.views import CompanyDeskList, DeskList
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework.test import APIClient, APIRequestFactory
from rest_framework import status

class DeskTestDB(TransactionTestCase):
    fixtures = ['data_for_test.json']

    def setUp(self):
        #Set up non-modified objects used by all test methods
        self.user=User.objects.get(username='admin')
        self.desk=Desk.objects.create(company_name=Company.objects.get(name='RGD'),
                                    due_date = '2000-01-23',
                                    task = 'For testing',
                                    executor = self.user.username,
                                    owner = self.user)
        self.desk.save()

    def test_get_real_Desks(self):
        token = Token.objects.get(user__username='dima')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/todo/RGD/2019-04-25/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(len(response.data['results']), 0)

    def test_get_test_Desks(self):
        token = Token.objects.get(user__username='dima')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/todo/RGD/2000-01-23/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)

    def test_get_obj_from_testDB_1(self):
        try:
            obj=Desk.objects.get(due_date = '2000-01-23', executor = 'admin')
        except Desk.DoesNotExist:
            self.assertTrue(False)
        else:
            self.assertTrue(True)

    def test_get_obj_from_DBtestDB_2(self):
        try:
            obj=Desk.objects.get(due_date = '2019-04-25', executor = 'admin')
        except Desk.DoesNotExist:
            self.assertTrue(False)
        else:
            self.assertTrue(True)
