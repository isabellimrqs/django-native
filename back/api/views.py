from django.shortcuts import render
from .models import Cliente
from .serializer import ClienteSerializer, UserSerializar
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

@api_view(['GET', 'POST'])
def listar_clientes(request):
    if request.method == 'GET':
        queryset = Cliente.objects.all()
        serializer = ClienteSerializer(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST': 
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED) 
        else:
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class ClientesView(ListCreateAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClientesDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    serializer = UserSerializar(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

