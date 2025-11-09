from quarto import Quarto

quarto1 = Quarto(101, "Simples")
quarto2 = Quarto(102, "Duplo")

print("Estado inicial:")
quarto1.exibir_dados()
quarto2.exibir_dados()

print("\nReservando quarto 101...")
quarto1.reservar()

print("\nEstado após reserva:")
quarto1.exibir_dados()
quarto2.exibir_dados()
