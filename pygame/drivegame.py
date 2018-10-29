import pygame,random
#Let's import the Car Class
from car import Car
from aicar import AiCar


def collision(sprite1,sprite2):
    if(sprite1.rect.top == sprite2.rect.top and
    sprite1.rect.bottom == sprite2.rect.bottom

    ):
        return True
    else:
        return False






pygame.init()
 
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
        
SCREENWIDTH=275
SCREENHEIGHT=1000
ROAD_STARTX = 75
ROAD_ENDX = SCREENWIDTH-(2*ROAD_STARTX)

difficulty = 100
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
ai_sprites_list = pygame.sprite.Group() 

playerCar = Car(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300
 
# Add the car to the list of objects
all_sprites_list.add(playerCar)

#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()
 
while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_x:
                    carryOn=False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(5)
        if keys[pygame.K_UP]:
            #playerCar.moveUp(5)
            playerCar.accelerate()
        if keys[pygame.K_DOWN]:
            playerCar.moveDown(5)
            #playerCar.decellerate()

        if(pygame.time.get_ticks() % difficulty ==0 ):
            aiColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            aiCar = Car(aiColor, 20, 30)
            aiCar.rect.x = random.randrange(ROAD_STARTX, 2*ROAD_STARTX + aiCar.image.get_width() )#2*GRASS+ aiCar.image.get_width())
            #aiCar.rect.x = SCREENWIDTH-(GRASS+ aiCar.image.get_width())
            #aiCar.rect.x = GRASS
            
            aiCar.rect.y = 000
            all_sprites_list.add(aiCar)
            ai_sprites_list.add(aiCar)




        for sprite in ai_sprites_list:
            sprite.moveDown(playerCar.speed)
            if(sprite.rect.y == playerCar.rect.y):
                if(collision(playerCar, sprite)):
                    #playerCar.decellerate()
                    playerCar.moveDown(10)
                else:
                    #playerCar.accelerate()
                    playerCar.moveUp(10)

        
        #Game Logic
        all_sprites_list.update()
 
        #Drawing on Screen
        screen.fill(GREEN)
        #Draw The Road
        pygame.draw.rect(screen, GREY, [ROAD_STARTX,0, ROAD_ENDX,SCREENHEIGHT])
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [140,0],[140,SCREENHEIGHT],5)
        
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)
 
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pygame.quit()