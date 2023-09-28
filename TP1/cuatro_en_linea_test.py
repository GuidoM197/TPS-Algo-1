import pprint
import sys
import traceback
from typing import List

import cuatro_en_linea

# Si las pruebas se ven mal en tu terminal, probá cambiando el valor
# de esta constante a True para desactivar los colores ANSI.
TERMINAL_SIN_COLOR = False


def validar_estado(desc: List[List[str]], tablero: List[List[str]]):
    """Asegura que `tablero` tenga un estado similar a `desc`. Se prueba que:
    - El tipo de cada elemento, en todos sus niveles, sea el mismo
    - Las dimensiones sean las mismas
    - El contenido sea el mismo
    """
    x = None
    y = None
    ancho, alto = len(desc[0]), len(desc)
    try:
        assert type(desc) is type(tablero), (
            "Valor en `tablero` no es del tipo lista"
        )
        assert len(tablero) > 0, "Lista en `tablero` está vacía"
        assert (ancho, alto) == (len(tablero[0]), len(tablero)), (
            f"Dimension obtenida ({ancho}, {alto}) no es la esperada "
            f"({len(desc[0])}, {len(desc)})"
        )
        for y in range(alto):
            assert type(desc[y]) is type(tablero[y]), (
                f"Valor en `tablero[{y}]` no es del tipo lista"
            )
            for x in range(ancho):
                assert type(desc[y][x]) is type(tablero[y][x]), (
                    f"Valor en `tablero[{y}][{x}]` no es del tipo cadena"
                )
                assert desc[y][x] == tablero[y][x]
    except AssertionError as exc:
        error_msg = "Estado esperado:\n"
        error_msg += pprint.pformat(desc) + "\n"
        error_msg += "\n"
        error_msg += "Estado actual:\n"
        error_msg += pprint.pformat(tablero) + "\n\n"
        if x is not None and y is not None:
            error_msg += f"Error en columna = {x}, fila = {y}:\n"
            error_msg += f"\tValor esperado: {desc[x][y]}\n"
            error_msg += f"\tValor encontrado: {tablero[x][y]}\n"
        raise AssertionError(error_msg + str(exc)) from exc


def test_01_representacion_simple():
    """Crea un nuevo juego básico de cuatro en línea de dimensiones simétricas
    6x6"""
    desc = [
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
    ]
    tablero = cuatro_en_linea.crear_tablero(6, 6)
    validar_estado(desc, tablero)


def test_02_representacion_rectangular():
    """Crea un nuevo juego básico de cuatro en línea de dimensiones 5x7"""
    desc = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
    ]
    tablero = cuatro_en_linea.crear_tablero(5, 7)
    validar_estado(desc, tablero)


def test_03_juego_inicial_comienza_x():
    """Crea un nuevo juego 5x7 y valida el comportamiento de `es_turno_de_x` para
    el estado inicial."""
    tablero = cuatro_en_linea.crear_tablero(5, 7)
    assert cuatro_en_linea.es_turno_de_x(tablero), (
        "`es_turno_de_x` devolvió `False` cuando debería devolver `True`. "
        "Estado actual:\n"
        f"{pprint.pformat(tablero)}\n"
    )


def test_04_insertar_una_vez():
    """Crea un nuevo juego 5x7 e inserta un símbolo en la columna 3.
    Asegura que el primer símbolo insertado sea un X y se encuentre en la última
    fila del juego.
    Asegura que el retorno de `insertar_simbolo` sea True.
    Asegura que, luego insertado el símbolo, `es_turno_de_x` devuelva False."""
    desc = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", "X", " ", " ", " "],
    ]
    tablero = cuatro_en_linea.crear_tablero(5, 7)
    assert cuatro_en_linea.insertar_simbolo(tablero, 3), (
        "`insertar_simbolo` devolvió `False` cuando debería devolver `True`. "
        "Estado actual:\n"
        f"{pprint.pformat(tablero)}\n"
    )
    validar_estado(desc, tablero)
    assert not cuatro_en_linea.es_turno_de_x(tablero), (
        "`es_turno_de_x` devolvió `True` cuando debería devolver `False`. "
        "Estado actual:\n"
        f"{pprint.pformat(tablero)}\n"
    )


def test_05_insertar_dos_veces():
    """Crea un nuevo juego 5x7 e inserta un símbolo en la columna 3, y luego
    otro símbolo en la columna 2.
    Asegura que el primer símbolo insertado sea un X, el segundo sea un O, y
    que ambos se encuentren en la última fila del juego.
    Asegura que, luego insertado ambos símbolos, `es_turno_de_x` devuelva True.
    """
    desc = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "O", "X", " ", " ", " "],
    ]
    tablero = cuatro_en_linea.crear_tablero(5, 7)
    cuatro_en_linea.insertar_simbolo(tablero, 3)
    cuatro_en_linea.insertar_simbolo(tablero, 2)
    validar_estado(desc, tablero)
    assert cuatro_en_linea.es_turno_de_x(tablero), (
        "`es_turno_de_x` devolvió `False` cuando debería devolver `True`. "
        "Estado actual:\n"
        f"{pprint.pformat(tablero)}\n"
    )


