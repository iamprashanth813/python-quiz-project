def run_quiz():

  questions = [

    {
      "question": "What is the capital of France?",
      "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome" ],
      "answer": "C"
    },

    {
      "question": "What is 2 + 2?",
      "options": ["A) 3", "B) 4", "C) 5", "D) 6" ],
      "answer": "B"
    },

    {
      "question": "What is the largest planet in our solar system?",
      "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars" ],
      "answer": "B"
    },

    {
      "question": "Who wrote 'Hamlet'?",
      "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen" ],
      "answer": "C"
    }

  ]

  score = 0

  for index, q in enumerate(questions):
    print(f"Q{index + 1}: {q['question']}")
    for option in q['options']:
      print(option)

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q['answer']:
      print("Correct!\n")
      score += 1

  print(f"Your final score is {score}/{len(questions)}")
    
run_quiz()