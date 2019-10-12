from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from json import loads
from main.models import Units

# Create your views here.
@api_view(["GET"])
def units(request):

        context = Units.objects.all()  
        context = Units.serialize(context)

        return JsonResponse(context ,safe=False)

@api_view(["POST"])
def addunit(request):

        req = loads(request.body)
        name = req["name"]
        unit = Units(name=name)
        unit.save()
        
        return HttpResponse("created")

@api_view(["PUT"])
def editunit(request, id):
               
        req = loads(request.body)
        print(req)
        unit = Units.objects.filter(id=req['id'])
        unit.update(name=req['name'])
        
        return HttpResponse("edited")