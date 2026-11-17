import json
import os
import random
class Quiz:
    def __init__(self, question, choices, answer, explanation):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.explanation = explanation



class QuizGame:
    def __init__(self):
        self.best_score = 0
        self.can_save = True
        self.quizzes = self.load_state()

    def load_state(self):
        if os.path.exists("state.json"):
            try:
                with open("state.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
                if not isinstance(data, dict):
                     raise TypeError("저장 데이터 형식이 올바르지 않습니다.")

                self.best_score = data.get("best_score", 0)

                saved_quizzes = data.get("quizzes", [])

                if saved_quizzes:
                    quizzes = []

                    for item in saved_quizzes:
                        quiz = Quiz(
                            item["question"],
                            item["choices"],
                            item["answer"],
                            item["explanation"]
                        )
                        quizzes.append(quiz)

                    return quizzes

                return self.create_default_quizzes()

            except (json.JSONDecodeError, OSError, KeyError, TypeError, ValueError):
                print("저장 파일을 읽을 수 없어 기본 데이터로 시작합니다.")
                self.can_save = False
                self.best_score = 0
                return self.create_default_quizzes()

        return self.create_default_quizzes()

    
    def save_state(self):
        if not self.can_save:
            print("저장 파일 보호를 위해 저장을 건너뜁니다.")
            return


        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                    "explanation": quiz.explanation
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score
        }

        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("데이터가 저장되었습니다.")

        except OSError:
            print("데이터 저장에 실패했습니다.")



    def create_default_quizzes(self):
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

    def play_quiz(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        score = 0

        print("\n===== 영양학 퀴즈 시작 =====")

        shuffled_quizzes = self.quizzes.copy()
        random.shuffle(shuffled_quizzes)

        for number, quiz in enumerate(shuffled_quizzes, start=1):
            print(f"\n문제 {number}. {quiz.question}")

            for index, choice in enumerate(quiz.choices, start=1):
                print(f"{index}. {choice}")

            while True:
                try:
                    answer = int(input("정답 번호를 입력하세요 (1~4): "))

                    if 1 <= answer <= 4:
                        break

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
        print(f"총 {len(self.quizzes)}문제 중 {score}문제를 맞혔습니다.")

        if score > self.best_score:
            self.best_score = score
            self.save_state()
            print("최고 점수가 갱신되었습니다!")

    def show_quiz_list(self):
        print("\n===== 영양학 퀴즈 목록 =====")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

        print(f"\n현재 등록된 퀴즈: {len(self.quizzes)}개")

    def add_quiz(self):
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

                print("1~4 사이의 숫자를 입력해 주세요.")

            except ValueError:
                print("숫자로 입력해 주세요.")

        explanation = input("정답 해설을 입력하세요: ").strip()

        while not explanation:
            print("해설은 비워둘 수 없습니다.")
            explanation = input("정답 해설을 입력하세요: ").strip()

        new_quiz = Quiz(question, choices, answer, explanation)
        self.quizzes.append(new_quiz)

        self.save_state()

        print("\n새 퀴즈가 목록에 추가되었습니다!")

    def show_best_score(self):
        print("\n===== 최고 점수 =====")
        print(f"최고 점수: {self.best_score}점")

    def show_menu(self):
        print("\n===== 나의 영양 퀴즈 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가하기")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 보기")
        print("5. 종료하기")

    def run(self):
        print("영양학 퀴즈 프로그램에 오신 것을 환영합니다!")

        while True:
            self.show_menu()
            choice = input("메뉴를 선택하세요 (1~5): ").strip()

            if choice == "1":
                self.play_quiz()

            elif choice == "2":
                self.add_quiz()

            elif choice == "3":
                self.show_quiz_list()

            elif choice == "4":
                self.show_best_score()

            elif choice == "5":
                 self.save_state()
                 print("\n영양학 퀴즈 프로그램을 종료합니다.")
                 break

            else:
                print("\n잘못된 입력입니다. 1~5 사이의 숫자를 입력해 주세요.")


if __name__ == "__main__":
    game = QuizGame()

    try:
        game.run()

    except KeyboardInterrupt:
        print("\n\n프로그램이 중단되었습니다.")
        game.save_state()

    except EOFError:
        print("\n\n입력이 종료되었습니다.")
        game.save_state()
