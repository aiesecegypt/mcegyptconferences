from rest_framework import serializers
from .models import Delegate


class DelegateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegate
        fields = '__all__'
        read_only_fields = ['delegate_id', 'timestamp']
