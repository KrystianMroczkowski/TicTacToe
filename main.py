import random

game_active = True
slot_list = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
possible_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
current_player_sign = "X"


def print_board():
    board = f" {slot_list[0]} | {slot_list[1]} | {slot_list[2]} \n" \
            f" {slot_list[3]} | {slot_list[4]} | {slot_list[5]} \n" \
            f" {slot_list[6]} | {slot_list[7]} | {slot_list[8]} \n"
    print(board)


def end_game(sign):
    global game_active
    game_active = False
    print_board()
    print(f"{sign} win!")


def win(sign):
    global game_active

    if slot_list[0] == sign and slot_list[1] == sign and slot_list[2] == sign:
        end_game(sign)
    if slot_list[3] == sign and slot_list[4] == sign and slot_list[5] == sign:
        end_game(sign)
    if slot_list[6] == sign and slot_list[7] == sign and slot_list[8] == sign:
        end_game(sign)
    if slot_list[0] == sign and slot_list[3] == sign and slot_list[6] == sign:
        end_game(sign)
    if slot_list[1] == sign and slot_list[4] == sign and slot_list[7] == sign:
        end_game(sign)
    if slot_list[2] == sign and slot_list[5] == sign and slot_list[8] == sign:
        end_game(sign)
    if slot_list[0] == sign and slot_list[4] == sign and slot_list[8] == sign:
        end_game(sign)
    if slot_list[2] == sign and slot_list[4] == sign and slot_list[6] == sign:
        end_game(sign)


def check_spot(i):
    global slot_number
    if slot_list[i] != "-":
        print("This place is occupied")
        slot_number = int(input(f"{current_player_sign}'s turn. Choose slot 1-9: "))
        slot_number -= 1
        check_spot(slot_number)
    return True


while game_active:
    print_board()
    if current_player_sign == "X":
        slot_number = int(input(f"{current_player_sign}'s turn. Choose slot 1-9: "))
        slot_number -= 1
        if check_spot(slot_number):
            slot_list[slot_number] = current_player_sign
            win(current_player_sign)
            if slot_number in possible_moves:
                possible_moves.remove(slot_number)
            current_player_sign = "O"
    if current_player_sign == "O":
        if possible_moves:
            comp_move = random.choice(possible_moves)
            slot_list[comp_move] = current_player_sign
            win(current_player_sign)
            possible_moves.remove(comp_move)
            current_player_sign = "X"
        else:
            print("Draw!")
