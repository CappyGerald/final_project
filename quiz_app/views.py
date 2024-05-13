from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Question, Answer

def select_topic(request):
    topics = Topic.objects.all()
    return render(request, 'select_topic.html', {'topics': topics})
    
def ask_questions(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    questions = Question.objects.filter(topic=topic)
    return render(request, 'ask_questions.html', {'questions': questions})

def check_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        user_answer = request.POST.get('user_answer')
        
        # Checking if user_answer is empty or None
        if not user_answer:
            return render(request, 'answer_feedback.html', {'message': 'Please provide an answer.'})
        
        question = get_object_or_404(Question, pk=question_id)
        all_answers = Answer.objects.filter(question=question)
        
        # Finding the correct answer from all_answers
        correct_answer = next((ans for ans in all_answers if ans.is_correct), None)
        print(f"Question ID: {question_id}")
        print(f"User Answer: {user_answer}")
        print(f"All Answers: {all_answers}")
        print(f"Correct Answer: {correct_answer}")

        if correct_answer and user_answer.lower() == correct_answer.answer.lower():
            message = 'Congratulations! Correct answer!'
        else:
            message = f'Incorrect! The correct answer is {correct_answer.answer if correct_answer else "unknown"}'

        return render(request, 'answer_feedback.html', {'message': message})
    return redirect('select_topic')
