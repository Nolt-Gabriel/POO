class Exportador:

    def exportar(self, dados):
        raise NotImplementedError("Execute em uma subclasse")


class ExportadorPDF(Exportador):

    def exportar(self, dados):
        print(f"Exportando dados para PDF: {dados}")


class ExportadorCSV(Exportador):

    def exportar(self, dados):
        print(f"Exportando dados para CSV: {dados}")


class ExportadorJSON(Exportador):

    def exportar(self, dados):
        print(f"Exportando dados para JSON: {dados}")


def processar_exportacao(exportador: Exportador, dados):
    
    exportador.exportar(dados)



dados = {"nome": "Ana", "idade": 25}

exportadores = [
    ExportadorPDF(),
    ExportadorCSV(),
    ExportadorJSON()
]

for exp in exportadores:
    processar_exportacao(exp, dados)
