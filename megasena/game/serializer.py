from rest_framework import serializers

from game.models import Plays


class PLaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plays
        fields = '__all__'
