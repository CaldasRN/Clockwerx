from rest_framework import serializers
from clocksapp.models import Timer
class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = ('hour', 'min', 'sec')
