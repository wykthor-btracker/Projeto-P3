# -*- encoding: utf-8 -*-

# # imports
import interface
from abc import abstractmethod
# # imports

# # variables

# # variables

# # classes


class Coleta(interface.Coleta):
    def __init__(self, IGraficacls, IDiretoriocls, ISalvarcls):
        super().__init__(IGraficacls, IDiretoriocls, ISalvarcls)
        self._atual = None

    def _getCurrFileIndex(self):
        arquivos = self.getFileList()
        indexAtual = arquivos.index(self._atual)
        return arquivos, indexAtual

    def abrirDiretorio(self, path):
        self.IDiretorio.abrirDiretorio(path)

    def abrirArquivo(self):
        self._atual.abrir()

    def proximoArquivo(self):
        arquivos, indexAtual = self._getCurrFileIndex()
        self._atual = arquivos[indexAtual+1%len(arquivos)]
        self.abrirArquivo()

    def anteriorArquivo(self):
        arquivos, indexAtual = self._getCurrFileIndex()
        self._atual = arquivos[indexAtual-1%len(arquivos)]

    def coletarDados(self):
        return self.IGrafico.coletarDados()

    def salvarDados(self, title):
        self.ISalvar.saveToFile(title)

    def desenharInterface(self):
        self.IGrafico.desenharInterface()
# # classes

# # functions

# # functions

# # main
def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()