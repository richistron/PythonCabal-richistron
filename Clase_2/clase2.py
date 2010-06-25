class Robot:
    "Un robot con nombre, posición y dirección."

    def __init__( self, nombre, posicion=(0,0) , direccion='N' ):
        "Constructor"
        self.nombre = nombre
        self.x, self.y = posicion
        self.direccion = direccion

    def avanza( self, direccion='' ):
        "Avanza posición del robot y regresa nueva posición.  Opcionalmente, cambia su dirección."
        if direccion:
            self.direccion = direccion
        if self.direccion == 'N':
            self.y = self.y + 1
        elif self.direccion == 'E':
            self.x = self.x + 1
        elif self.direccion == 'S':
            self.y = self.y - 1
        elif self.direccion == 'O':
            self.x = self.x - 1
        return self.x,self.y

class RobotPlus( Robot ):
    "Robot que reporta."

    def reporta( self ):
        return 'Soy ' + self.nombre + ' y estoy en (' + str(self.x) + ', ' + str(self.y) + '), ' + self.direccion

    def __repr__( self ):
        return self.reporta()

