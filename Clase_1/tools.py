def ponComa( numero ):
    '''Regresa numero como cadena con comas.
    
    numero es un entero
   ya maneja punto decimal
   pero signo todavia no.'''

    entero, punto, decimales  = str( numero ).partition('.')
     
    cadenaNumero = str(entero)
    
    indiceCadena = len( cadenaNumero )
    
    if cadenaNumero[0:1] == '-':
        
        
        indiceCadena = indiceCadena - 1


    if indiceCadena < 3:
    
        return  cadenaNumero
        
    else:
    
        while indiceCadena > 3:
    
            indiceCadena = indiceCadena - 3
        
            cadenaNumero = cadenaNumero[ :indiceCadena ] +  ',' + cadenaNumero[ indiceCadena: ]
        
        return  cadenaNumero + punto + decimales        
    

if __name__ == '__main__':

    for datoDePrueba in [ '-123', '1234', '-123456789', '-123456789.11111', '-99999999999999999.99999999999999' ]:
    
        print ( datoDePrueba , ponComa( datoDePrueba ) )

''' By richistron@gmail.com'''

