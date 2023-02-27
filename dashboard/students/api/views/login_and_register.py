import json

from django.http import JsonResponse
#from datetime import datetime, timedelta
#from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


from ..serializers.user_serializer import RegisterSerializer
from common import basic_common


@api_view(['POST'])
def student_register(request):

    if request.method == 'POST':
        user = RegisterSerializer(request.data)
        if user.is_valid():
            user.save()
            return JsonResponse({'user': user.data}, status=200)
        return JsonResponse({'errors': user.errors}, status=404)


class RegisterAPIview(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = basic_common.get_user_from_serializer(serializer.data)
            return Response({
               'message': 'user created successfully',
               'user': serializer.data
            })
        return JsonResponse({'errors': serializer.errors}, status=404)



