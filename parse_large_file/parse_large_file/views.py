from django.db.models import Count
from rest_framework import viewsets

from parse_large_file.models import Customer

from parse_large_file.serializers import CustomerSerializer, CustomerAgeSerializer


class CustomerAgeViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.values('age').annotate(total=Count('id'))
    serializer_class = CustomerAgeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-last_seen')
    serializer_class = CustomerSerializer
