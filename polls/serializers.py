from rest_framework import serializers
from polls.models import User
#class UserSerializer(serializers.Serializer):
#    pk=serializers.IntegerField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', )

class DetailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('pk','username','answar_set',)

class ChoiceSerializer(serializers.Serializer):
    title=serializers.CharField()
    
class AnswerSerializer(serializers.Serializer):
    user=UserSerializer()#many=True,read_only=True, source='pk_set')
    choice=ChoiceSerializer()

class QuestionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=4096)
    ques_type = serializers.CharField(max_length=5)
    end_date = serializers.DateTimeField()
    #choices=ChoiceSerializer(many=True,read_only=True, source='choice_set')
    answer=AnswerSerializer(many=True,read_only=True, source='answer_set')
    user_ans=AnswerSerializer(many=True,read_only=True, source='user')
    #users=UserSerializer(many=True,read_only=True, source='user_set')


