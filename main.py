# -*- coding: utf-8 -*-

from robot import *
from constants import *


# https://gm0.org/en/latest/docs/software/odometry.html


def main():
    pygame.init()
    screen = pygame.display.set_mode((FULL_MAP_WIDTH + EXTRA_WIDTH,
                                      FULL_MAP_HEIGHT))
    pygame.display.set_caption(' Robot  |  Odometría ')
    imagen_robot = cargar_robot()

    robot = Robot()
    screen.fill(COLOR_BLANCO)
    robot.dibujar_robot(screen, imagen_robot)
    enc_der, enc_izq = 0, 0
    last_enc_der, last_enc_izq = 0, 0

    run = True
    clock = pygame.time.Clock()
    # ticks_vel = 0
    last_time = pygame.time.get_ticks()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                enc_der, enc_izq = 0, 0  # Descomentar para movimiento continuado.
                # Movimiento continuo hacia delante. Tecla W.
                if event.key == pygame.K_w:
                    enc_der, enc_izq = robot.movimiento_W()
                # Movimiento continuo hacia atrás. Tecla S.
                elif event.key == pygame.K_s:
                    enc_der, enc_izq = robot.movimiento_S()
                # Movimiento de giro sobre si mismo a la izquierda. Tecla A.
                elif event.key == pygame.K_a:
                    enc_der, enc_izq = robot.movimiento_A()
                # Movimiento de giro sobre si mismo a la derecha. Tecla D.
                elif event.key == pygame.K_d:
                    enc_der, enc_izq = robot.movimiento_D()
                # Movimiento continuo con desviación izquierda. Tecla Q.
                elif event.key == pygame.K_q:
                    enc_der, enc_izq = robot.movimiento_Q()
                # Movimiento continuo con desviación derecha. Tecla E.
                elif event.key == pygame.K_e:
                    enc_der, enc_izq = robot.movimiento_E()
                # Resbalón de la rueda derecha. Tecla V.
                elif event.key == pygame.K_v:
                    robot.resbalon_derecha()
                # Resbalón de la rueda izquierda. Tecla B.
                elif event.key == pygame.K_b:
                    robot.resbalon_izquierda()
                # Reinicio de las variables.
                elif event.key == pygame.K_r:
                    robot.reinicio()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_i] and keys[pygame.K_UP]:
                    robot.encoder_aumenta()
                elif keys[pygame.K_i] and keys[pygame.K_DOWN]:
                    robot.encoder_disminuye()
                elif keys[pygame.K_o] and keys[pygame.K_UP]:
                    robot.diametro_derecha_aumenta()
                elif keys[pygame.K_o] and keys[pygame.K_DOWN]:
                    robot.diametro_derecha_disminuye()
                elif keys[pygame.K_p] and keys[pygame.K_UP]:
                    robot.diametro_izquierda_aumenta()
                elif keys[pygame.K_p] and keys[pygame.K_DOWN]:
                    robot.diametro_izquierda_disminuye()
                # Tecla incorrecta = 0.
            # robot.odo_calc(enc_der, enc_izq, ticks_vel) #Activa aceleración continuada (Recoge todos los eventos)
        # robot.dibujar_fondo(screen)
        ticks_vel = (pygame.time.get_ticks() - last_time) / 1000
        last_time = pygame.time.get_ticks()
        pygame.display.flip()
        robot.dibujar_fondo(screen)
        robot.dibujar_robot(screen, imagen_robot)
        robot.dibujar_trail(screen)
        robot.dibujar_pos_info(screen)
        # pygame.display.flip()
        robot.odo_calc(enc_der, enc_izq, ticks_vel)  # Movimiento continuado
        clock.tick(FPS)

    pygame.quit()


def cargar_robot():
    """
        Carga de la imagen del robot.
    """
    robot = pygame.transform.scale(pygame.image.load("assets/car_top_view-removebg.png"),
                                   (FULL_MAP_WIDTH / 10, FULL_MAP_HEIGHT / 10))
    return robot


if __name__ == '__main__':
    main()
