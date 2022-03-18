import math

global posicion


def no_regla_1():
    sujeto_no_regla = "(O_o)"
    return sujeto_no_regla


class Emojis:
    def __init__(self):
        super(Emojis, self).__init__()
        self.sujeto_completo = "(-_-)"
        self.sujeto_lateral_izquierda = "_-)"
        self.sujeto_lateral_derecha = "(-_"
        self.sujeto_parcial_derecha = "(-_-"
        self.sujeto_parcial_izquierda = "-_-)"
        self.sujeto_final_derecha = "(-"
        self.sujeto_final_izquierda = "-)"

    def regla_1(self, num):
        try:
            if 0 < num < 256:
                self.par_vs_impar(num)
            else:
                caracter = no_regla_1()
                print(caracter)
        except (ValueError, Exception):
            no_regla_1()

    def par_vs_impar(self, num):
        if num % 2 == 0:
            self.resultante_par(num)
        else:
            self.resultante_impar(num)

    def resultante_par(self, num):
        print("En esta multitud hay", num, "sujeto/s")
        sujetos = []
        if num == 1:
            print(self.sujeto_completo)
        elif num > 1:
            mitad = self.medio(num)
            medio = mitad
            self.numeros(num)
            final = self.sujeto_final(num)
            for i in range(1, mitad):
                sujetos.append(self.sujeto_lateral_derecha)
            for x in range(mitad, final[1]+1):
                sujetos.insert(x, self.sujeto_lateral_izquierda)

            sujetos[mitad - 1] = self.sujeto_completo
            for h in range(mitad, final[1]+1):
                mitad += 2
                if mitad < final[1]:
                    sujetos[mitad] = self.sujeto_parcial_izquierda
                    mitad += 1

            for h in range(medio):
                medio -= 4
                if medio > 0:
                    sujetos[medio] = self.sujeto_parcial_derecha
                    medio += 1

            if num >= 7:
                sujetos[final[0]-1] = self.sujeto_final_derecha
                sujetos[final[1]-1] = self.sujeto_final_izquierda
        print(sujetos)

    def resultante_impar(self, num):
        print("En esta multitud hay", num, "sujeto/s")
        sujetos = []
        if num == 1:
            print(self.sujeto_completo)
        elif num > 1:
            mitad = self.medio(num)
            medio = mitad
            self.numeros(num)
            final = self.sujeto_final(num)
            for i in range(1, mitad):
                sujetos.append(self.sujeto_lateral_derecha)
            for x in range(mitad, final[1]+1):
                sujetos.insert(x, self.sujeto_lateral_izquierda)

            sujetos[mitad - 1] = self.sujeto_completo
            for h in range(mitad, final[1]+1):
                mitad += 2
                if mitad < final[1]:
                    sujetos[mitad] = self.sujeto_parcial_izquierda
                    mitad += 1

            for h in range(medio):
                medio -= 4
                if medio > 0:
                    sujetos[medio] = self.sujeto_parcial_derecha
                    medio += 1

            if num >= 7:
                sujetos[final[0]-1] = self.sujeto_final_derecha
                sujetos[final[1]-1] = self.sujeto_final_izquierda
            print(sujetos)

    @staticmethod
    def numeros(num):
        cadena = []
        for i in range(1, num + 1):
            cadena.append(i)
        return cadena[0], cadena[-1], cadena

    def sujeto_final(self, num):
        global posicion
        posicion = self.numeros(num)
        return posicion[0], posicion[1]

    @staticmethod
    def medio(num):
        mitad = math.ceil(num / 2)
        return mitad


if __name__ == "__main__":
    try:
        numero = int(input("Ingresa un número: "))
        multitud = Emojis()
        multitud.regla_1(numero)
    except (ValueError, Exception):
        no_regla_1()
