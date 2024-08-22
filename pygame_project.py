#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:17:07 2024

@author: priwi
"""
#   https://webshare.cz
#   https://www.iconarchive.com
import pygame 
import random
import time


file_name = "score.txt"
with open(file_name, 'r') as file:
    # Načítanie obsahu súboru a konverzia na číslo
    hi_score = int(file.read())

                # innicialization pygame 
pygame.init()

                # Farbe definition 
                
schwarz = (0, 0, 0)           # "RGB" /  R = Red  / G = Green / B = Blue
weiss = (255, 255, 255)              
rot = (255, 0, 0)
grun = (0, 250, 0)
blau = (0, 0, 255)
gelb = ( 255, 255, 0)
F1 =( 35, 152, 87)


                # Windows setting
whidth = 1200        # breite  800
height = 1000        # hohe    600
fps = 30                        # Wie fiel bilde in sekunde 
clock = pygame.time.Clock()     # zeit beobachten
name = "Unser Spiel"          # name des fenster
pygame.display.set_caption(name)     # initialicion aus dem name   
screen = pygame.display.set_mode((whidth, height))      # definition des fenster "screeen"
score = 0
file_name = "score.txt"
abgelaufene_zeit = None

                # hintengrund farbe 
# screen.fill(schwarz)      # Zum haupkod ubernehnem !!!      # hintengrund farbe einstellen


                # Bilde
dino_image = pygame.image.load("dracik_prava.png")              # import bild
fish_image = pygame.image.load("maso.png")      # import bild
    
                # Dino einstelungen
dino_start_position = (300, 400)
dino_image_rect = dino_image.get_rect()         # Zum rec  $eck bringen 
dino_image_rect.topleft = (dino_start_position)

                # Fisch einstelunge 
fish_image_rect = fish_image.get_rect()         # Zum rec  $eck bringen 
fish_image_rect.topleft = (100, 200)


                # Tone 
# musikhintergrund = ("musikhintergrund.mp3")
musikhintergrund = ("60sekund.mp3")             # import musikhintergrund 
pygame.mixer.music.load(musikhintergrund)       # musik zum pygame implementieren 
#pygame.mixer.music.play(-1) 
music_schalter = "OFF"                   # Wie viel mal ist wiederholung 
sound_1 = pygame.mixer.Sound("1.mp3")
sound_1.set_volume(0.0)
sound_2 = pygame.mixer.Sound("2.mp3")
sound_1.set_volume(0.0)
sound_3 = pygame.mixer.Sound("OGGGG.mp3")
sound_1.set_volume(0.8)
                # Formen
pygame.draw.line(screen, gelb, (0, 0), (whidth//2,height//2), 1)   # linie malen (fenste, farbe, start point, endpoin, dycke)


                # Texte

                    # font
                    
fonts = pygame.font.get_fonts()         # Fonts aus system ubernomen
# print(fonts)                            # print er die name des fonts 
                    
system_font = pygame.font.SysFont("kokila", 35)   # "kokila"    
system_text = system_font.render("Unsere unbekante Spiel", True, F1)
system_text_rect = system_text.get_rect()           # kestchien fur text
system_text_rect.center = (whidth//2 , 25)                # position text 

super_score_font = pygame.font.SysFont("kokila", 25)
super_score_text = super_score_font.render(f"Höchstpunktzahl: {hi_score}", True, F1)
super_score_text_rect = super_score_text.get_rect()
super_score_text_rect.center = (whidth-(whidth//6) , 25)

production_font = pygame.font.SysFont("kokila", 15)
production_text = production_font.render("Production :" 
                                         "Muhammed Emin Onat," 
                                         "Arjan Nicolaas Versteegh," 
                                         "Peter Priwitzer", True, F1)
production_text_rec = production_text.get_rect()
production_text_rec.center = (whidth/4, height-7)

def zwischen_zeit(formatet_abgelaufene_zeit):
    zwischen_zeit_font = pygame.font.SysFont("ubuntu", 15)
    zwischen_zeit_text = zwischen_zeit_font.render(f"Zwischen Zeit: {formatet_abgelaufene_zeit}", True, F1)
    zwischen_zeit_text_rect = zwischen_zeit_text.get_rect(center=(whidth//2, height - 30))
    return zwischen_zeit_text, zwischen_zeit_text_rect
def music(music_schalter):
    music_on_of_font = pygame.font.SysFont("ubuntu", 15) 
    music_text = music_on_of_font.render(f"Music on/off: {music_schalter}  M", True, F1)
    music_text_rect = music_text.get_rect()
    music_text_rect.center = (whidth-(whidth//6), height - 30) 
    return music_schalter, music_text, music_text_rect

def skore(score):
    skore_font = pygame.font.SysFont("kokila", 28)
    # skore_text = skore_font.render(("Punkte : " + str(score)) , True,F1)
    skore_text = skore_font.render(f"Punkte : {score}", True, F1)
    skore_text_rect = skore_text.get_rect()
    skore_text_rect.center = (whidth//8, 25)
    return skore_text, skore_text_rect

# skore_text, skore_text_rect = skore(score)
# print(skore_text)
# print(skore_text_rect)


                # Haupcode

zwischen_zeit_text, zwischen_zeit_text_rect = zwischen_zeit("0.00 sekunden")

        #
lets_continue = True              # variable fur dem kreislauf / schleife


# counter = 0


while lets_continue:            # anfang der kreitslauf / schleife 
    # counter +=1    
    # print(counter)
    #pygame.event.get()
    for event in pygame.event.get():      # event definbition aus pygame 
                          # die position ausdruck
        if event.type == pygame.QUIT:       # wenn event = QUIT 
            if hi_score < score:
                with open(file_name, 'w') as file:
                    file.write(str(score))
            lets_continue = False   # variable getauscht
            
            
                        # Tastatur definition 
    keys = pygame.key.get_pressed()
    
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dino_image_rect.top > 50:
        dino_image_rect.y -= 10
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dino_image_rect.bottom < height:
        dino_image_rect.y += 10
    if (keys[pygame.K_LEFT] or keys[pygame.K_a])and dino_image_rect.left > 0:
        dino_image_rect.x -= 10
        dino_image = pygame.image.load("dracik_lava.png") 
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d])and dino_image_rect.right < whidth:
        dino_image = pygame.image.load("dracik_prava.png") 
        dino_image_rect.x += 10
    if (keys[pygame.K_m]):
        if music_schalter == "ON":
            music_schalter = "OFF"
            pygame.mixer.music.stop() 
        else:
            music_schalter = "ON"
            pygame.mixer.music.play(-1) 
            
    
                        # Kolision 
    if dino_image_rect.colliderect(fish_image_rect):
        zeit_punkt = time.time()
        if abgelaufene_zeit is not None:
            abgelaufene_zeit_value = zeit_punkt - abgelaufene_zeit
            formatet_abgelaufene_zeit = f"{abgelaufene_zeit_value:.2f} sekunden"
            print(formatet_abgelaufene_zeit)
            zwischen_zeit_text, zwischen_zeit_text_rect = zwischen_zeit(formatet_abgelaufene_zeit)
        abgelaufene_zeit = zeit_punkt
        
        if abgelaufene_zeit == None:
            abgelaufene_zeit = zeit_punkt
            
        if score < 10:
            sound_3.play()
            
        elif score % 20 == 0:
            sound_2.play()
            
        elif score % 10 == 0:
            sound_1.play()
            
        else:
            sound_3.play()
            
        fish_image_rect.centerx = random.randint(24, whidth - 24)  
        fish_image_rect.centery = random.randint(65, height - 55)
        # skore = skore + 1 
        score += 1
   
    skore_text, skore_text_rect = skore(score)
    music_schalter, music_text, music_text_rect = music(music_schalter)    
        # print("KOLISON !!!!!!!!!!!!!!!!")
        
        # Gamers   -- w- oben , s - unten , a - links , d rechts 
        
        #                     # KEY DEFINITION 
        # if event.type == pygame.KEYDOWN:
        #     # print(pygame.key.name(event.key))
        #     if event.key == pygame.K_UP:
        #         # dino_image_rect.y == dino_image_rect.y -10
        #         dino_image_rect.y -= 10
        #     elif event.key == pygame.K_DOWN:
        #         dino_image_rect.y += 10
        #     elif event.key == pygame.K_LEFT:
        #         dino_image_rect.x -= 10
        #     elif event.key == pygame.K_RIGHT:
        #         dino_image_rect.x += 10
                
   
                
    screen.fill(schwarz)
        # print(event) 

            
    screen.blit(dino_image, dino_image_rect)        # dino eitragung    
    screen.blit(fish_image, fish_image_rect)
    
    pygame.draw.line(screen, gelb, (0, 50), (whidth , 50), 2) 

    screen.blit(production_text, production_text_rec)
    screen.blit(zwischen_zeit_text, zwischen_zeit_text_rect)
    screen.blit(music_text,music_text_rect)
    screen.blit(system_text, system_text_rect)      #Text ausdrucken
    screen.blit(skore_text, skore_text_rect)
    screen.blit(super_score_text, super_score_text_rect)
    pygame.display.update()                 # upgrade fur dem display  / verknupft  "hintergrundfarbe,
   
    
            # Timme manager 
    clock.tick(fps)




#                 # Benderung pygame
pygame.quit()                   # proces beendung