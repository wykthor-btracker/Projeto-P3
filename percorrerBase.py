# -*- encoding: utf-8 -*-

# # imports
import interface
import os
import subprocess
# # imports

# # variables

# # variables

# # classes


class OSDiretorio(interface.Diretorio):
    def __init__(self,caminho):
        super().__init__(caminho)
        self.classeArquivo = BrowserArquivo

    def isFile(self,caminho):
        return os.path.isfile(caminho)

    def isFolder(self,caminho):
        return os.path.isdir(caminho)

    def abrirArquivo(self,caminho):
        self.classeArquivo(caminho).abrir()

    def listarArquivos(self):
        return [self.classeArquivo(file) for file in os.listdir(self.caminho) if self.isFile(file)]

    def listarDiretorios(self):
        return [OSDiretorio(folder) for folder in os.listdir(self.caminho) if self.isFolder(folder)]

    def irParaDiretorio(self,caminho):
        os.chdir(caminho)
        self.caminho = caminho


class BrowserArquivo(interface.Arquivo):
    def __init__(self,caminho):
        super().__init__(caminho)

    def abrir(self):
        subprocess.Popen(["firefox",self.caminho])

    def ler(self):
        return Exception("Função não definida")

# # classes

# # functions

# # functions

# # main
def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()