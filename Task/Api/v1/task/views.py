from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from Task.Api.v1.task.serializer import TasksSerializer, TasksUpdateSerializer
from Task.models import Tasks


# Create your views here.
class TasksViews(APIView):
    # authentication_classes = [IsAuthenticated]
    @staticmethod
    @permission_classes([IsAuthenticated])
    def get(request):
        instance = Tasks.objects.all()
        serializer = TasksSerializer(instance, many=True)
        return Response(serializer.data)

    @staticmethod
    # @permission_classes([IsAuthenticated])
    def post(request):
        payload = request.data
        serializer = TasksSerializer(data=payload)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        request.POST._mutable = True
        return Response({"data": "New task added successfully"}, status=status.HTTP_201_CREATED)


class TasksDetailsViews(APIView):
    @staticmethod
    # @permission_classes([IsAuthenticated])
    def get(request, slug):
        task = get_object_or_404(Tasks, slug=slug)
        serializer = TasksSerializer(task)
        return Response(serializer.data)

    @staticmethod
    # @permission_classes([IsAuthenticated])
    def put(request, slug):
        try:
            task = Tasks.objects.get(slug=slug)
        except Tasks.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        payload = request.data
        serializer = TasksUpdateSerializer(task, data=payload)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({"data": "Task updated successfully"}, status=status.HTTP_200_OK)

    @staticmethod
    # @permission_classes([IsAuthenticated])
    def delete(request, slug):
        try:
            task = Tasks.objects.get(slug=slug)
        except Tasks.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({"data": "Task deleted successfully"}, status=status.HTTP_200_OK)
