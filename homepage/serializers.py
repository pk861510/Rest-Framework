from rest_framework import serializers
from .models import NavbarContent,OurClient,ClientTestimonials,ManagementTeam,DeveloperTeam

class NavbarContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavbarContent
        fields = '__all__'

class OurClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurClient
        fields = '__all__'

class ClientTestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientTestimonials
        fields = '__all__'

class ManagementTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementTeam
        fields = '__all__'

class DeveloperTeamSerializer(serializers.ModelSerializer):  
    class Meta:
        model = DeveloperTeam
        fields = '__all__'  