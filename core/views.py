from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Client, Program, User
from django.contrib.auth.models import Group
from .serializers import ClientSerializer, ClientCreateSerializer, ProgramSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsDoctor

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ClientCreateSerializer
        return ClientSerializer

    @action(detail=True, methods=['post'])
    def enroll(self, request, pk=None):
        client = self.get_object()
        program_ids = request.data.get("program_ids", [])
        programs = Program.objects.filter(id__in=program_ids)
        client.programs.add(*programs)
        return Response({"message": "Client enrolled successfully."})

    @action(detail=False, methods=['get'])
    def search(self, request):
        name = request.query_params.get('name', '')
        clients = Client.objects.filter(name__icontains=name)
        serializer = self.get_serializer(clients, many=True)
        return Response(serializer.data)

class ClientViewSet(viewsets.ModelViewSet):
    ...
    permission_classes = [IsAuthenticated, IsDoctor]
