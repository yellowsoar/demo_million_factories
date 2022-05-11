from rest_framework import serializers

from justatest.models import Factory


class FactoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'
