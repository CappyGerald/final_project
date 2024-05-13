import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plp_final.settings')
django.setup()

from quiz_app.models import Topic, Question, Answer

# Define the topics, questions, and answers
topics_data = [
    {
        "name": "History",
        "questions": [
            "As recently dramatized in a critically acclaimed miniseries, what year did the Chernobyl disaster occur?",
            "Who was Lord Mayor of London four times between 1397 and 1419 and the inspiration for a classic English folk tale?",
            # Add more questions as needed
        ],
        "answers": [
            "1986",
            "Richard (Dick) Whittington",
            # Add corresponding answers
        ]
    },
    {
        "name": "Python",
        "questions": [
            "Who developed the Python programming language?",
            "Which type of programming does Python support?",
            # Add more questions as needed
        ],
        "answers": [
            "Guido van Rossum",
            "All of the mentioned",
            # Add corresponding answers
        ]
    },
    {
        "name": "Geography",
        "questions": [
            "What is the only country that borders the United Kingdom?",
            "Ninety percent of the Earth's population lives in which hemisphere?",
            # Add more questions as needed
        ],
        "answers": [
            "Ireland",
            "The Northern Hemisphere",
            # Add corresponding answers
        ]
    },
]

# Populate the database with topics, questions, and answers
for topic_data in topics_data:
    topic_obj, created = Topic.objects.get_or_create(name=topic_data["name"])
    if created:
        print(f"Created topic: {topic_obj}")

    for question_text, answer_text in zip(topic_data["questions"], topic_data["answers"]):
        question_obj, created = Question.objects.get_or_create(topic=topic_obj, text=question_text)
        if created:
            print(f"Created question: {question_obj}")

        answer_obj, created = Answer.objects.get_or_create(question=question_obj, text=answer_text)
        if created:
            print(f"Created answer: {answer_obj}")

print("Data population complete.")
