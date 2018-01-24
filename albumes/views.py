from songs.models import Songs
from albumes.models import Albumes
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def get_albumes(request):
    if request.method == 'GET':
        albumes = Albumes.objects.all()
        data = serializers.serialize('json', albumes)
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        model = Albumes()
        model.name = data.get('name', None)
        model.save()
        return HttpResponse(204)

@csrf_exempt
def remove_album(request, pk):
    if request.method == 'POST':
        try:
            albumes = Albumes.objects.get(pk=pk)
            songs = Songs.objects.filter(albumId=pk)
            songs.delete()
            albumes.delete()
            status = 204
        except Albumes.DoesNotExist:
            status = 404
        return HttpResponse(status)
