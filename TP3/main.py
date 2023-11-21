import gamelib
from juegoflood import JuegoFlood

# Constantes para inicializar el estado del juego
# Si N_COLORES es mayor a 10, deben agregarse mas entradas al
# arreglo COLORES mas abajo
ANCHO_JUEGO = 15
ALTO_JUEGO = 12
N_COLORES = 5

# Constantes de visuales
TAM_CELDA = 35
ANCHO_LINEA = 2
MOSTRAR_NUMEROS = False  # útil activarlo por si no son claros los diferentes colores

MARGEN = 20

ALTURA_MOV = ALTO_JUEGO * TAM_CELDA + MARGEN * 2
ALTURA_BOTONES = ALTURA_MOV + MARGEN
ANCHO_BOTONES = (ANCHO_JUEGO * TAM_CELDA - MARGEN) // 2
ANCHO_VENTANA = ANCHO_JUEGO * TAM_CELDA + MARGEN * 2
ALTO_VENTANA = ALTURA_BOTONES + (TAM_CELDA + MARGEN) * 2

COLORES = [
    '#FF0000',
    '#33DD33',
    '#334DFF',
    '#8000B3',
    '#FF8000',
    '#DA2071',
    '#EEEE00',
    '#C0C0C0',
    '#808080',
    '#0C0C0C'
]


def juego_crear():
    juego = JuegoFlood(ALTO_JUEGO, ANCHO_JUEGO, N_COLORES)
    return juego


def manejar_click(juego, x, y):
    if not juego:
        return

    fil = (y - MARGEN) // TAM_CELDA
    col = (x - MARGEN) // TAM_CELDA

    alto, ancho = juego.dimensiones()

    if 0 <= fil < alto and 0 <= col < ancho:
        color = juego.obtener_color(
            (y - MARGEN) // TAM_CELDA,
            (x - MARGEN) // TAM_CELDA
        )
        juego.cambiar_color(color)

    # Primer fila de botones
    if 0 <= y - ALTURA_BOTONES < TAM_CELDA:
        if 0 <= x - MARGEN < ANCHO_BOTONES:
            juego.deshacer()
        if 0 <= x - MARGEN * 2 - ANCHO_BOTONES < ANCHO_BOTONES:
            juego.rehacer()

    # Segunda fila de botones
    if 0 <= y - ALTURA_BOTONES - TAM_CELDA - MARGEN < TAM_CELDA:
        if 0 <= x - MARGEN < ANCHO_BOTONES:
            return juego_crear()
        if 0 <= x - MARGEN * 2 - ANCHO_BOTONES < ANCHO_BOTONES:
            juego.calcular_nueva_solucion()

    return juego



def juego_mostrar_grilla(juego):
    alto, ancho = juego.dimensiones()

    # Muestra los cuadrados de colores
    for f in range(alto):
        for c in range(ancho):
            color = juego.obtener_color(f, c)
            i = list(juego.obtener_posibles_colores()).index(color)
            gamelib.draw_rectangle(
                c * TAM_CELDA + MARGEN,
                f * TAM_CELDA + MARGEN,
                (c + 1) * TAM_CELDA + MARGEN,
                (f + 1) * TAM_CELDA + MARGEN,
                fill=COLORES[i],
                width=0
            )
            if juego.hay_proximo_paso() and color == juego.proximo_paso():
                gamelib.draw_oval(
                    c * TAM_CELDA + MARGEN + TAM_CELDA // 4,
                    f * TAM_CELDA + MARGEN + TAM_CELDA // 4,
                    (c + 1) * TAM_CELDA + MARGEN - TAM_CELDA // 4,
                    (f + 1) * TAM_CELDA + MARGEN - TAM_CELDA // 4,
                    fill='black',
                    width=1
                )

    # Muestra las líneas "divisoras"
    for f in range(alto):
        for c in range(ancho):
            color = juego.obtener_color(f, c)
            if MOSTRAR_NUMEROS:
                gamelib.draw_text(
                    str(color),
                    c * TAM_CELDA + TAM_CELDA // 2 + MARGEN,
                    f * TAM_CELDA + TAM_CELDA // 2 + MARGEN,
                    bold=True,
                    fill='white',
                    anchor='center',
                    size=TAM_CELDA // 2
                )
            if f + 1 < alto and juego.obtener_color(f + 1, c) != color:
                gamelib.draw_line(
                    c * TAM_CELDA - ANCHO_LINEA / 2 + MARGEN,
                    (f + 1) * TAM_CELDA + MARGEN,
                    (c + 1) * TAM_CELDA + ANCHO_LINEA / 2 + MARGEN,
                    (f + 1) * TAM_CELDA + MARGEN,
                    fill='black',
                    width=ANCHO_LINEA
                )
            if c + 1 < ancho and juego.obtener_color(f, c + 1) != color:
                gamelib.draw_line(
                    (c + 1) * TAM_CELDA + MARGEN,
                    f * TAM_CELDA - ANCHO_LINEA / 2 + MARGEN,
                    (c + 1) * TAM_CELDA + MARGEN,
                    (f + 1) * TAM_CELDA + ANCHO_LINEA / 2 + MARGEN,
                    fill='black',
                    width=ANCHO_LINEA
                )


    gamelib.draw_rectangle(
        MARGEN,
        MARGEN,
        ancho * TAM_CELDA + MARGEN,
        alto * TAM_CELDA + MARGEN,
        fill=None,
        width=ANCHO_LINEA
    )


