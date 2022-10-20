from rest_framework import serializers

from parse_large_file.models import Customer


class CustomerAgeSerializer(serializers.HyperlinkedModelSerializer):
    total = serializers.IntegerField()

    class Meta:
        model = Customer
        fields = ['age', 'total']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['email', 'username', 'age', 'last_seen']
