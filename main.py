import pygame
import random

               # innicialization_pygame
pygame.init()

                # Farben definition

black = rgb = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
F1 =(15,15,15)


               #Windows setting

whidth = 800   # breite
height = 600   # höhe
fps = 30                                # wie viele Bilder pro Sekunde
clock = pygame.time.Clock()             # Zeitfenster
Name = "Unser Spiel"
pygame.display.set_caption('Name')
screen = pygame.display.set_mode((whidth, height))
score = 0
                    # Hintergrund Farbe


#screen.fill(black)                           #Hintergrund Farbe einstellen



                    # Bilder

dino_image = pygame.image.load("Papirus-Team-Papirus-Apps-Dino.64.png")              # import bild
fish_image = pygame.image.load("Icons-Land-Multiple-Smiley-Fish-Movie.48.png")               # importiertes Bild


dino_image_rect = dino_image.get_rect()
dino_image_rect.topleft =(400, 400)
fish_image_rect = fish_image.get_rect()
fish_image_rect.topright =(400, 400)

                    # Töne

# musikhintergrund = ("musikhintergrund.mp3")
musikhintergrund = ("60sekund.mp3")                # Import Musik Hintergrund
pygame.mixer.music.load(musikhintergrund)           #  Musik bei Pygame intergrieren
#pygame.mixer.music.play(-1)                         # Wie oft wiederholen





                    # Formen

pygame.draw.line(screen, yellow, (0, 0), (whidth//2,height//2), 5)      #Linie zeichnen (Fenster, Farbe, Startpunkt, Endpunkt, Dicke)

                    # Text



#fonts = pygame.font.get_fonts()             # Fonts aus System übernommen
#print(fonts)                                # Print die Namen von dem Fonts

system_font = pygame.font.SysFont("Arial",22 )
system_text = system_font.render("Peter´s Spielchen", True, white, red)
system_text = system_font.render("Peter´s Spielchen", True, white, red)
system_text_rect = system_text.get_rect()               # Kästchen für den Text
system_text_rect.center = (whidth//3 , height//3)                    # Position des Textes

skore_font = pygame.font.SysFont("Arial",30 )
# score_text = pygame.font.render(("Punkte" :  + score),  True, white, red)
# skore_text = skore_font.render(f"Punkte : {score}", True, F1)
skore_text = skore_font.render(f"Punkte : {score}", True, F1)
skore_text_rect = skore_text.get_rect()
skore_text_rect.center = (whidth//10, 25)





                    # Hauptcode

          #
lets_continue = True                                    # Variable für die Schleife

score = 0

while lets_continue:                                            # Anfang der Schleife
    ##counter = 0

    ##print(counter)
    ##pygame.event.get()
    for event in pygame.event.get():                                 # Event Definition aus Pygame
                         # Positionsausdruck
        if event.type == pygame.QUIT:
            lets_continue = False  # Variable getauscht

                       # Tastastur definition


    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and fish_image_rect.top > 0:
        fish_image_rect.y -= 10
    if keys[pygame.K_DOWN] and fish_image_rect.bottom < height:
        fish_image_rect.y += 10
    if keys[pygame.K_LEFT] and fish_image_rect.left > 0:
        fish_image_rect.x -= 10
    if keys[pygame.K_RIGHT] and fish_image_rect.right < whidth:
        fish_image_rect.x += 10

                        # Kolision
    if fish_image_rect.colliderect(dino_image_rect):
        dino_image_rect.centerx = random.randint(0,whidth - 24)
        dino_image_rect.centery = random.randint(0,height - 24)
       # score = score + 1
        score += 1


        # Gamers     **W-Oben ,S-Unten ,D-Rechts ,A-Links




        whidth -= 10
        height              #Breite




#if event.type == pygame.KEYDOWN:
       # print(pygame.key.name(event.key))
#if event.key == pygame.K_UP:
       # fisch_image_rect.y == fisch_image_rect.y -10
       # fisch_image_rect.y -= 10
   # elif event.key == pygame.K_DOWN:
              # fisch_image_rect.y += 10
   # elif event.key == pygame.K_LEFT:
               #fisch_image_rect.x -= 10
  #  elif event.key == pygame.K_RIGHT:
          # fisch_image_rect.x += 10





    screen.fill(black)
        # print(event)



    screen.blit(dino_image, dino_image_rect)                           # Dino hinzugefügt
    screen.blit(fish_image , fish_image_rect)                          # Fisch hinzugefügt

    #pygame.draw.line(screen, yellow, (0, 50), (whidth, 50), 2)

    screen.blit(skore_text, skore_text_rect)

    pygame.display.update()                                #Upgrade für den Display



            # Time Manger
    clock.tick(fps)

                            # Beendung Pygame

pygame.quit()           # Beendung des Prozesses     ######  da war die fehler war nicht in richtige position !!!! vorsicht :D 
