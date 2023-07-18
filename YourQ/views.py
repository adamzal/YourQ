from django.shortcuts import render
from quizzes.models import Quiz
from questions.models import Question
from users.models import YourQUser

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def allquizzes(request):
    all_quizzes = Quiz.objects.all()
    return render(request, 'allquizzes.html', {'all_quizzes': all_quizzes})

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password, model=YourQUser)

        if user.is_active:            
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:        
        return render(request, 'signin.html', {})

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def myquizzes(request):
    my_quizzes = Quiz.objects.filter(author=request.user)
    my_quizzes_count = my_quizzes.count()
    return render(request, 'myquizzes.html', {'my_quizzes': my_quizzes, 'my_quizzes_count':my_quizzes_count})

def profile(request):
    return render(request, 'profile.html')

def createquiz(request):
    return render(request, 'createquiz.html')

def createquiz_status(request):
    try:
        if request.method == 'POST':
            form = request.POST

            quiz = Quiz(name = form['quiz_name'], author = request.user)     
            quiz.save()

            question_number = 1                 
            while form.get(f'question_text_{question_number}')!=None:
                text = form.get(f'question_text_{question_number}')
                answer_a = form.get(f'answer_A_{question_number}')
                answer_b = form.get(f'answer_B_{question_number}')
                answer_c = form.get(f'answer_C_{question_number}')
                answer_d = form.get(f'answer_D_{question_number}')
                correct_answer = form.get(f'correct_answer_{question_number}')

                question = Question(quiz = quiz, text = text, answer_a = answer_a, answer_b = answer_b, answer_c = answer_c, answer_d = answer_d, correct_answer = correct_answer)                   
                question.save() 

                question_number+=1                           

        return render(request, 'createquiz-status.html', {'type':'OK', 'error_message': ''})
    except NameError:
        return render(request, 'createquiz-status.html', {'type':'ERROR', 'error_message': 'f{NameError}'})


def playquiz(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)   
    questions = Question.objects.filter(quiz=quiz)
    quiz.views+=1
    quiz.save()
    return render(request, 'playquiz.html', {'quiz': quiz, 'questions' : questions})

def playquiz_status(request, quiz_id):
    if request.method == 'POST':
        form = request.POST
        quiz = Quiz.objects.get(pk=quiz_id)   
        questions = Question.objects.filter(quiz=quiz)
        quiz.execute+=1
        quiz.save()

        checked_answers = []
        number_of_good_answers = 0         

        for question in questions:            
            checked_answers.append(form.get(f'question_radio_{question.pk}'))
            if question.correct_answer == form.get(f'question_radio_{question.pk}'):
                number_of_good_answers+=1
        number_of_all_answers = len(checked_answers)                            
    return render(request, 'playquiz-status.html', {'quiz':quiz, 'questions_checked_answers': zip(questions, checked_answers), 'number_of_good_answers':number_of_good_answers, 'number_of_all_answers':number_of_all_answers})

def editquiz(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)    
    questions = Question.objects.filter(quiz=quiz)
    numbers = range(1,len(questions)+1)
    return render(request, 'editquiz.html', {'quiz': quiz, 'questions' : zip(questions, numbers)})

def editquiz_confirm(request, quiz_id):
    if request.method == 'POST':
            form = request.POST

            quiz = Quiz.objects.get(pk=quiz_id)
            questions = Question.objects.filter(quiz = quiz)                   
            
            cheanched_questions=[]

            question_number = 1            
            while form.get(f'question_text_{question_number}')!=None:
                text = form.get(f'question_text_{question_number}')
                answer_a = form.get(f'answer_A_{question_number}')
                answer_b = form.get(f'answer_B_{question_number}')
                answer_c = form.get(f'answer_C_{question_number}')
                answer_d = form.get(f'answer_D_{question_number}')
                correct_answer = form.get(f'correct_answer_{question_number}')

                cheanched_questions.append(Question(quiz = quiz, text = text, answer_a = answer_a, answer_b = answer_b, answer_c = answer_c, answer_d = answer_d, correct_answer = correct_answer))

                question_number+=1
            
    return render(request, 'editquiz-confirm.html', {'quiz': quiz, 'questions':zip(questions, cheanched_questions), 'cheanged_quiz_name':form['quiz_name']})

def editquiz_status(request, quiz, questions):
    try:


        return render(request, 'createquiz-status.html', {'type':'OK', 'error_message': ''})
    except NameError:
        return render(request, 'createquiz-status.html', {'type':'ERROR', 'error_message': 'f{NameError}'})


def deletequiz_confirm(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'deletequiz-confirm.html', {'quiz': quiz, 'questions':questions})

def deletequiz_status(request, quiz_id):
    quiz = Quiz.objects.filter(pk=quiz_id)
    if len(quiz)>0:
        quiz.delete()
        return render(request, 'deletequiz-status.html',{'type':'OK'})
    else:
        return render(request, 'deletequiz-status.html',{'type':'ERROR'})