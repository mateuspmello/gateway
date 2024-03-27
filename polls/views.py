from django.http import HttpResponse, JsonResponse
from django.template import loader
import requests
from polls.serializers import PostSerializer, AuthorSerializer
from .models import *
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

@csrf_exempt
def get_token(request):
    keycloak_host = 'keycloak:8080'
    realm = 'myrealm'
    grant_type = request.META.get('HTTP_GRANT_TYPE')
    client_id = request.META.get('HTTP_CLIENT_ID')
    client_secret = request.META.get('HTTP_CLIENT_SECRET')
    username = request.META.get('HTTP_USERNAME')
    password = request.META.get('HTTP_PASSWORD')
    print(grant_type, client_id, client_secret, username, password)
    token_url = 'http://{keycloak_host}/realms/{realm}/protocol/openid-connect/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': grant_type,
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': password
    }
    response = requests.post(token_url.format(realm=realm, keycloak_host=keycloak_host), headers=headers, data=data)
    
    if response.status_code == requests.codes.unauthorized:
        return JsonResponse({'error': 'Invalid credentials'}, status=response.status_code)
    
    return HttpResponse(response.json()['access_token'])

@csrf_exempt
def validate_token(request):
    keycloak_host = 'keycloak:8080'
    realm = 'myrealm'
    introspect_url = 'http://{keycloak_host}/realms/{realm}/protocol/openid-connect/token/introspect'
    client_id = request.META.get('HTTP_CLIENT_ID')
    client_secret = request.META.get('HTTP_CLIENT_SECRET')
    access_token = request.META.get('HTTP_AUTHORIZATION').replace('Bearer ', '')
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'token': access_token,
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(introspect_url.format(realm=realm, keycloak_host=keycloak_host), headers=headers, data=data)
    response.raise_for_status()
    return HttpResponse(response.json())

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    http_method_names = ['get','post','retrieve','put','patch']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get','post','retrieve','put','patch']


