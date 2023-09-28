
def diferencia(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x = x1 - x2
    dif_y = y1 - y2
    dif_z = z1 - z2
    return dif_x, dif_y, dif_z

def norma(x, y, z):
    """Recibe un vector en R3 y devuelve su norma"""
    return (x**2 + y**2 + z**2) ** 0.5

def prod_vect(x1, y1, z1, x2, y2, z2): return y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2
"""Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""