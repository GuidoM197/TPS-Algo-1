def diferencia(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x = x1 - x2
    dif_y = y1 - y2
    dif_z = z1 - z2
    return dif_x, dif_y, dif_z


assert diferencia(77, -22, -10, 52, 37, -80) == (25, -59, 70)
assert diferencia(16, -72, -52, 55, 90, -31) == (-39, -162, -21)
assert diferencia(55, -88, -75, 38, 62, -12) == (17, -150, -63)