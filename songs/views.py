from songs.models import Songs
from albumes.models import Albumes
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def get_songs(request):    
    if request.method == 'POST':
        data = json.loads(request.body)
        model = Songs()
        model.name = data.get('name', None)
        model.albumId = Albumes.objects.get(pk=data.get('albumId', None))
        model.save()
        return HttpResponse(204)

@csrf_exempt
def song(request, pk):
    if request.method == 'POST':
        try:
            song = Songs.objects.filter(pk=pk)
            song.delete()
            status = 204
        except Songs.DoesNotExist:
            status = 404
        return HttpResponse(status)

    elif request.method == 'GET':
        try:
            songs = Songs.objects.filter(albumId=pk)
        except Songs.DoesNotExist:
            songs = []
        data = serializers.serialize('json', songs)
        return JsonResponse(data, safe=False)    
