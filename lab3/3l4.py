import random

def generate_expression():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*"])  # Выбираем случайный оператор: "+" или "-" или "*"
    expression = f"{num1} {operator} {num2}"
    return expression, eval(expression)  # Возвращаем выражение и его результат

def play_game():
    correct_answers = 0
    wrong_answers = 0

    while wrong_answers < 3:
        expression, expected_result = generate_expression()  # Генерируем новое выражение

        user_answer = input(f"{expression} = ")
        if user_answer.isdigit() and int(user_answer) == expected_result:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Ответ неверный")
            wrong_answers += 1

    print(f"Игра окончена. Правильных ответов: {correct_answers}")

play_game()