import sys, pygame, random
from tooltips import check_hands, end_game, check_button

def comp() -> int:
    # return an integer that corresponds a hand
    return random.randint(0,2)

size = width, height = 640, 640

black = 0, 0, 0
white = 255, 255, 250
color_light = 170,170,170

player_score = 0
computer_score = 0
draw_score = 0

class Sprite(pygame.sprite.Sprite):
    def __init__(self, height, width, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        pygame.draw.rect(self.image,pygame.Rect(x, y, width, height))
        self.rect = self.image.get_rect()

pygame.init()
screen = pygame.display.set_mode(size)
rock = pygame.image.load("images/rock.png")
scissors = pygame.image.load("images/scissors.png")
paper = pygame.image.load("images/paper.png")

hands = ["images/rock.png", "images/scissors.png", "images/paper.png"]

rock_img = pygame.transform.scale(rock, (75, 75))
scissors_img = pygame.transform.scale(scissors, (75, 75))
paper_img = pygame.transform.scale(paper, (75, 75))

text = pygame.font.SysFont('Comic Sans MS', 30)
computer = text.render(f'Computer: {str(computer_score)}', True, white)
player = text.render(f'Player: {str(player_score)}', True, white)
draw = text.render(f'Draw: {str(draw_score)}', True, white)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or end_game(player_score, computer_score): sys.exit()
        mouse = pygame.mouse.get_pos()
        if check_button(mouse,width,height):
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
            if event.type == pygame.MOUSEBUTTONDOWN:
                temp_comp = comp()
                temp_player = check_button(mouse,width,height)[1]
                hand_comp = pygame.image.load(hands[temp_comp])
                hand_player = pygame.image.load(hands[temp_player])
                hand_comp = pygame.transform.scale(hand_comp, (75, 75))
                hand_player = pygame.transform.scale(hand_player, (75, 75))
                screen.fill(black)
                screen.blit(hand_comp, (width/2 + 75,height/2 - 70))
                screen.blit(hand_player, (width/2 - 150,height/2 - 70))
                
                if check_hands(temp_player,temp_comp) == 1:
                    player_score += 1
                    computer = text.render(f'Computer: {str(computer_score)}', True, white)
                    player = text.render(f'Player: {str(player_score)}', True, white)
                    draw = text.render(f'Draw: {str(draw_score)}', True, white)
                    screen.blit(computer,(5,5))
                    screen.blit(player,(5,30))
                    screen.blit(draw,(5,55))
                elif check_hands(temp_player,temp_comp) == 2:
                    computer_score +=1
                    computer = text.render(f'Computer: {str(computer_score)}', True, white)
                    player = text.render(f'Player: {str(player_score)}', True, white)
                    draw = text.render(f'Draw: {str(draw_score)}', True, white)
                    screen.blit(computer,(5,5))
                    screen.blit(player,(5,30))
                    screen.blit(draw,(5,55))
                else:
                    draw_score += 1
                    computer = text.render(f'Computer: {str(computer_score)}', True, white)
                    player = text.render(f'Player: {str(player_score)}', True, white)
                    draw = text.render(f'Draw: {str(draw_score)}', True, white)
                    screen.blit(computer,(5,5))
                    screen.blit(player,(5,30))
                    screen.blit(draw,(5,55))
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            
        screen.blit(computer,(5,5))
        screen.blit(player,(5,30))
        screen.blit(draw,(5,55))
        screen.blit(rock_img, (50,height - 130))
        screen.blit(scissors_img, (width/2 - 37.5,height - 130))
        screen.blit(paper_img, (width - 125,height - 130))
        
        pygame.draw.rect(screen,white,[width/2 - 5,height/2 - 20, 10,10])
        pygame.draw.rect(screen,white,[width/2 - 5,height/2 - 50, 10,10])
        
        pygame.display.flip()