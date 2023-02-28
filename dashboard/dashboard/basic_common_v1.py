from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User as AuthUser

from students.models import Student, Test, Question, Answer


def get_user_from_serializer(serializer):
    try:
        return AuthUser.objects.get(pk=serializer.get('pk')), None
    except ObjectDoesNotExist:
        return None, {'error': 'user not found'}


def create_student(user):
    try:
        return Student.objects.get(pk=user.pk)
    except ObjectDoesNotExist:
        student = Student.objects.create(user=None)
        student.user = user
        student.save()
        return student


def get_student_from_auth_user(user):
    try:
        return Student.objects.get(user=user), None
    except ObjectDoesNotExist:
        return None, {'msg': 'student not found'}


def user_access_denied():
    return {'msg': 'access denied'}


def get_student(user):
    student, _ = get_student_from_auth_user(user)
    if student and student.user.is_authenticated:
        return student.user, None
    else:
        return None, user_access_denied()


def authenticated_user_from_request(request):
    if request.GET.get('user_id'):
        try:
            user = AuthUser.objects.get(pk=int(request.GET.get('user_id')))
            student, payload = get_student(user)
            return student, payload
        except ObjectDoesNotExist:
            return None, user_access_denied()
    elif request.POST.get('user_id'):
        try:
            user = AuthUser.objects.get(pk=int(request.POST.get('user_id')))
            student, payload = get_student(user)
            return student, payload
        except ObjectDoesNotExist:
            return None, user_access_denied()
    elif request.data.get('user_id'):
        try:
            user = AuthUser.objects.get(pk=int(request.data.get('user_id')))
            student, payload = get_student(user)
            return student, payload
        except ObjectDoesNotExist:
            return None, user_access_denied()


def create_answers(data_answers, user):
    answers = []
    for answer in data_answers:
        try:
            answer_obj = Answer.objects.create(text=answer.get('text'),
                                               auth_user=user,
                                               order=answer.get('order'),
                                               is_correct=answer.get('is_correct'))
            answers.append(answer_obj)
        except ValueError:
            return None, {'msg': 'Some parameters are missing'}
    return answers, None


def create_questions(data_questions, user):
    questions = []
    for question in data_questions:
        try:
            question_obj = Question.objects.create(text=question.get('text'),
                                                   auth_user=user,
                                                   order=question.get('order'))
            answers, payload = create_answers(question.get('answers'), user)
            if payload:
                return payload
            question_obj.answers.set(answers)
            questions.append(question_obj)
        except ValueError:
            return None, {'msg': 'Some parameters are missing'}
    return questions, None


def create_test(data_test, user):
    """
        you can use this method for create a test in your app
    """
    try:
        test = Test.objects.create(name=data_test.get('name'), auth_user=user)
        questions, payload = create_questions(data_test.get('questions'), user)
        test.questions.set(questions)
        return test, None
    except ValueError:
        return None, {'msg': 'Some parameters are missing'}


def get_test(test_id):
    """
        get specific test from test_id
    """
    try:
        return Test.objects.get(pk=test_id), None
    except ObjectDoesNotExist:
        return None, {'msg': 'Test not found'}
