from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListAPIView

from .models import Student
from .serializer import StudentSerializers

class StudentListAPIView(ListAPIView):
    model = Student
    serializer = StudentSerializers

    def get_queryset(self):
        return Student.objects.all
