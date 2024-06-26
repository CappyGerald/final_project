from django.shortcuts import render, get_object_or_404
from .models import Topic, Question, Choice, UserQuizAttempt
from .forms import QuizForm


def select_topic(request):
    topics = Topic.objects.all()
    return render(request, 'select_topic.html', {'topics': topics})
def ask_questions(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    questions = Question.objects.filter(topic=topic)

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            results = []
            score = 0
            for question in questions:
                selected_choice_id = form.cleaned_data[f"question_{question.id}"]
                selected_choice = Choice.objects.get(id=selected_choice_id)
                is_correct = selected_choice.is_correct
                correct_choice = question.choices.get(is_correct=True)
                results.append((question, selected_choice,is_correct, correct_choice))
                if selected_choice.is_correct:
                    score += 1
                #results.append((question, selected_choice, is_correct, correct_choice))
            UserQuizAttempt.objects.create(topic=topic, score=score)

            return render(request, 'quiz_result.html', {'questions': questions, 'results': results, 'score': score})
    else:
        form = QuizForm(questions=questions)
        
    return render(request, 'ask_questions.html', {'form': form, 'topic': topic})
def quiz_result(request):
    return render(request, 'quiz_result.html')