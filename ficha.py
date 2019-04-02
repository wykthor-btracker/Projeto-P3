# -*- encoding: utf-8 -*-

# # imports
from coleta import Coleta
import interface


# # imports

# # variables

# # variables

# # classes


class ColetaFicha(Coleta):
    def __init__(self, IGraficacls, IDiretoriocls, ISalvarcls, Arquivo, data):
        super().__init__(IGraficacls, IDiretoriocls, ISalvarcls)
        if not isinstance(Arquivo, interface.Arquivo):
            raise Exception("{} é do tipo errado! Instância de {} esperado.".format(Arquivo, interface.Arquivo))
        self.Arquivo = Arquivo
        self.data = data

    def getFileList(self):
        return [arquivo for arquivo in self.IDiretorio.listarArquivos() if "atendimento" in arquivo]

    def initSalvar(self, colunas=None, index=None):
        if colunas is None:
            colunas = self._fazerColunasPadrao()
        if index is None:
            index = colunas[0]
        self.ISalvar = self.ISalvarcls(colunas, index)

    def _fazerColunasPadrao(self):
        colunas = ["Esférico", "Cilindro",
                   "Eixo", "Acuidade", "AR"]
        OlhoEsquerdo = [campo + " OE" for campo in colunas]
        OlhoDireito = [campo + " OD" for campo in colunas]
        novasColunas = ["Data"]
        OlhoEsquerdo.extend(OlhoDireito)
        novasColunas.extend(OlhoEsquerdo)
        colunas = novasColunas
        return colunas

    def initGrafico(self, width=None, height=None, widgets=None):
        if widgets is None:
            raise Exception("Não tem nada para mostrar!")
        if width is None:
            width = "300"
        if height is None:
            height = "350"
        self.IGrafico = self.IGraficacls(width, height, widgets)

    def initDiretorio(self, caminho):
        self.IDiretorio = self.IDiretoriocls(caminho)
        self._atual = self.getFileList()[0]


# How to make this better?


class ColetaFichaPre(ColetaFicha):

    def _fazerColunasPadrao(self):
        colunas = super()._fazerColunasPadrao()
        return list(
            map(
                lambda x: "Pré-" + x, colunas))

    def getFileList(self):
        arquivos = self._getOrderedFileList()
        limit = arquivos.index(self.Arquivo)
        arquivos = [arquivo
                    for arquivo in arquivos[limit:]
                    if "atendi" in arquivo]

        return arquivos


class ColetaFichaPos(ColetaFicha):

    def _fazerColunasPadrao(self):
        colunas = super()._fazerColunasPadrao()
        return list(
            map(
                lambda x: "Pos-" + x, colunas
            ))

    def getFileList(self):
        arquivos = self._getOrderedFileList()
        limit = arquivos.index(self.Arquivo)
        arquivos = [arquivo
                    for arquivo in arquivos[:limit]
                    if "atendi" in arquivo]

        return arquivos


# # classes

# # functions

# # functions

# # main


def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()
