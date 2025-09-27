from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from gestion.models import Rol, User
from gestion.serializers import RolSerializer, UserSerializer

@api_view(['GET','POST'])
def crud_rol(request):
    if request.method == 'GET':
        roles = Rol.objects.all()
        serializer = RolSerializer(roles, many = True)
        return Response(serializer.data)   


    elif request.method == 'POST':
        serializer = RolSerializer(data= request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer._errors, status= status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def crud_user(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)   


    elif request.method == 'POST':
        serializer = UserSerializer(data= request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer._errors, status= status.HTTP_400_BAD_REQUEST)
            
@api_view(['GET'])
def userByRol(request):
    users = User.objects.filter(rol_id=1)    
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)   

@api_view(['GET'])
def api_ext(request):
    url = "https://restcountries.com/v3.1/name/bolivia"
    response = requests.get(url)
    data = response.json()[0]
    print(data)
    result = {
        "nombre_comun": data.get("name", {}).get("common"),
        "nombre_oficial": data.get("name", {}).get("official"),
        "capital": data.get("capital", [None])[0],
        "region": data.get("region"),
        "subregion": data.get("subregion"),
        "poblacion": data.get("population"),
        "bandera": data.get("flag"),
        "mapa_google": data.get("maps").get("googleMaps"),
        "moneda": list(data.get("currencies", {}).keys())[0] if data.get("currencies") else None,
        "idiomas": list(data.get("languages", {}).values()) if data.get("languages") else [],
    }

    rol = {
        "nombre": data.get("name", {}).get("common")
    }
    Rol.objects.create(**rol)
    return Response(result)   

@api_view(['GET'])
def show_rol(request):
    respuesta= [
       {"inicio":"a"}
    ]
    return Response(respuesta)