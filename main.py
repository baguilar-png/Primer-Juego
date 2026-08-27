import pygame

pygame.init()
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Menú principal")
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (70, 130, 180)
GRIS = (180, 180, 180)
fuente_titulo = pygame.font.Font(None, 60)
fuente = pygame.font.Font(None, 40)
menu = "menu"
juego = "juego"
intrucciones = "instrucciones"
estado = menu
boton_jugar = pygame.Rect(300, 220, 200, 60)
boton_instrucciones = pygame.Rect(300, 310, 200, 60)
boton_salir = pygame.Rect(300, 400, 200, 60)
personaje_img = pygame.image.load("personajes/benja.png").convert_alpha()
personaje_img = pygame.transform.scale(personaje_img, (60, 80))
personaje = pygame.Rect(100, 400, 60, 80)
personaje_img1 = pygame.image.load("personajes/benja1.png").convert_alpha()
personaje_img1 = pygame.transform.scale(personaje_img1, (60, 80))
personaje1 = pygame.Rect(100, 400, 60, 80)
fondo = pygame.image.load("imagenes/fondo (2).png").convert()
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
ejecutando = True
velocidad = 5
x = 400
y = 100
velocidad_horizontal = 5
velocidad_vertical = 0
gravedad = 1
fuerza_salto = -15
en_suelo = True
suelo = 500
reloj = pygame.time.Clock()


while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = pygame.mouse.get_pos()
            if estado == menu:
                if boton_jugar.collidepoint(posicion_mouse):
                    estado = juego
                elif boton_instrucciones.collidepoint(posicion_mouse):
                    estado = intrucciones
                elif boton_salir.collidepoint(posicion_mouse):
                    ejecutando = False
            elif estado == juego or estado == intrucciones:
                estado = menu

    if estado == menu:
        ventana.fill((25, 30, 40))
        titulo = fuente_titulo.render("Mi primer juego", True, NEGRO)
        ventana.blit(titulo, (250, 100))
        pygame.draw.rect(ventana, AZUL, boton_jugar)
        pygame.draw.rect(ventana, AZUL, boton_instrucciones)
        pygame.draw.rect(ventana, AZUL, boton_salir)
        texto_jugar = fuente.render("Jugar", True, BLANCO)
        texto_instrucciones = fuente.render("Instrucciones", True, BLANCO)
        texto_salir = fuente.render("Salir", True, BLANCO)
        ventana.blit(texto_jugar, (355, 235))
        ventana.blit(texto_instrucciones, (305, 325))
        ventana.blit(texto_salir, (365, 415))

    elif estado == juego:
        ventana.blit(fondo, (0, 0))
        texto = fuente_titulo.render("PANTALLA DE JUEGO", True, BLANCO)
        ventana.blit(texto, (170, 100))
        volver = fuente.render("Hacé click para volver al menú", True, NEGRO)
        ventana.blit(volver, (170, 530))
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_a]:
            personaje.x -= velocidad_horizontal
        if teclas[pygame.K_d]:
            personaje.x += velocidad_horizontal
        if teclas[pygame.K_SPACE] and en_suelo:
            velocidad_vertical = fuerza_salto
            en_suelo = False
        velocidad_vertical += gravedad
        personaje.y += velocidad_vertical
        if personaje.bottom >= suelo:
            personaje.bottom = suelo
            velocidad_vertical = 0
            en_suelo = True
        if personaje.left < 0:
            personaje.left = 0
        if personaje.right > ANCHO:
            personaje.right = ANCHO

        ventana.blit(personaje_img, personaje)

    elif estado == intrucciones:
        ventana.fill((25, 30, 40))
        titulo = fuente_titulo.render("INSTRUCCIONES", True, NEGRO)
        ventana.blit(titulo, (220, 100))
        texto1 = fuente.render("Usá las flechas para moverte.",True, NEGRO)
        texto2 = fuente.render("Evitá los obstáculos.", True, NEGRO)
        texto3 = fuente.render("Hacé click para volver al menú.", True, NEGRO)
        ventana.blit(texto1, (160, 230))
        ventana.blit(texto2, (160, 290))
        ventana.blit(texto3, (160, 550))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

