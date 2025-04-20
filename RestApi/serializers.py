from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        # fields = ['id', 'name', 'image', 'created_at']
        # exclude = ['created_at']