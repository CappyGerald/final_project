import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
django.setup()

from quiz_app.models import Topic, Question, Answer

# Define the topics, questions, and answers
topics_data = [
    {
        "name": "History",
        "questions": [
            "As recently dramatized in a critically acclaimed miniseries, what year did the Chernobyl disaster occur?",
            "Who was Lord Mayor of London four times between 1397 and 1419 and the inspiration for a classic English folk tale?",
            "Who was the second President of the United States?",
            "Which British archaeologist discovered Tutankhamun's tomb?",
            "Who was the leader of Britain's ill-fated Antarctic expedition that was one of the first to reach the South Pole in 1912?",
            "In which European country was there a civil war between 1946 and 1949?",
            "Which 13th-century Scottish knight did Mel Gibson portray in 'Braveheart'?",
            "Which war was fought in South Africa between 1899 and 1902?",
            "In which country did the Second World War Battles of El Alamein take place?",
            "Who discovered the wreckage of the Titanic?"
        ],
        "answers": [
            "1986",
            "Richard (Dick) Whittington",
            "John Adams",
            "Howard Carter",
            "Robert Falcon Scott",
            "Greece",
            "William Wallace",
            "Anglo-Boer War",
            "Egypt",
            "Robert Ballard"
        ]
    },
    {
        "name": "Python",
        "questions": [
            "Who developed the Python programming language?",
            "Which type of programming does Python support?",
            "Is Python case-sensitive when dealing with identifiers?",
            "What is the correct extension for Python files?",
            "Is Python code compiled or interpreted?",
            "What are all the keywords in Python written in?",
            "What will be the output of 4 + 3 % 5?",
            "Which keyword is used for defining a block of code in Python?",
            "Which function is used for creating anonymous functions at runtime?",
            "What does 'pip' stand for in Python?"
        ],
        "answers": [
            "Guido van Rossum",
            "All of the mentioned",
            "Yes",
            ".py",
            "Python code is both compiled and interpreted",
            "Capitalized",
            "7",
            "Indentation",
            "lambda",
            "Pip Installs Packages"
        ]
    },
    {
        "name": "Geography",
        "questions": [
            "What is the only country that borders the United Kingdom?",
            "Ninety percent of the Earth's population lives in which hemisphere?",
            "In which country would you find the city of Dresden?",
            "In which country would you find the city of Dresden?",
            "What would you call someone from Sudan?",
            "What are the names of South Africa's three capital cities?",
            "How many large islands make up Hawaii?",
            "In which U.S. state can the world's tallest trees be found?",
            "What is the name of the highest uninterrupted waterfall in the world?",
            "Which river flows through the Grand Canyon?",
            "What is the largest ocean in the world?"
        ],
        "answers": [
            "Ireland",
            "The Northern Hemisphere",
            "The Northern Hemisphere",
            "Germany",
            "Sudanese",
            "Cape Town, Pretoria, and Bloemfontein",
            "Eight",
            "California",
            "Angel Falls",
            "Colorado River",
            "Pacific Ocean"
        ]
    },
]

# Populating the database with topics, questions, and answers
for topic_data in topics_data:
    topic_obj, created = Topic.objects.get_or_create(name=topic_data["name"])
    if created:
        print(f"Created topic: {topic_obj}")

    for question_text, answer_text in zip(topic_data["questions"], topic_data["answers"]):
        # Checking if the question already exists for this topic
        existing_questions = Question.objects.filter(topic=topic_obj, text=question_text)
        if existing_questions.exists():
            question_obj = existing_questions.first()
            print(f"Question already exists: {question_obj}")
        else:
            question_obj = Question.objects.create(topic=topic_obj, text=question_text)
            print(f"Created question: {question_obj}")

        # Converting answer to lowercase for consistency
        answer_text_lower = answer_text.lower()
        # Checking if the answer already exists for this question
        existing_answers = Answer.objects.filter(question=question_obj, answer=answer_text_lower, is_correct=True)
        if existing_answers.exists():
            answer_obj = existing_answers.first()
            print(f"Answer already exists: {answer_obj}")
        else:
            answer_obj = Answer.objects.create(question=question_obj, answer=answer_text_lower, is_correct=True)
            print(f"Created answer: {answer_obj}")

