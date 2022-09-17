from Usuario import Usuario

Usuario1 = Usuario("Edward", 25000, 10000, 0, 20000)
Usuario2 = Usuario("Iván", 30000, 15000, 0, 0)
Usuario3 = Usuario("María Elena", 25000, 10000, 0, 0)

Usuario1.mov_usuario1()
print("Usuario:",Usuario1.nombre,", Balance:",Usuario1.mostrar_balance_usuario)

Usuario2.mov_usuario2()
print("Usuario:",Usuario2.nombre,", Balance:",Usuario2.mostrar_balance_usuario)

Usuario3.mov_usuario3()
print("Usuario:",Usuario3.nombre,", Balance:",Usuario3.mostrar_balance_usuario)

#BONUS: Transferencia del 1er al 3er usuario, obtener balance de ambos
def transf_dinero():
        if Usuario1.transferir_dinero > 0:
            Usuario3.mostrar_balance_usuario = Usuario3.mostrar_balance_usuario + Usuario1.transferir_dinero
            Usuario1.mostrar_balance_usuario = Usuario1.mostrar_balance_usuario - Usuario1.transferir_dinero
            print("Balance final",Usuario1.nombre,":",Usuario1.mostrar_balance_usuario,"; Balance final",Usuario3.nombre,":",Usuario3.mostrar_balance_usuario)

transf_dinero()