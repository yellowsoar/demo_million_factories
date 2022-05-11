from justatest.models import Factory
from justatest.serializers import FactoryRetrieveSerializer
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from rest_framework import mixins, viewsets

default_lat = 24.08825881648228
default_lng = 120.48504632216294
default_radius = 10
point = Point(default_lng, default_lat)


class FactoriesViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Factory.objects.all()
    serializer_class = FactoryRetrieveSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        queryset = Factory.objects.filter(
            location__distance_lt=(
                Point(
                    float(query_params['lng'])
                    if query_params['lng'].isdecimal()
                    else default_lng,
                    float(query_params['lat'])
                    if query_params['lat'].isdecimal()
                    else default_lat,
                ),
                Distance(
                    km=float(query_params['range'])
                    if query_params['range'].isdecimal()
                    else default_radius,
                ),
            )
        ).all()
        return queryset
