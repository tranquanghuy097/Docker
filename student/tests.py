from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Movie

class StudentAPITests(APITestCase):
    studentlist = [{'name' : 'abc', 'birthday' : '2021-03-07'},
                    {'name' : 'Huy', 'birthday' : '2022-03-07'},
                    {'name' : 'John', 'birthday' : '2021-04-07'},
                    {'name' : 'Jack', 'birthday' : '2021-03-25'},
                    {'name' : 'Jane', 'birthday' : '2022-01-11'},
                    {'name' : 'Key', 'birthday' : '2023-03-02'}]