def test_06_mantener_dos_juegos_en_paralelo():
    """Crea un juego 4x4 y un juego 5x6. Inserta un símbolo en el primero y dos
    en el segundo. Valida que las dimensiones y el contenido de cada uno sea el
    esperado al finalizar de insertar.
    Si falla esta prueba, probablemente se estén usando variables globales en
    alguna parte del código realizado, prohibido por el enunciado del TP1.
    """
    tablero1 = cuatro_en_linea.crear_tablero(5, 5)
    cuatro_en_linea.insertar_simbolo(tablero1, 3)

    tablero2 = cuatro_en_linea.crear_tablero(5, 6)
    cuatro_en_linea.insertar_simbolo(tablero2, 2)
    cuatro_en_linea.insertar_simbolo(tablero2, 1)

    desc1 = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", "X", " "],
    ]
    desc2 = [
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", "O", "X", " ", " ", " "],
    ]
    assert not cuatro_en_linea.es_turno_de_x(tablero1), (
        "`es_turno_de_x` devolvió `True` cuando debería devolver `False`. "
        "¿Se están usando variables globales en el código?"
    )
    assert cuatro_en_linea.es_turno_de_x(tablero2), (
        "`es_turno_de_x` devolvió `False` cuando debería devolver `True`. "
        "¿Se están usando variables globales en el código?"
    )

    validar_estado(desc1, tablero1)
    validar_estado(desc2, tablero2)


def test_07_insertar_tres_veces_con_superposicion():
    """Crea un nuevo juego 5x7 e inserta tres símbolos en la columna 3.
    Asegura que los tres símbolos insertados sean los correctos y se encuentren
    en la posición esperada.
    Asegura que, luego insertado ambos símbolos, `es_turno_de_x` devuelva True.
    """
    desc = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", "X", " ", " ", " "],
        [" ", " ", " ", "O", " ", " ", " "],
        [" ", " ", " ", "X", " ", " ", " "],
    ]
    tablero = cuatro_en_linea.crear_tablero(5, 7)
    cuatro_en_linea.insertar_simbolo(tablero, 3)
    cuatro_en_linea.insertar_simbolo(tablero, 3)
    cuatro_en_linea.insertar_simbolo(tablero, 3)
    validar_estado(desc, tablero)
    assert not cuatro_en_linea.es_turno_de_x(tablero), (
        "`es_turno_de_x` devolvió `True` cuando debería devolver `False`. "
        "Estado actual:\n"
        f"{pprint.pformat(tablero)}\n"
    )


def test_08_insertar_todas_las_columnas():
    """Crea un nuevo juego 5x7 e inserta símbolos en todas las columnas una
    vez. Asegura que el retorno de `insertar_simbolo` sea True en todos los
    casos."""
    desc = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        ["X", "O", "X", "O", "X", "O", "X"],
    ]
    tablero = cuatro_en_linea.crear_tablero(5, 7)
    for col in range(len(tablero[0])):
        assert cuatro_en_linea.insertar_simbolo(tablero, col), (
            "`insertar_simbolo` devolvió `False` cuando deberia devolver `True`. "
            "Estado actual:\n"
            f"{pprint.pformat(tablero)}\n"
        )
    validar_estado(desc, tablero)
    assert not cuatro_en_linea.es_turno_de_x(tablero), (
        "`es_turno_de_x` devolvió `True` cuando debería devolver `False`. "
        "Estado actual:\n"
        f"{pprint.pformat(tablero)}\n"
    )


def test_09_insertar_en_columnas_invalidas():
    """Crea un nuevo juego 5x7 e intenta insertar símbolos en columnas
    inválidas. Asegura que la función `insertar_simbolo` devuelva `False` para
    estos casos.
    """
    desc = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
    ]
    tablero = cuatro_en_linea.crear_tablero(5, 7)
    for col in (-1, 10, 7, -15):
        assert not cuatro_en_linea.insertar_simbolo(tablero, col), (
            f"`insertar_simbolo` para columna={col} devolvió `True`. "
            "Estado actual:\n"
            f"{pprint.pformat(tablero)}\n"
        )
    validar_estado(desc, tablero)


