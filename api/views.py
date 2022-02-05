from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

# show all the views that we gonna have in this project

from .serializers import TaskSerializer
from .models import Task


@api_view(['GET'])
def apiOverView(request):
    # this view is over view
    api_urls = {
        'List': '/task-list/',
        'Detail View ': '/task-detail/',
        'Create ': '/task-create/',
        'Update': '/task-update/',
        'Delete ': '/task-delete/',
    }

    # return Response('hello response ', safe=False)
    return Response(api_urls)


# all list of responses that can see it in db

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, id):
    tasks = Task.objects.get(id=id)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response('task deleted successfully ... ')
