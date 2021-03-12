from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, sent_otp
from django.shortcuts import get_object_or_404, Http404
from .send_mail import mail


# class UserView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#         def get_queryset(self):
#             if self.request.user.is_staff:
#                 return User.objects.all()
#             else:
#                 return User.objects.all().filter(id=self.request.user.id)


@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            mail(request.data["email"], sent_otp)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response('Deleted', status=status.HTTP_204_NO_CONTENT)

    def patch(self,  request, *args, **kwargs):
        user = get_object_or_404(User, *args, **kwargs)
        data = request.data
        user.fname = data.get("fname", user.fname)
        user.lname = data.get("lname", user.lname)
        user.phone = data.get("phone", user.phone)
        user.is_verified = data.get("is_verified", user.is_verified)
        user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data)