def test_10_insertar_hasta_saturar_columna():
    """Crea un nuevo juego 5x7 e inserta símbolos hasta que la columna se
    encuentre llena.
    Asegura que en la columna se encuentren los símbolos esperados en la columna
    tres, y que el retorno de `insertar_simbolo` sea el correcto en todos los
    casos."""
    desc = [
        [" ", " ", " ", "X", " ", " ", " "],
        [" ", " ", " ", "O", " ", " ", " "],
        [" ", " ", " ", "X", " ", " ", " "],
        [" ", " ", " ", "O", " ", " ", " "],
        [" ", " ", " ", "X", " ", " ", " "],
    ]
    tablero = cuatro_en_linea.crear_tablero(5, 7)
    for _ in range(5):
        assert cuatro_en_linea.insertar_simbolo(tablero, 3), (
            f"`insertar_simbolo` devolvió `False` cuando debería devolver `True`. "
            "Estado actual:\n"
            f"{pprint.pformat(tablero)}\n"
        )
    assert not cuatro_en_linea.insertar_simbolo(tablero, 3), (
        f"`insertar_simbolo` devolvió `True` cuando debería devolver `False`. "
        "Estado actual:\n"
        f"{pprint.pformat(tablero)}\n"
    )
    validar_estado(desc, tablero)


def test_11_tablero_completo():
    """Crea un nuevo juego 5x5 e inserta símbolos hasta saturar todo el tablero.
    Valida el retorno de la función `juego_terminado`."""
    tablero = cuatro_en_linea.crear_tablero(5, 5)
    for _ in range(5):
        for col in range(5):
            assert not cuatro_en_linea.tablero_completo(tablero), (
                f"`tablero_completo` devolvió `True` cuando debería devolver `False`. "
                "Estado actual:\n"
                f"{pprint.pformat(tablero)}\n"
            )
            cuatro_en_linea.insertar_simbolo(tablero, col)

    assert cuatro_en_linea.tablero_completo(tablero), (
        f"`tablero_completo` devolvió `False` cuando debería devolver `True`. "
        "Estado actual:\n"
        f"{pprint.pformat(tablero)}\n"
    )


def test_12_obtener_ganador_horizontal():
    """Crea un nuevo juego 5x5 e inserta los símbolos necesarios para que X
    gane el juego por un cuatro en línea en la fila inferior.
    Asegura que `obtener_ganador` devuelva lo correcto en cada paso."""
    tablero = cuatro_en_linea.crear_tablero(5, 5)
    for col in range(3):
        assert cuatro_en_linea.obtener_ganador(tablero) == " ", (
            f"`obtener_ganador` no devolvió \" \". "
            "Estado actual:\n"
            f"{pprint.pformat(tablero)}\n"
        )
        for _ in range(2):
            cuatro_en_linea.insertar_simbolo(tablero, col)

    cuatro_en_linea.insertar_simbolo(tablero, 3)
    assert cuatro_en_linea.obtener_ganador(tablero) == "X", (
        f"`obtener_ganador` no devolvió \"X\". "
        "Estado actual:\n"
        f"{pprint.pformat(tablero)}\n"
    )


def test_13_obtener_ganador_vertical():
    """Crea un nuevo juego 5x5 e inserta los símbolos necesarios para que O
    gane el juego por un cuatro en línea en la columna derecha.
    Asegura que `obtener_ganador` devuelva lo correcto en cada paso."""
    tablero = cuatro_en_linea.crear_tablero(5, 5)
    for i in range(4):
        assert cuatro_en_linea.obtener_ganador(tablero) == " ", (
            f"`obtener_ganador` no devolvió \" \". "
            "Estado actual:\n"
            f"{pprint.pformat(tablero)}\n"
        )
        cuatro_en_linea.insertar_simbolo(tablero, (i % 3) + 1)
        cuatro_en_linea.insertar_simbolo(tablero, 0)

    assert cuatro_en_linea.obtener_ganador(tablero) == "O", (
        f"`obtener_ganador` no devolvió \"O\". "
        "Estado actual:\n"
        f"{pprint.pformat(tablero)}\n"
    )


def test_14_obtener_ganador_diagonal():
    """Crea un nuevo juego 5x5 e inserta los símbolos necesarios para que X
    gane el juego por un cuatro en línea en una diagonal de abajo a la
    derecha hacia arriba a la izquierda.
    Asegura que `obtener_ganador` devuelva lo correcto en cada paso."""
    tablero = cuatro_en_linea.crear_tablero(5, 5)
    for i in range(4):
        assert cuatro_en_linea.obtener_ganador(tablero) == " ", (
            f"`obtener_ganador` no devolvió \" \". "
            "Estado actual:\n"
            f"{pprint.pformat(tablero)}\n"
        )
        for j in range(i + 1):
            if j == i and not cuatro_en_linea.es_turno_de_x(tablero):
                cuatro_en_linea.insertar_simbolo(tablero, 4)
            cuatro_en_linea.insertar_simbolo(tablero, 4 - i)

    assert cuatro_en_linea.obtener_ganador(tablero) == "X", (
        f"`obtener_ganador` no devolvió \"X\". "
        "Estado actual:\n"
        f"{pprint.pformat(tablero)}\n"
    )


