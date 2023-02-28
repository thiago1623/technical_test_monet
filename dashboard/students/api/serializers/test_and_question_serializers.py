from students.models import Test, Question, Answer
from ..serializers.user_serializer import ParentModelSerializer, UserSerializer


class AnswerSerializer(ParentModelSerializer):

    class Meta:
        model = Answer
        fields = ('pk', 'text', 'order', 'is_correct', 'created_at')

    @staticmethod
    def process(answer, **kwargs):
        return answer


class QuestionSerializer(ParentModelSerializer):
    all_answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ('pk', 'text', 'all_answers', 'order', 'created_at')

    @staticmethod
    def process(question, **kwargs):
        question.all_answers = [AnswerSerializer(ans).data for ans in question.answers.all()]
        return question


class TestSerializer(ParentModelSerializer):
    all_questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Test
        fields = ('pk', 'name', 'all_questions', 'created_at')

    @staticmethod
    def process(test, **kwargs):
        test.all_questions = [QuestionSerializer(question).data for question in test.questions.all()]
        return test
