def is_lucky_ticket(ticket_number):

    if len(ticket_number) % 2 != 0:
        return False


    half_length = len(ticket_number) // 2
    first_half_sum = sum(int(digit) for digit in ticket_number[:half_length])
    second_half_sum = sum(int(digit) for digit in ticket_number[half_length:])


    return first_half_sum == second_half_sum


# Примеры использования
print(is_lucky_ticket("284397"))
print(is_lucky_ticket("972990"))