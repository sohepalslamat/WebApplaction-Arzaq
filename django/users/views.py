from json import loads
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsSuperUser
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.contrib.auth.models import User



# Create your views here.
@api_view(["GET"])
@permission_classes((IsSuperUser,))
def users(request):

        context = User.objects.all()
        context = serialize(context)
        

        return JsonResponse(context ,safe=False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsSuperUser,))
def checkusername(request):

        req = loads(request.body)
        username = req["username"]
        try:
            user = User.objects.get(username__exact=username)            
            return HttpResponse("true")
        except:
            return HttpResponse("false")


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsSuperUser,))
def adduser(request):

        req = loads(request.body)
        username = req["username"]
        password = req["password"]
        email = req["email"]
        first_name = req["first_name"]
        is_superuser = req["is_superuser"]
        user = User(username=username, password=password, email=email, first_name=first_name,
        is_superuser=is_superuser)
        

        user.save()
        
        return HttpResponse("created")

@csrf_exempt
@api_view(["PUT"])
def edituser(request, id):
               
        req = loads(request.body)
        username = req["username"]
        password = req["password"]
        email = req["email"]
        first_name = req["first_name"]
        is_superuser = req["is_superuser"]
        
        user = User.objects.filter(id=req['id'])
        user.update(username=username, password=password, email=email, first_name=first_name,
         is_superuser=is_superuser)
        
        return HttpResponse("edited")
'''
@api_view(["GET","POST"])
def login(request):
    if request.method == "POST":
        req = loads(request.body)
        username = req["username"]
        password = req["password"]
        
        user = authenticate(username=username, password=password)
    if user is not None:
        return JsonResponse(serialize(user) ,safe=False )
    else:
        return JsonResponse({'username':'Error'} ,safe=False)
'''
##################################


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    req = loads(request.body)
    username = req["username"]
    password = req["password"]
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return JsonResponse(serialize(user, token.key) ,safe=False, status=HTTP_200_OK )
    

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAdminUser,))
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)
##################################


def serialize(context,tokenKey):
    try:
        all =[]
        for data in context:
            all.append({'Authorization':tokenKey,'id': data.id, 'username': data.username,
             'password': data.password , 'email': data.email ,'first_name': data.first_name ,
             'is_superuser': data.is_superuser})
    except:         
        data = context
        all = {'Authorization':tokenKey,'id': data.id, 'username': data.username,
             'password': data.password , 'email': data.email ,'first_name': data.first_name ,
             'is_superuser': data.is_superuser}
    
        
    return all

def authenticate( username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None

    if user.password == password:
        return user
    else:
        return None
