class Transporte:
    def custo_viagem(self, distancia):
        raise NotImplementedError("Implemente em uma subclasse")


class Onibus(Transporte):
    def custo_viagem(self, distancia):
        return 4.50   

class Metro(Transporte):
    def custo_viagem(self, distancia):
        return 0.80 * distancia   


class BicicletaCompartilhada(Transporte):
    def custo_viagem(self, distancia):
        if distancia <= 5:
            return 0.0
        else:
            extra = distancia - 5
            return extra * 0.50


def mostrar_custos(transportes, distancia):
    print(f"Distância: {distancia} km")
    for t in transportes:
        custo = t.custo_viagem(distancia)
        print(f"{t.__class__.__name__}: R${custo:.2f}")  # polimorfismo[web:170][web:316]



meios = [Onibus(), Metro(), BicicletaCompartilhada()]
dist = float(input("Informe a distância da viagem (km): "))
mostrar_custos(meios, dist)
