from rest_framework import serializers
from rest_framework_simplejwt.serializers import RefreshToken
from .models import User

import random
sent_otp = str(random.randint(1000, 9999))


class UserSerializer(serializers.ModelSerializer):
    fname = serializers.CharField(required=False)
    lname = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    token = serializers.SerializerMethodField(read_only=True)
    otp = serializers.SerializerMethodField(read_only=True)
    # spots = serializers.HyperlinkedRelatedField(view_name='spots', read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'fname', 'lname', 'email', 'phone', 'is_verified', 'token', 'otp')

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def get_otp(self, obj):
        return str(sent_otp)
