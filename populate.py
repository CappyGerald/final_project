import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
django.setup()

from quiz_app.models import Topic, Question, Choice

# Define the topics, questions, answers, and choices
topics_data = [
    {
        "name": "History",
        "questions": [
            {
                "text": "As recently dramatized in a critically acclaimed miniseries, what year did the Chernobyl disaster occur?",
                "correct_answer": "1986",
                "choices": ["1986", "1987", "1988", "1989"]
            },
            {
                "text": "Who was Lord Mayor of London four times between 1397 and 1419 and the inspiration for a classic English folk tale?",
                "correct_answer": "Richard (Dick) Whittington",
                "choices": ["Richard (Dick) Whittington", "Thomas Becket", "Geoffrey Chaucer", "William Shakespeare"]
            },
            {
                "text": "Who was the second President of the United States?",
                "correct_answer": "John Adams",
                "choices": ["John Adams", "Thomas Jefferson", "George Washington", "James Madison"]
            },
            {
                "text": "Which British archaeologist discovered Tutankhamun's tomb?",
                "correct_answer": "Howard Carter",
                "choices": ["Howard Carter", "Arthur Evans", "Gertrude Bell", "Zahi Hawass"]
            },
            {
                "text": "Who was the leader of Britain's ill-fated Antarctic expedition that was one of the first to reach the South Pole in 1912?",
                "correct_answer": "Robert Falcon Scott",
                "choices": ["Robert Falcon Scott", "Ernest Shackleton", "Roald Amundsen", "Douglas Mawson"]
            },
            {
                "text": "In which European country was there a civil war between 1946 and 1949?",
                "correct_answer": "Greece",
                "choices": ["Greece", "Spain", "Italy", "France"]
            },
            {
                "text": "Which 13th-century Scottish knight did Mel Gibson portray in 'Braveheart'?",
                "correct_answer": "William Wallace",
                "choices": ["William Wallace", "Robert the Bruce", "James Douglas", "Andrew Moray"]
            },
            {
                "text": "Which war was fought in South Africa between 1899 and 1902?",
                "correct_answer": "Anglo-Boer War",
                "choices": ["Anglo-Boer War", "Zulu War", "World War I", "World War II"]
            },
            {
                "text": "In which country did the Second World War Battles of El Alamein take place?",
                "correct_answer": "Egypt",
                "choices": ["Egypt", "Libya", "Tunisia", "Algeria"]
            },
            {
                "text": "Who discovered the wreckage of the Titanic?",
                "correct_answer": "Robert Ballard",
                "choices": ["Robert Ballard", "James Cameron", "Jacques Cousteau", "David Attenborough"]
            }
        ]
    },
    {
        "name": "Python",
        "questions": [
            {
                "text": "Who developed the Python programming language?",
                "correct_answer": "Guido van Rossum",
                "choices": ["Guido van Rossum", "James Gosling", "Dennis Ritchie", "Bjarne Stroustrup"]
            },
            {
                "text": "Which type of programming does Python support?",
                "correct_answer": "All of the mentioned",
                "choices": ["Procedural", "Object-oriented", "Functional", "All of the mentioned"]
            },
            {
                "text": "Is Python case-sensitive when dealing with identifiers?",
                "correct_answer": "Yes",
                "choices": ["Yes", "No"]
            },
            {
                "text": "What is the correct extension for Python files?",
                "correct_answer": ".py",
                "choices": [".py", ".python", ".pt", ".p"]
            },
            {
                "text": "Is Python code compiled or interpreted?",
                "correct_answer": "Python code is both compiled and interpreted",
                "choices": ["Compiled", "Interpreted", "Python code is both compiled and interpreted", "None of the mentioned"]
            },
            {
                "text": "What are all the keywords in Python written in?",
                "correct_answer": "Lowercase",
                "choices": ["Uppercase", "Lowercase", "Capitalized", "None of the mentioned"]
            },
            {
                "text": "What will be the output of 4 + 3 % 5?",
                "correct_answer": "7",
                "choices": ["7", "2", "4", "1"]
            },
            {
                "text": "Which keyword is used for defining a block of code in Python?",
                "correct_answer": "Indentation",
                "choices": ["Indentation", "Key", "Block", "Def"]
            },
            {
                "text": "Which function is used for creating anonymous functions at runtime?",
                "correct_answer": "lambda",
                "choices": ["lambda", "def", "func", "anonymous"]
            },
            {
                "text": "What does 'pip' stand for in Python?",
                "correct_answer": "Pip Installs Packages",
                "choices": ["Pip Installs Packages", "Python Installation Pack", "Pip Installs Python", "Packages in Python"]
            }
        ]
    },
    {
        "name": "Geography",
        "questions": [
            {
                "text": "What is the only country that borders the United Kingdom?",
                "correct_answer": "Ireland",
                "choices": ["Ireland", "France", "Belgium", "Netherlands"]
            },
            {
                "text": "Ninety percent of the Earth's population lives in which hemisphere?",
                "correct_answer": "The Northern Hemisphere",
                "choices": ["The Northern Hemisphere", "The Southern Hemisphere", "The Western Hemisphere", "The Eastern Hemisphere"]
            },
            {
                "text": "In which country would you find the city of Dresden?",
                "correct_answer": "Germany",
                "choices": ["Germany", "Austria", "Switzerland", "Poland"]
            },
            {
                "text": "What would you call someone from Sudan?",
                "correct_answer": "Sudanese",
                "choices": ["Sudanese", "Sudanian", "Sudanish", "Sudar"]
            },
            {
                "text": "What are the names of South Africa's three capital cities?",
                "correct_answer": "Cape Town, Pretoria, and Bloemfontein",
                "choices": ["Cape Town, Pretoria, and Bloemfontein", "Johannesburg, Pretoria, and Durban", "Cape Town, Johannesburg, and Durban", "Pretoria, Durban, and Bloemfontein"]
            },
            {
                "text": "How many large islands make up Hawaii?",
                "correct_answer": "Eight",
                "choices": ["Eight", "Seven", "Six", "Nine"]
            },
            {
                "text": "In which U.S. state can the world's tallest trees be found?",
                "correct_answer": "California",
                "choices": ["California", "Oregon", "Washington", "Nevada"]
            },
            {
                "text": "What is the name of the highest uninterrupted waterfall in the world?",
                "correct_answer": "Angel Falls",
                "choices": ["Angel Falls", "Niagara Falls", "Victoria Falls", "Yosemite Falls"]
            },
            {
                "text": "Which river flows through the Grand Canyon?",
                "correct_answer": "Colorado River",
                "choices": ["Colorado River", "Mississippi River", "Missouri River", "Rio Grande"]
            },
            {
                "text": "What is the largest ocean in the world?",
                "correct_answer": "Pacific Ocean",
                "choices": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]
            }
        ]
    }
]

# Populating the database with topics, questions, and choices
for topic_data in topics_data:
    topic_obj, created = Topic.objects.get_or_create(name=topic_data["name"])
    if created:
        print(f"Created topic: {topic_obj}")

    for question_data in topic_data["questions"]:
        question_text = question_data["text"]
        correct_answer = question_data["correct_answer"]
        choices = question_data["choices"]

        # Checking if the question already exists for this topic
        existing_questions = Question.objects.filter(topic=topic_obj, text=question_text)
        if existing_questions.exists():
            question_obj = existing_questions.first()
            print(f"Question already exists: {question_obj}")
        else:
            question_obj = Question.objects.create(topic=topic_obj, text=question_text)
            print(f"Created question: {question_obj}")

        for choice_text in choices:
            is_correct = (choice_text == correct_answer)
            # Checking if the choice already exists for this question
            existing_choices = Choice.objects.filter(question=question_obj, choice_text=choice_text)
            if existing_choices.exists():
                choice_obj = existing_choices.first()
                print(f"Choice already exists: {choice_obj}")
            else:
                choice_obj = Choice.objects.create(question=question_obj, choice_text=choice_text, is_correct=is_correct)
                print(f"Created choice: {choice_obj}")
