class User:
    def __init__(self, name, user_type):
        self.name = name
        self.user_type = user_type


class Student(User):
    def __init__(self, name, student_id):
        super().__init__(name, "Student")
        self.student_id = student_id
        self.parents = []  # Add a list to store parents

class Teacher(User):
    def __init__(self, name, teacher_id):
        super().__init__(name, "Teacher")
        self.teacher_id = teacher_id

class Parent(User):
    def __init__(self, name, student_name):
        super().__init__(name, "Parent")
        self.student_name = student_name

class Quiz:
    def __init__(self, quiz_id, teacher):
        self.quiz_id = quiz_id
        self.teacher = teacher
        self.participants = {}
        self.questions = []
        self.results = {}

    def add_question(self, question, answer):
        self.questions.append({"question": question, "answer": answer})

    def invite_participant(self, participant):
        if isinstance(participant, Student):
            self.participants[participant.student_id] = participant
        elif isinstance(participant, Parent):
            student_id = None
            for student in self.participants.values():
                if student.name == participant.student_name:
                    student_id = student.student_id
                    break
            if student_id:
                self.participants[student_id].parents.append(participant)

    def take_quiz(self):
            if not self.questions:
                raise ValueError("No questions added to the quiz.")
    
            for student_id in self.participants:
                # Initialize the score for the current student
                self.results[student_id] = {"score": 0, "answers": []}
                self.current_student_id = student_id
    
                for question_data in self.questions:
                    question = question_data["question"]
                    correct_answer = question_data["answer"]
    
                    # Display the question
                    print(f"Question: {question}")
    
                    # Take input for the answer
                    user_answer = input("Your answer: ")
    
                    # Check if the answer is correct
                    if user_answer.strip().lower() == correct_answer.strip().lower():  # Ignore case and leading/trailing spaces
                        print("Correct!\n")
                        self.results[student_id]["score"] += 1
                    else:
                        print(f"Wrong! The correct answer is: {correct_answer}\n")
    
                    # Store the user's answer
                    self.results[student_id]["answers"].append((question, user_answer))


class QuizManagementSystem:
    def __init__(self):
        self.quizzes = {}

    def create_quiz(self, quiz_id, teacher):
        if quiz_id in self.quizzes:
            raise ValueError("Quiz ID already exists.")
        quiz = Quiz(quiz_id, teacher)
        self.quizzes[quiz_id] = quiz
        return quiz

    def get_quiz_results(self, quiz_id):
        if quiz_id in self.quizzes:
            return self.quizzes[quiz_id].results
        else:
            raise ValueError("Quiz not found.")

# ... (Previous code)

if __name__ == "__main__":
    # Instantiate users
    student1 = Student("Alice", "S001")
    teacher1 = Teacher("Mr. Smith", "T001")
    parent1 = Parent("John", "Alice")

    # Create a quiz management system
    quiz_system = QuizManagementSystem()

    # Create a quiz
    quiz1 = quiz_system.create_quiz("Q001", teacher1)

    # Add questions to the quiz
    quiz1.add_question("What is the capital of France?", "paris")
    quiz1.add_question("What is 2 + 2?", "4")
    quiz1.add_question("Who wrote the play 'Romeo and Juliet'?", "william shakespeare")
    quiz1.add_question("Which planet is known as the 'Red Planet'?", "mars")
    quiz1.add_question("What is the chemical symbol for gold?", "au")

    # Invite participants
    quiz1.invite_participant(student1)
    quiz1.invite_participant(parent1)

    # Take the quiz for each participant
    quiz1.take_quiz()

    # Get and display quiz results
    results = quiz_system.get_quiz_results("Q001")
    
    for student_id, data in results.items():
        print(f"{student_id}: Score - {data['score']}/{len(quiz1.questions)}")
        print("Answers:")
        for question, user_answer in data["answers"]:
            print(f"Question: {question}")
            print(f"Your answer: {user_answer}")
            correct_answer = next(q["answer"] for q in quiz1.questions if q["question"] == question)
            print(f"Correct answer: {correct_answer}\n")
4




