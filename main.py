
class Quiz:
    def __init__(self, question, choices, answer, explanation):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.explanation = explanation

def create_default_quizzes():
    return [
        Quiz(
            "탄수화물 1g은 몇 kcal의 에너지를 제공할까요?",
            ["2 kcal", "4 kcal", "7 kcal", "9 kcal"],
            2,
            "탄수화물은 1g당 약 4 kcal의 에너지를 제공합니다."
        ),
        Quiz(
            "단백질을 구성하는 기본 단위는 무엇일까요?",
            ["지방산", "포도당", "아미노산", "글리세롤"],
            3,
            "단백질은 아미노산이 연결되어 만들어집니다."
        ),
        Quiz(
            "지방 1g은 몇 kcal의 에너지를 제공할까요?",
            ["4 kcal", "5 kcal", "7 kcal", "9 kcal"],
            4,
            "지방은 1g당 약 9 kcal의 에너지를 제공합니다."
        ),
        Quiz(
            "비타민 C가 풍부한 과일은 무엇일까요?",
            ["오렌지", "쌀", "달걀", "식빵"],
            1,
            "오렌지와 같은 감귤류 과일에는 비타민 C가 풍부합니다."
        ),
        Quiz(
            "뼈와 치아를 구성하는 데 중요한 무기질은 무엇일까요?",
            ["철분", "칼슘", "나트륨", "요오드"],
            2,
            "칼슘은 뼈와 치아를 구성하고 유지하는 데 중요한 무기질입니다."
        )
    ]

def play_quiz(quizzes):
    score = 0

    print("\n===== 영양학 퀴즈 시작 =====")

    for number, quiz in enumerate(quizzes, start=1):
        print(f"\n문제 {number}. {quiz.question}")

        for index, choice in enumerate(quiz.choices, start=1):
            print(f"{index}. {choice}")

        while True:
            try:
                answer = int(input("정답 번호를 입력하세요 (1~4): "))

                if 1 <= answer <= 4:
                    break
                else:
                    print("1~4 사이의 숫자를 입력해 주세요.")

            except ValueError:
                print("숫자로 입력해 주세요.")

        if answer == quiz.answer:
            print("정답입니다!")
            score += 1
        else:
            print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(f"해설: {quiz.explanation}")

    print("\n===== 퀴즈 결과 =====")
    print(f"총 {len(quizzes)}문제 중 {score}문제를 맞혔습니다.")

def show_quiz_list(quizzes):
    print("\n===== 영양학 퀴즈 목록 =====")

    for number, quiz in enumerate(quizzes, start=1):
        print(f"{number}. {quiz.question}")

    print(f"\n현재 등록된 퀴즈: {len(quizzes)}개")

def add_quiz():
    print("\n===== 새 퀴즈 추가하기 =====")

    question = input("문제를 입력하세요: ").strip()

    while not question:
        print("문제는 비워둘 수 없습니다.")
        question = input("문제를 입력하세요: ").strip()

    choices = []

    for number in range(1, 5):
        choice = input(f"{number}번 보기 입력: ").strip()

        while not choice:
            print("보기는 비워둘 수 없습니다.")
            choice = input(f"{number}번 보기 입력: ").strip()

        choices.append(choice)

    while True:
        try:
            answer = int(input("정답 번호를 입력하세요 (1~4): "))

            if 1 <= answer <= 4:
                break
            else:
                print("1~4 사이의 숫자를 입력해 주세요.")

        except ValueError:
            print("숫자로 입력해 주세요.")

    explanation = input("정답 해설을 입력하세요: ").strip()

    while not explanation:
        print("해설은 비워둘 수 없습니다.")
        explanation = input("정답 해설을 입력하세요: ").strip()

    new_quiz = Quiz(question, choices, answer, explanation)

    print("\n새 퀴즈가 만들어졌습니다!")

    return new_quiz



def show_menu():
    print("\n===== 나의 영양 퀴즈 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가하기")
    print("3. 퀴즈 목록 보기")
    print("4. 최고 점수 보기")
    print("5. 종료하기")




def main():
    print("영양학 퀴즈 프로그램에 오신 것을 환영합니다!")

    quizzes = create_default_quizzes()

    while True:
        show_menu()
        choice = input("메뉴를 선택하세요 (1~5): ").strip()

        if choice == "1":
            play_quiz(quizzes)

        elif choice == "2":
            new_quiz = add_quiz()
            quizzes.append(new_quiz)
            print("\n퀴즈가 목록에 추가되었습니다!")
        
        elif choice == "3":
            show_quiz_list(quizzes)

        elif choice == "4":
            print("\n[최고 점수 보기] 기능은 준비 중입니다.")

        elif choice == "5":
            print("\n영양학 퀴즈 프로그램을 종료합니다.")
            break

        else:
            print("\n잘못된 입력입니다. 1~5 사이의 숫자를 입력해 주세요.")


if __name__ == "__main__":
    main()




