
class ViajeroFrecuente:
    __num_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0
    def __init__(self,num,dni,nombre,apellido,millas):
        self.__num_viajero = num
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas
    def get_numeroViajero(self):
        return self.__num_viajero
    def __str__(self):
        return "{}   {}   {}   {}   {}".format(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)
    def cantidadTotalMillas(self):
        return (self.__millas_acum)
    def acumularMilas(self,m):
        self.__millas_acum += m
        return(self.__millas_acum)
    def canjearMillas(self,millas_canje):
        if (millas_canje <= self.__millas_acum):
            return (self.__millas_acum - millas_canje)
        else: print("error en la operacion, la cantidad de millas a canjear"
                        "es mayor a la cantidad de millas acumuladas")
