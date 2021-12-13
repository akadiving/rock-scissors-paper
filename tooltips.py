def check_button(mouse, width, height):
    if 50 <= mouse[0] <= 125 and height - 130 <= mouse[1] <= height - 55:
        return True, 0
    elif width/2 - 37.5 <= mouse[0] <= width/2+37.5 and height - 130 <= mouse[1] <= height - 55:
        return True, 1
    elif width - 125 <= mouse[0] <= width - 50 and height - 130 <= mouse[1] <= height - 55:
        return True, 2
    else:
        return False

def check_hands(player: int, comp: int):
    if player == comp:
        return None
    elif player == 0 and comp == 1:
        return 1
    elif player == 0 and comp == 2:
        return 2
    elif player == 1 and comp == 2:
        return 1
    elif player == 2 and comp == 1:
        return 2
    elif player == 2 and comp == 0:
        return 1
    else:
        return 2

def end_game(player, comp):
    if player == 3 and player > comp:
        return 1
    elif comp == 3 and comp > player:
        return 2
    else:
        None