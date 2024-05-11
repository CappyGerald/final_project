from django.shortcuts import render
from .models import Topic,  Question, Answer
# Create your views here.

def select_topic(request):
    topics = opic.object.all()
    return render(request, 'select_topic.html', {'topics': topics})
    
def ask_questions(request, question_id):
    topic = Topic.objects.get(pk=topic_id)
    questions = Question.objects.filter(topic=topic)
    return render(request, 'ask_questions.html', {'questions': questions})

def check_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        user_answer = request.POST.get('user_answer')
        question = Question.objects.get(pk=question)
        correct_answer = question.answer_set.filter(is_correct=True).first()

        if user_answer.lower() == correct_answer.text.lower():
            message = 'Congratulations! Correct answer!'
        else:
            message = f'Incorrect! The correct answer is {correct_answer.text}'
        return render(request, 'answer_feedback.html', {'message': message})
    return redirect('select_topic')