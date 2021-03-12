from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from spot.models import ParkingSpot
from spot.serializers import SpotSerializer
from django.shortcuts import get_object_or_404, Http404


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def spot_list(request):
    if request.method == 'GET':
        spot = ParkingSpot.objects.all()
        serializer = SpotSerializer(spot, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SpotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpotDetail(APIView):
    def get_object(self, pk):
        try:
            return ParkingSpot.objects.get(pk=pk)
        except ParkingSpot.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spot = self.get_object(pk)
        serializer = SpotSerializer(spot)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spot = self.get_object(pk)
        serializer = SpotSerializer(spot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spot = self.get_object(pk)
        spot.delete()
        return Response('Deleted', status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        spot = get_object_or_404(ParkingSpot, *args, **kwargs)
        data = request.data

        spot.description = data.get("description", spot.description)
        spot.price = data.get("price", spot.price)
        spot.image = data.get("image", spot.image)
        spot.available = data.get("available", spot.available)
        spot.longitude = data.get("longitude", spot.longitude)
        spot.latitude = data.get("latitude", spot.latitude)

        spot.save()
        serializer = SpotSerializer(spot)

        return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def spot_detail(request, pk):

#     try:
#         spot = ParkingSpot.objects.get(pk=pk)
#     except ParkingSpot.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SpotSerializer(spot)
#         print(serializer.data)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SpotSerializer(spot, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         spot.delete()
#         return Response('Deleted', status=status.HTTP_204_NO_CONTENT)
