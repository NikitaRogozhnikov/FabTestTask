from django.urls import path
from . import views 
app_name = "polls"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.MainView.as_view(), name="main"),
    path('<int:qid>', views.DetailView.as_view(), name="detail"),
    path('new', views.NewQuestionView.as_view(), name="new"),
    path('login',views.LoginView.as_view(),name='login'),
    path('logout',views.logout_user,name='logout'),
    path('register', views.RegisterView.as_view(),name='register'),
    path('text',views.text_question, name="text"),
    path('cb',views.cb_question, name="cb"),
    path('rb',views.rb_question, name="rb"),
    path('apiget',views.PollsView.as_view(), name="apiget"),
    path('apiget/<int:pk>',views.DetailPolsView.as_view()),
]