from vectores import diferencia, prod_vect, norma

def calcular_area_triangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3):
    "x1,y1,z1 hacen referencia a las coordenadas del primer vector, x2,y2,z2 a las del segundo y x3,y3,z3 al del tercero"
    vector_ab = diferencia(x2,y2,z2,x1,y1,z1)
    vector_ac = diferencia(x3,y3,z3,x1,y1,z1)

    "Desarmamos la tupla para poder utilizar las coordenadas i,j,k para calcular el Producto Vectorial"
    i1,j1,k1 = vector_ab
    i2,j2,k2 = vector_ac

    "Calculamos ABxAC"
    producto_vectorial = prod_vect(i1,j1,k1,i2,j2,k2)

    "Desarmamos la tupla del producto vectrial en p1 primera coord, p2 segunda y p3 tercera para poder utrilizarla en la func norma"
    p1,p2,p3 = producto_vectorial

    "Calculamos la norma ABxAC y lo dividimos entre 2 para poder hallar el area de un triangulo"
    area_triangulo = norma(p1,p2,p3)/2

    return area_triangulo

assert calcular_area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0) == 19.45507645834372
assert calcular_area_triangulo(10, 8, -11, -2, 35, 54, -31, 3, 0) == 1428.7111324547031
assert calcular_area_triangulo(15, 82, 0, -14, 4, 24, -2, 3, 0) == 1083.1095281641649

