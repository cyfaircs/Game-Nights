import pygame
import random

# tuple for window size
size = width, height = (800, 800)
# variable 500 pixels = width/ 1.6
road_w = int(width/1.6)
# variable for yellow line on road
roadmark_w = int(width/80)
# right lane
right_lane = width/2 + road_w/4
# left lane
left_lane = width/2 - road_w/4
#speed of enemy car
speed = 3
# initialize pygame
pygame.init()
running = True
# create the scrren size
screen = pygame.display.set_mode(size)
# set title
pygame.display.set_caption("My first game")
#set background color
screen.fill((60,220,0))

# apply changes
pygame.display.update()
#load player vehicle
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8
#load enemy vehicle
car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

counter = 0
# game loop
while running:
    counter += 1
    if counter == 4000:
        speed += 0.50
        counter =0
        print("Level up", speed)
    #white car animation
    car2_loc[1] += speed
    if car2_loc[1] > height:
#spawning enemy car in random locations
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    #end game
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1]- 250:
        print("GAME OVER YOU LOST!")
        break

#event listeners
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key == pygame.K_RIGHT:
                car_loc = car_loc.move([int(road_w/2), 0])


    # draw graphics
    # main road
    pygame.draw.rect(
        screen,
        (50,50,50),
        (width/2-road_w/2, 0, road_w, height)
        )
    # yellow line
    pygame.draw.rect(
            screen,
            (255, 240, 60),
            (width/2 - roadmark_w/2, 0, roadmark_w, height)
        )
    # white line 1
    pygame.draw.rect(
            screen,
            (255, 255, 255),
            (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height)
        )

    #white line 2
    pygame.draw.rect(
            screen,
            (255, 255, 255),
            (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height)
        )



    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()


pygame.quit()