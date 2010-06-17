def ponComa( numero ):
    '''Regresa numero como cadena con comas.
    
    numero es un entero
    no maneja signo ni punto decimal.'''

    cadenaNumero = str( numero )
    
    indiceCadena = len( cadenaNumero )
    
    while indiceCadena > 3:
    
        indiceCadena = indiceCadena - 3
        
        cadenaNumero = cadenaNumero[ :indiceCadena ] +  ',' + cadenaNumero[ indiceCadena: ]
        
    return cadenaNumero

if __name__ == '__main__':

    for datoDePrueba in [ '1000' ]:
    
        print ( datoDePrueba , ponComa( datoDePrueba ) )

