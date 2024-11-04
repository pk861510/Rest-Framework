from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import (NavbarContent,OurClient
                    ,ClientTestimonials,ManagementTeam
                    ,DeveloperTeam)
from .serializers import (NavbarContentSerializer,OurClientSerializer
                        ,ClientTestimonialsSerializer,ManagementTeamSerializer
                        ,DeveloperTeamSerializer)


class NavbarContentViewSet(viewsets.ModelViewSet):
    queryset = NavbarContent.objects.all()    
    serializer_class = NavbarContentSerializer

class OurClientViewSet(viewsets.ModelViewSet):
    queryset = OurClient.objects.all()
    serializer_class = OurClientSerializer

class ClientTestimonialsViewSet(viewsets.ModelViewSet):
    queryset = ClientTestimonials.objects.all()
    serializer_class = ClientTestimonialsSerializer

class ManagementTeamViewSet(viewsets.ModelViewSet):
    queryset =ManagementTeam.objects.all()
    serializer_class = ManagementTeamSerializer

class DeveloperTeamViewSet(viewsets.ModelViewSet):
    queryset = DeveloperTeam.objects.all()
    serializer_class = DeveloperTeamSerializer


@api_view(['POST'])
def adddeveloper(request):
    developer = DeveloperTeamSerializer(data = request.data)
    if developer.is_valid():
        developer.save()
        return Response(developer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(developer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addmanagement(request):
    management = ManagementTeamSerializer(data = request.data)
    if management.is_valid():
        management.save()
    return Response(management.data)


@api_view(['POST'])
def addclient(request):
    client = OurClientSerializer(data = request.data)
    if client.is_valid():
        client.save()
    return Response(client.data)

@api_view(['POST'])
def addclienttmls(request):
    clienttmls = ClientTestimonialsSerializer(data = request.data)
    if clienttmls.is_valid():
        clienttmls.save()
    return Response(clienttmls.data)