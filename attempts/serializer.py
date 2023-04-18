from rest_framework import serializers
from .models import Attempt

class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = "__all__"