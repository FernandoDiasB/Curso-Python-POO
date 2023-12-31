# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None


    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, nome):
        self._motor = nome

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome



carro1 = Carro('TR4')
carro2 = Carro('Focus')
motor1 = Motor('Diesel 2.0')
motor2 = Motor('Gasolina 2.0')
marca = Fabricante('Mitsubish')
marca2 = Fabricante('Ford')
print(f'O carro é um {marca.nome}, modelo {carro1.nome} com motor {motor1.nome}.')
print(f'O carro é um {marca2.nome}, modelo {carro2.nome} com motor {motor2.nome}.')