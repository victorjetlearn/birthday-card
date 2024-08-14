import pygame
import time

pygame.init()
width = 800
height = 800
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Birthday card")

img1 = pygame.image.load("card.jpg")
image1 = pygame.transform.scale(img1,(800,800))
img2 = pygame.image.load("cake.jpg")
image2 = pygame.transform.scale(img2,(800,800))
img3 = pygame.image.load("sparkles.jpg")
image3 = pygame.transform.scale(img3,(800,800))
while True:
    screen.fill((0,0,0))
    font = pygame.font.SysFont("Arial", 52)
    text = font.render("HAPPY BIRTHDAY",True,"blue")
    screen.blit(image1,(0,0))
    screen.blit(text,(width/3.3,height/2))
    pygame.display.update()
    time.sleep(3)

    
    img2 = pygame.image.load("cake.jpg")
    font = pygame.font.SysFont("Arial", 72)
    text = font.render("HAPPY BIRTHDAY",True,"blue")
    screen.fill((255,255,255))
    screen.blit(image2,(0,0))
    screen.blit(text,(width/2,height/3))
    pygame.display.update()
    time.sleep(3)

    
    img3 = pygame.image.load("sparkles.jpg")
    font = pygame.font.SysFont("Arial", 40)
    text = font.render("Have a lovely day!",True,"blue")
    screen.fill((255,255,255))
    screen.blit(image3,(0,0))
    screen.blit(text,(width/2,height/3))
    pygame.display.update()
    time.sleep(3)

