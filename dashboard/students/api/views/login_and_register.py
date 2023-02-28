from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from dashboard import basic_common_v1
from ..serializers.user_serializer import RegisterSerializer, UserSerializer


@api_view(['POST'])
def student_register(request):

    if request.method == 'POST':
        user = RegisterSerializer(data=request.data)
        if user.is_valid():
            user.save()
            user, payload = basic_common_v1.get_user_from_serializer(user.data)
            if payload:
                return JsonResponse({'error': payload}, status=404)
            student = basic_common_v1.create_student(user=user)
            return JsonResponse(UserSerializer(user).data, status=200)
        return JsonResponse({'errors': user.errors}, status=404)


class RegisterAPIview(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user, payload = basic_common_v1.get_user_from_serializer(serializer.data)
            if payload:
                return JsonResponse({'error': payload}, status=404)
            _ = basic_common_v1.create_student(user=user)
            return Response({
               'message': 'user created successfully',
               'user': serializer.data,
            })
        return JsonResponse({'errors': serializer.errors}, status=404)



