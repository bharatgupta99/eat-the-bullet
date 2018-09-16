import sys, pygame
from random import randint
pygame.init()

score = 0
game_over = 0
gameLoop = True
high_score = 0
updateContent = True

fps = 60
size = width, height = 500, 700
white = 255, 255, 255
black = 0, 0, 0
movement_on_press = 12

clock = pygame.time.Clock();

screen = pygame.display.set_mode(size)

myfont = pygame.font.SysFont('Comic Sans MS', 25)
score_textsurface = myfont.render('Press Up ', False, black)
quit_textsurface = myfont.render('Press \'X\' to quit', False, black)
miss_textsurface = myfont.render('Miss - ' + str(game_over), False, black)
gameOverMyFont = pygame.font.SysFont('Comic Sans MS', 50)
game_over_text_surface = gameOverMyFont.render('GAME OVER', False, black)
retry_text_surface = myfont.render('Press \'R\' to retry', False, black)
high_score_surface = myfont.render('High Score - ' + str(high_score), False, black)



pills = [pygame.image.load("pill.png"), pygame.image.load("pill.png"), pygame.image.load("pill.png"), pygame.image.load("pill.png")]
pills_rects = [pills[0].get_rect(), pills[1].get_rect(), pills[2].get_rect(), pills[3].get_rect()]


flap = pygame.image.load("flappy.png")
flap_width = flap_height = 56
flap_rect = flap.get_rect()
flap_rect.x = 60
flap_rect.y = height - flap_height - 10
y_change = 0

pills_rects[0].x = width
pills_rects[0].y = randint(15, height -flap_height)
pills_rects[1].x = width
pills_rects[1].y = randint(15, height -flap_height)
pills_rects[2].x = width
pills_rects[2].y = randint(15, height -flap_height)
pills_rects[3].x = width
pills_rects[3].y = randint(15, height -flap_height)

def moveFlappy():
	flap_rect.y += y_change
	if flap_rect.y > height - flap_height - 10:
		flap_rect.y = height - flap_height - 10
	elif flap_rect.y < 15:
		flap_rect.y = 15

def startPills():
	global game_over
	pills_rects[0].x -= randint(1,3)
	if pills_rects[0].x < 0:
		game_over += 1
		pills_rects[0].x = width
		pills_rects[0].y = randint(15, height-flap_height)

	pills_rects[1].x -= randint(1,3)
	if pills_rects[1].x < 0:
		game_over += 1
		pills_rects[1].x = width
		pills_rects[1].y = randint(15, height-flap_height)

	pills_rects[2].x -= randint(1,3)
	if pills_rects[2].x < 0:
		game_over += 1 
		pills_rects[2].x = width
		pills_rects[2].y = randint(15, height-flap_height)

	pills_rects[3].x -= randint(1,3)
	if pills_rects[3].x < 0:
		game_over += 1
		pills_rects[3].x = width
		pills_rects[3].y = randint(15, height-flap_height)
	#for i in range(0, 4):
	#	pills_rects[i].x -= randint(1,3)
	#	if pills_rects[i].x < 0:
	#		pills_rects[i].x = width
	#		pills_rects[i].y = randint(15, height-flap_height)

def collisionCheck():
	global score
	if flap_rect.colliderect(pills_rects[0]):
			score += 1
			pills_rects[0].x = width
			pills_rects[0].y = randint(15, height-flap_height)

	if flap_rect.colliderect(pills_rects[1]):
			score += 1
			pills_rects[1].x = width
			pills_rects[1].y = randint(15, height-flap_height)
	if flap_rect.colliderect(pills_rects[2]):
			score += 1
			pills_rects[2].x = width
			pills_rects[2].y = randint(15, height-flap_height)
	if flap_rect.colliderect(pills_rects[3]):
			score += 1
			pills_rects[3].x = width
			pills_rects[3].y = randint(15, height-flap_height)
	#for i in range(0, 4):
	#	if flap_rect.colliderect(pills_rects[i]):
	#		score += 1
	#		pills_rects[i].x = width
	#		pills_rects[i].y = randint(15, height-flap_height)

	

def updateScore():
	score_string = 'Score - ' + str(score)
	global score_textsurface
	score_textsurface = myfont.render(score_string, False, (0, 0, 0))

def updateMisses():
	global miss_textsurface
	miss_score = 'Miss - ' + str(game_over) + '(Max allowed 5)'
	miss_textsurface = myfont.render(miss_score, False, (0, 0, 0))

def gameOver():
	global high_score_surface
	global updateContent
	global high_score
	if game_over >= 5:
		updateContent = False
		if high_score < score:
			high_score = score
		high_score_surface = myfont.render('High Score - ' + str(high_score), False, black)			
		screen.blit(game_over_text_surface, (width - 300, height - 300))
		screen.blit(retry_text_surface, (width - 350, height - 20))	

def reset():
	global game_over
	global score
	global updateContent
	for i in range(0, 4):
		pills_rects[i].x = width	
	flap_rect.x = 60
	game_over = 0
	score = 0
	updateContent = True
	flap_rect.y = height - flap_height - 10


while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        	sys.exit()
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_x:
        		sys.exit()
        	if event.key == pygame.K_r:
        		reset()
        	if event.key == pygame.K_UP:
        		y_change += -movement_on_press
       		if event.key == pygame.K_DOWN:
        		y_change += movement_on_press

        if event.type == pygame.KEYUP:
        	if event.key == pygame.K_UP:
        		y_change += movement_on_press
        	if event.key == pygame.K_DOWN:
        		y_change += -movement_on_press

    if updateContent:
	    moveFlappy()
	    startPills()
	    collisionCheck()
	    updateScore()
	    updateMisses()


    screen.fill(white)
    for i in range(0,4):
    	screen.blit(pills[i], pills_rects[i])
    screen.blit(score_textsurface, (width - 100, 0))
    screen.blit(high_score_surface, (0, 0))
    screen.blit(quit_textsurface, (width - 150, height - 20))
    screen.blit(miss_textsurface, (width - 300, 0))
    screen.blit(flap, flap_rect)
    gameOver()
    pygame.display.update()
    clock.tick(fps)
