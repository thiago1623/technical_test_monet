from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dashboard import basic_common_v1
from ..serializers.test_and_question_serializers import TestSerializer, AnswerSerializer


@api_view(['POST', 'GET'])
def create_test_api(request, test_id=None):
    """
        create test with questions and answers:
        request.data is an object
        Pdt: I used Response in this api but if you have a front for example react or nuxt you can use JsonResponse
        the method authenticated_user_from_request in this momment search a user login and is student
        but If you want to improve this method you can include JWT
    """
    user, payload = basic_common_v1.authenticated_user_from_request(request)

    if request.method == 'GET' and user and test_id:
        test, payload = basic_common_v1.get_test(test_id)
        if payload:
            return Response(payload)
        return Response({'test': TestSerializer(test).data})

    if request.method == 'POST' and user:
        test, payload = basic_common_v1.create_test(data_test=request.data, user=user)
        if payload:
            return JsonResponse(payload, status=404)
        return Response({
            'test': TestSerializer(test, user=user).data
        })
    return Response({'msg': 'method denied'}, status=400)


@api_view(['POST'])
def save_user_answer_selected(request):
    """
        save user answer for specific question
    """
    user, payload = basic_common_v1.authenticated_user_from_request(request)

    if request.method == 'POST' and user:
        answer, payload = basic_common_v1.save_answer(user_data=request.data, user=user)
        if payload:
            return JsonResponse(payload, status=404)
        return Response({
            'answer': AnswerSerializer(answer, user=user).data
        })
    return Response({'msg': 'method denied'}, status=400)
