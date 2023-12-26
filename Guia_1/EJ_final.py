'''
trigo, avena, cebada, centeno
'''

# def separar(entrada, con_tacc, sin_tacc):

#     tacc = ['trigo', 'avena', 'cebada', 'cente']

#     with open(entrada) as origen, open(con_tacc, "w") as destino_con_tacc, open(sin_tacc, "w") as destino_sin_tacc:
#         for linea in origen:
#             tiene_tacc = False
#             linea = linea.rstrip().split(';')
#             ingredientes = linea[2].split(',')

#             for ing in ingredientes:
#                 if ing in tacc:
#                     tiene_tacc = True  
            
#             if tiene_tacc:
#                 linea = ';'.join(linea)
#                 destino_con_tacc.write(f'{linea}\n')
#             else:
#                 linea = ';'.join(linea)
#                 destino_sin_tacc.write(f'{linea}\n')



