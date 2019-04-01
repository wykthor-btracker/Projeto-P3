# -*- encoding: utf-8 -*-

# # imports
import interface
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

    def _extractFileNumber(self,file):
        # "1 - FICHA DE ATENDIMENTO.pdf.pdf"
        return int(file.split("-")[0].strip())

    def _getOrderedFileList(self):
        arquivos = self.IDiretorio.listarArquivos()
        arquivos = sorted(arquivos, key=lambda arquivo: self._extractFileNumber(arquivo.getFileName()))
        return arquivos

    def abrirDiretorio(self, path):
        self.IDiretorio.abrirDiretorio(path)

    def abrirArquivoAtual(self):
        self._atual.abrir()

    def proximoArquivo(self):
        arquivos, indexAtual = self._getCurrFileIndex()
        self._atual = arquivos[(indexAtual+1) % len(arquivos)]

    def anteriorArquivo(self):
        arquivos, indexAtual = self._getCurrFileIndex()
        self._atual = arquivos[(indexAtual-1) % len(arquivos)]

    def coletarDados(self):
        return self.IGrafico.coletarDados()

    def salvarDados(self, title):
        self.ISalvar.saveToFile(title)

    def adicionarDados(self,listaDeDados):
        self.ISalvar.append(listaDeDados, True)

    def desenharInterface(self):
        self.IGrafico.desenharInterface()

    def fecharInterface(self):
        self.IGrafico.fecharInterface()
# # classes

# # functions

# # functions

# # main
def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()