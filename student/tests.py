from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student


class StudentAPITests(APITestCase):
    studentlist = [{
        'name': 'abc',
        'birthday': '2021-03-07'
    }, {
        'name': 'Huy',
        'birthday': '2022-03-07'
    }, {
        'name': 'John',
        'birthday': '2021-04-07'
    }, {
        'name': 'Jack',
        'birthday': '2021-03-25'
    }, {
        'name': 'Jane',
        'birthday': '2022-01-11'
    }, {
        'name': 'Key',
        'birthday': '2023-03-02'
    }]

    response_ok = status.HTTP_200_OK

    def setUp(self):
        for student in self.studentlist:
            Student.objects.create(**student)

    def test_get_students(self):
        """
        Test get all movies
        """
        url = reverse('student-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, self.response_ok)
        for i in range(0, len(self.studentlist)):
            self.assertEqual(response.json()[i]['name'],
                             self.studentlist[i]['name'])
