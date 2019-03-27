# -*- encoding: utf-8 -*-

# # imports
from coleta import Coleta
# # imports

# # variables

# # variables

# # classes


class ColetaFicha(Coleta):
    def getFileList(self):
        return [arquivo for arquivo in self.IDiretorio.listarArquivos() if "atendimento" in arquivo]

    def initSalvar(self, colunas=None, index=None):
        if colunas is None:
            colunas = ["Esférico", "Cilindro",
                       "Eixo", "Acuidade", "AR"]
            OlhoEsquerdo = [campo+" OE" for campo in colunas]
            OlhoDireito =  [campo+" OD" for campo in colunas]
            novasColunas = ["Data"]
            OlhoEsquerdo.extend(OlhoDireito)
            novasColunas.extend(OlhoEsquerdo)
            colunas = novasColunas
        if index is None:
            index = colunas[0]
        self.ISalvar = self.ISalvarcls(colunas, index)

    def initGrafico(self, width=None, height=None, widgets=None):
        if widgets is None:
            raise Exception("Não tem nada para mostrar!")
        if width is None:
            width = "500"
        if height is None:
            height = "300"
        self.IGrafico = self.IGraficacls(width,height,widgets)

    def initDiretorio(self,caminho):
        self.IDiretorio = self.IDiretoriocls(caminho)
        self._atual = self.getFileList()[0]

# # classes

# # functions

# # functions

# # main


def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()