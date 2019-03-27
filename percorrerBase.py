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
        self.classeArquivo = OSArquivo

    def makeFileHandler(self,caminho):
        return self.classeArquivo(os.path.join(self.caminho,caminho))

    def makeFolderHandler(self,caminho):
        return OSDiretorio(os.path.join(self.caminho,caminho))

    def isFile(self,caminho):
        return os.path.isfile(os.path.join(self.caminho, caminho))

    def isFolder(self,caminho):
        return os.path.isdir(os.path.join(self.caminho, caminho))

    def abrirArquivo(self,caminho):
        self.classeArquivo(caminho).abrir()

    def listarArquivos(self):
        return [self.makeFileHandler(file) for file in os.listdir(self.caminho) if
                self.isFile(file)]

    def listarDiretorios(self):
        return [self.makeFolderHandler(folder) for folder in os.listdir(self.caminho) if self.isFolder(folder)]

    def irParaDiretorio(self,caminho):
        os.chdir(caminho)
        self.caminho = caminho

    def getFolderName(self):
        basename = self.caminho
        basename = os.path.basename(basename)
        return basename

    def __repr__(self):
        return "OSDiretorio Instance: {}".format(self.caminho)

    def __lt__(self, other):
        if isinstance(other, type(self)) and hasattr(other, "caminho"):
            return self.caminho < other.caminho


class OSArquivo(interface.Arquivo):
    def __init__(self,caminho):
        super().__init__(caminho)

    def abrir(self):
        subprocess.Popen(["firefox",self.caminho])

    def ler(self):
        return Exception("Função não definida")

    def getFileName(self):
        basename = self.caminho
        basename = os.path.basename(basename)
        if "." in basename:
            basename = basename.split(".")[0]
        return basename

    def __eq__(self, other):
        if hasattr(other, "caminho"):
            return self.caminho == other.caminho and isinstance(self, type(other))
        else:
            return False

    def __contains__(self, item):
        if isinstance(item,str):
            return item.lower() in self.caminho.lower()

    def __repr__(self):
        return "OSArquivo Instance: {}".format(self.caminho)

    def __lt__(self,other):
        if isinstance(other,type(self)) and hasattr(other,"caminho"):
            return self.caminho < other.caminho
# # classes

# # functions

# # functions

# # main
def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()