def test_15_obtener_ganador_diagonal_inversa():
    """Crea un nuevo juego 5x5 e inserta los símbolos necesarios para que X
    gane el juego por un cuatro en línea en una diagonal de abajo a la
    izquierda hacia arriba a la derecha.
    Asegura que `obtener_ganador` devuelva lo correcto en cada paso."""
    tablero = cuatro_en_linea.crear_tablero(5, 5)
    for i in range(4):
        assert cuatro_en_linea.obtener_ganador(tablero) == " ", (
            f"`obtener_ganador` no devolvió \" \". "
            "Estado actual:\n"
            f"{pprint.pformat(tablero)}\n"
        )
        for j in range(i + 1):
            if j == i and not cuatro_en_linea.es_turno_de_x(tablero):
                cuatro_en_linea.insertar_simbolo(tablero, 0)
            cuatro_en_linea.insertar_simbolo(tablero, i)

    assert cuatro_en_linea.obtener_ganador(tablero) == "X", (
        f"`obtener_ganador` no devolvió \"X\". "
        "Estado actual:\n"
        f"{pprint.pformat(tablero)}\n"
    )


# Sólo se van a correr aquellos tests que estén mencionados dentro de la
# siguiente constante
TESTS = (
    test_01_representacion_simple,
    test_02_representacion_rectangular,
    test_03_juego_inicial_comienza_x,
    test_04_insertar_una_vez,
    test_05_insertar_dos_veces,
    test_06_mantener_dos_juegos_en_paralelo,
    test_07_insertar_tres_veces_con_superposicion,
    test_08_insertar_todas_las_columnas,
    test_09_insertar_en_columnas_invalidas,
    test_10_insertar_hasta_saturar_columna,
    test_11_tablero_completo,
    test_12_obtener_ganador_horizontal,
    test_13_obtener_ganador_vertical,
    test_14_obtener_ganador_diagonal,
    test_15_obtener_ganador_diagonal_inversa,
)

# El código que viene abajo tiene algunas *magias* para simplificar la corrida
# de los tests y proveer la mayor información posible sobre los errores que se
# produzcan. ¡No te preocupes si no lo entendés completamente!

# Colores ANSI para una salida más agradable en las terminales que lo permitan
COLOR_OK = "\033[1m\033[92m"
COLOR_ERR = "\033[1m\033[91m"
COLOR_RESET = "\033[0m"


def print_color(color: str, *args, **kwargs):
    """
    Mismo comportamiento que `print` pero con un
    primer parámetro para indicar de qué color se
    imprimirá el texto.

    Si la constante TERMINAL_SIN_COLOR es True,
    esta función será exactamente equivalente
    a utilizar `print`.
    """
    if TERMINAL_SIN_COLOR:
        print(*args, **kwargs)
    else:
        print(color, end="")
        print(*args, **kwargs)
        print(COLOR_RESET, end="", flush=True)


def main():
    tests_fallidos = []
    tests_a_correr = [int(t) for t in sys.argv[1:]]
    for i, test in [
        (i, test)
        for i, test in enumerate(TESTS)
        if not tests_a_correr or i + 1 in tests_a_correr
    ]:
        print(f"Prueba {i + 1 :02} - {test.__name__}: ", end="", flush=True)
        try:
            test()
            print_color(COLOR_OK, "[OK]")
        except AssertionError as e:
            tests_fallidos.append(test.__name__)
            print_color(COLOR_ERR, "[ERROR]")
            print_color(COLOR_ERR, " >", *e.args)
            break
        except Exception:
            tests_fallidos.append(test.__name__)
            print_color(COLOR_ERR, "[BOOM - Explotó]")
            print("\n--------------- Python dijo: ---------------")
            traceback.print_exc()
            print("--------------------------------------------\n")
            break

    if not tests_fallidos:
        print()
        print_color(COLOR_OK, "###########")
        print_color(COLOR_OK, "# TODO OK #")
        print_color(COLOR_OK, "###########")
        print()
    else:
        print()
        print_color(COLOR_ERR, "##################################")
        print_color(COLOR_ERR, "              ¡ERROR!             ")
        print_color(COLOR_ERR, "Falló el siguiente test:")
        for test_con_error in tests_fallidos:
            print_color(COLOR_ERR, " - " + test_con_error)
        print_color(COLOR_ERR, "##################################")
        print(
            "TIP: Si la información de arriba no es suficiente para entender "
            "el error, revisá el código de las pruebas que fallaron en el "
            "archivo cuatro_en_linea_tes.py."
        )


main()