def juego_mostrar_controles(juego):
    gamelib.draw_rectangle(
        0,
        0,
        ANCHO_VENTANA,
        ALTO_VENTANA,
        fill='lightgrey'
    )

    color_movimientos = 'black'
    if juego:
        mejor_n_movimientos = juego.mejor_n_movimientos
        texto_movimientos = f'Movimientos: {juego.n_movimientos} / {mejor_n_movimientos}'
        if juego.n_movimientos > mejor_n_movimientos:
            color_movimientos = 'red'
            texto_movimientos += '  :('
        elif juego.esta_completado():
            color_movimientos = 'blue'
            texto_movimientos += '  :)'
    else:
        texto_movimientos = 'Movimientos: ???'

    gamelib.draw_text(
        texto_movimientos,
        ANCHO_VENTANA // 3,
        ALTURA_MOV,
        anchor='w',
        bold=True,
        fill=color_movimientos
    )

    acciones = [
        'Deshacer (Z)',
        'Rehacer (X)',
        'Nuevo (N)',
        'Solucionar (S)',
    ]
    for i in range(4):
        gamelib.draw_rectangle(
            MARGEN + (ANCHO_BOTONES + MARGEN) * (i % 2),
            ALTURA_BOTONES + (TAM_CELDA + MARGEN if i >= 2 else 0),
            (ANCHO_BOTONES + MARGEN) * (i % 2 + 1),
            ALTURA_BOTONES + TAM_CELDA + (TAM_CELDA + MARGEN if i >= 2 else 0),
            width=ANCHO_LINEA
        )
        gamelib.draw_text(
            acciones[i],
            MARGEN + (ANCHO_BOTONES + MARGEN) * (i % 2) + ANCHO_BOTONES // 2,
            ALTURA_BOTONES + TAM_CELDA // 2 + (TAM_CELDA + MARGEN if i >= 2 else 0),
            fill='black',
            anchor='c',
            bold=True
        )


def main():
    try:
        juego = juego_crear()
    except NotImplementedError:
        print('No se completaron todos los métodos de la Parte 1')
        juego = None

    gamelib.resize(
        ANCHO_VENTANA,
        ALTO_VENTANA
    )

    while gamelib.loop(fps=30):
        gamelib.draw_begin()
        juego_mostrar_controles(juego)
        if juego:
            try:
                juego_mostrar_grilla(juego)
            except NotImplementedError:
                print("No se completaron todos los métodos de la Parte 1")
                pass
        gamelib.draw_end()

        for ev in gamelib.get_events():
            if ev.type == gamelib.EventType.KeyPress:
                if ev.key == 'Escape':
                    return

                if not juego:
                    continue

                if ev.key.lower() == 'z':
                    juego.deshacer()

                if ev.key.lower() == 'x':
                    juego.rehacer()

                if ev.key.lower() == 's':
                    juego.calcular_nueva_solucion()

                if ev.key.lower() == 'n':
                    juego = juego_crear()

            if ev.type == gamelib.EventType.ButtonPress:
                x, y = ev.x, ev.y
                juego = manejar_click(juego, x, y)

gamelib.init(main)
