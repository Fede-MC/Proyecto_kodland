#Importar librerias
import sys
import pygame
import random


# declaro las constantes a utilizar en el juego
ancho_pantalla= 800
alto_pantalla = 600
color_sprite=255, 0, 0
color_ventana = 0, 0, 0
color_enemigo=0,0,255

#jugador atributos
jugador_size=[50,50]
jugador_pos=[ancho_pantalla/2, alto_pantalla - jugador_size[0]]

#enemigo atributos
enemigo_size=[50,50]
enemigo_pos=[random.randint(0,ancho_pantalla-enemigo_size[0]),0]



#mantenemos la ventana abierta hasta que se de clic en la x de cerrar
ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
game_over=False
clock = pygame.time.Clock()

#Evaluamos las posiciones
def detectar_colision(jugador_pos, enemigo_pos):
    jx_jugador = jugador_pos[0]
    jy_jugador = jugador_pos[1]
    ex_enemigo = enemigo_pos [0]
    ey_enemigo = enemigo_pos[1]

    if (ex_enemigo >= jx_jugador and ex_enemigo <(jx_jugador + jugador_size[0])) or (jx_jugador >= ex_enemigo and jx_jugador < (ex_enemigo + enemigo_size[0])):
       if (ey_enemigo >= jy_jugador and ey_enemigo <(jy_jugador + jugador_size[0])) or (jy_jugador >= ey_enemigo and jy_jugador < (ey_enemigo + enemigo_size[0])):
           return True
    return False   


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = jugador_pos[0]
            if event.key == pygame.K_LEFT:
                x -= jugador_size[0]
            if event.key == pygame.K_RIGHT:
                x += jugador_size[0]
            
            jugador_pos[0] = x
    #volvemos la ventana a su color original para que no quede rastro del personaje al moverse
    ventana.fill(color_ventana) 

    #movimiento al enemigo
    if enemigo_pos[1] >= 0 and enemigo_pos[1] < alto_pantalla:
        enemigo_pos[1] += 20
    else:
        enemigo_pos[0] = random.randint(0, ancho_pantalla - enemigo_size[0] )
        enemigo_pos[1] = 0


    #Llamamos a la función de colisiones
    if detectar_colision(jugador_pos, enemigo_pos):
        game_over = True
   
    #dibujar enemigo
    pygame.draw.rect(ventana, color_enemigo, 
                    (enemigo_pos[0], enemigo_pos[1], 
                    enemigo_size[0], enemigo_size[1]))
    #Dibujar jugador
    pygame.draw.rect(ventana, color_sprite,
                     (jugador_pos[0],jugador_pos[1],
                      jugador_size[0],jugador_size[1]))
    clock.tick(25)
    pygame.display.update()

