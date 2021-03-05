import pygame
import sys

pygame.init()  # Para iniciar pygame

# El tamaño de la ventana se le debe poner en tuplas
size_wn = (800, 500)

# Asignacion de colores en formato RGB (los que se desee)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
AZURE = (0, 127, 255)
ORANGE = (255, 103, 0)
BROWN = (139, 69, 19)
SILVER = (201, 192, 187)

# Crear la ventana
wn = pygame.display.set_mode(size_wn)

# Velocidad a la que se moverá el cuadrado (FPS)
clock = pygame.time.Clock()

# Coordenadas del cuadrado
coord_x = 400
coord_y = 240

# Pixeles a la que se cambiará el cuadrado
speed_x = 3
speed_y = 3

while True:
    # Este "for" sirve para que no se trabe la ventana al momento de cerrarla
    for event in pygame.event.get():
        # print(event) Para ver en la consola cada movimiento
        if event.type == pygame.QUIT:
            sys.exit()
      
    # Para la animación
    coord_x += speed_x
    coord_y += speed_y
    #-------LOGICA DEL JUEGO
    if coord_x > 720 or coord_x < 0:
          speed_x *= -1
    elif coord_y > 420 or coord_y < 0:
          speed_y *= -1
    #-------LOGICA DEL JUEGO
      
    
    # Para asignar el color de fondo
    wn.fill(AZURE)
    
    # <--------ZONA DE DIBUJO---------->
    # Se dibuja una linea desde el punto (100, 100) hasta (200, 300) con un espesor de 5.
   #pygame.draw.line(wn, GREEN, (0, 100), (200, 300), 5)
    
    # Se dibuja un cuadrado a 100 de la izquierda y 100 de arriba con dimensiones
   # 25px de width y 25px de height
   # fill_rect = pygame.Rect(100, 100, 25, 25)
   # pygame.draw.rect(wn, RED, fill_rect) # Si not tiene width es relleno
    
   # empty_rect = pygame.Rect(200, 150, 25, 25)
   # pygame.draw.rect(wn, WHITE, empty_rect, 3)
    
    # Creando bucles para no repetir
    # for x in range(100, 701, 100):
    #    pygame.draw.rect(wn, WHITE, (x, 100, 25, 25), 2)
    #    pygame.draw.line(wn, GREEN, (x, 150), (x, 300), 3)
    #<--------ZONA DE DIBUJO---------->
    
    #<--------ANIMACIÓN------------->
    cuadrado = pygame.Rect(coord_x, coord_y, 80, 80)
    pygame.draw.rect(wn, RED, cuadrado)
    #<--------ANIMACIÓN------------->
    
    # Para actualizar la pantalla
    pygame.display.flip()
    
    # Velocidad de movimiento
    clock.tick(60)
