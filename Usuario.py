class Usuario:

    def __init__(self, nombre, deposito, retiro, balance, transferencia):
        self.nombre = nombre
        self.hacer_deposito = deposito
        self.hacer_retiro = retiro
        self.mostrar_balance_usuario = balance
        self.transferir_dinero = transferencia

#Usuario1: 3 depósitos y 1 giro, obtener balance
    def mov_usuario1(self):
        self.mostrar_balance_usuario = (self.hacer_deposito * 3) - (self.hacer_retiro)

#Usuario2: 2 depósitos y 2 giros, obtener balance
    def mov_usuario2(self):
        self.mostrar_balance_usuario = (self.hacer_deposito * 2) - (self.hacer_retiro * 2)

#Usuario3: 1 depósito y 3 giros, obtener balance
    def mov_usuario3(self):
        self.mostrar_balance_usuario = (self.hacer_deposito) - (self.hacer_retiro * 3)