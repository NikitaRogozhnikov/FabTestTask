from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import  ListAPIView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError 
# Create your views here.
from .models import Question, Choice, Answer
from .serializers import *
import pytz
from datetime import datetime

class PollsView(APIView):


    def get(self,request):
        questions=Question.objects.all()
        choices=Choice.objects.all()
        q_serializer=QuestionSerializer(questions,many=True)
        #c_serializer=ChoiceSerializer(choices)
        return Response({"questions":q_serializer.data})

    
class MainView(TemplateView):
    utc=pytz.UTC
    template_name = "polls/main.html"
    def dispatch(self, request):
        context={}
        new_ques=[x for x in Question.objects.all() if x.end_date > datetime.now(tz=self.utc)]
        if request.user.is_authenticated:
            questions_set=set(new_ques)
            user_answers_set=set([ans.question for ans in request.user.answer_set.all()])
            not_answered_questions=list(questions_set.difference(user_answers_set))
            context['questions']=not_answered_questions

        else:
            context['questions']=new_ques
        print(context)
        return render(request,self.template_name,context=context)

class DetailView(TemplateView):
    
    template_name = "polls/detail.html"
    def dispatch(self, request,qid):
        question=Question.objects.get(pk=int(qid))
        context={'ques_type':question.ques_type,'title':question.title,'ques':question}
        if request.method=='POST':
            try:
                request.POST['anon']
                user=User.objects.get(username='Anonymous')
            except:
                user=request.user
                
            try:
                answers_list=dict(request.POST.lists())['answer']
                print(answers_list)

            except:
                context['error']="Вы не выбрали ответ"
                return render(request,self.template_name,context=context)
            if question.ques_type=='text':
                for ans in answers_list:
                    ch=Choice(question=question,title=ans)
                    ch.save()
                    answer=Answer(user=user,question=question,choice=ch)
                    answer.save()
            else:
                for ans in answers_list:
                    answer=Answer(user=user,question=question,choice=question.choice_set.filter(title=ans).get())
                    answer.save()
            return redirect("/api")
        return render(request,self.template_name,context=context)



class NewQuestionView(TemplateView):
    template_name='polls/new.html'
    def dispatch(self,request):
        if request.method=='POST':
            print(request.POST.lists())
        return render (request, self.template_name)


def text_question(request):
    if request.method=="POST":
        ques=Question(title=request.POST['question'],ques_type=Question.TEXT)
        ques.save()
        return redirect("/api")
    return render(request,'polls/textq.html')

def cb_question(request):
    if request.method=="POST":
        ques=Question(title=request.POST['question'],ques_type=Question.CHECK)   
        print(request.POST)
        ques.save()
        answers_list=dict(request.POST.lists())['answer']
        for ans in answers_list:
            choise=Choice(title=ans, question=ques)
            choise.save()
        
        return redirect("/api")
    return render(request,'polls/cbq.html')

def rb_question(request):
    if request.method=="POST":
        ques=Question(title=request.POST['question'],ques_type=Question.RADIO)   
        print(request.POST)
        ques.save()
        answers_list=dict(request.POST.lists())['answer']
        for ans in answers_list:
            choise=Choice(title=ans, question=ques)
            choise.save()
        
        return redirect("/api")
    return render(request,'polls/cbq.html')

def logout_user(request):
    logout(request)
    return redirect('/api')

class RegisterView(TemplateView):
    template_name = "polls/register.html"

    def dispatch(self, request, *args, **kwargs):
        
        context = {}
        
        if request.method == 'POST':
            usrname = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']        
            if password == password2:
                try:
                    User.objects.create_user(usrname, email, password)
                    login(request, authenticate(request,username=usrname,password=password))
                    return redirect("/api")
                except IntegrityError:
                    context['error'] = "Такой пользователь уже существует"
                    return render(request, self.template_name,context)
            else:
                context['error']="Пароли не совпадают"
        return render(request, self.template_name,context)

class LoginView(TemplateView):
    template_name = "polls/login.html"
    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect("/api")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context) 