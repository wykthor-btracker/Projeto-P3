# -*- encoding: utf-8 -*-

# # imports
from pandasSave import SalvarDados
from percorrerBase import OSDiretorio
import interfaceGrafTk as iGT
# # imports

# # variables

# # variables

# # classes

# # classes

# # functions

# # functions

# # main


class JanelaTkPadrao:
    def __init__(self, path, inst):
        self.path = path
        self.inst = inst(iGT.JanelaTkinter, OSDiretorio, SalvarDados)

    def coletarDados(self):
        dados = self.inst.coletarDados()
        for widget, fields in dados.items():
            if isinstance(widget, iGT.TextWidgets):
                self.inst.adicionarDados(fields)

    def coletar(self):
        self.initInstances()
        self.inst.abrirArquivo()
        self.inst.desenharInterface()
        return self.inst.ISalvar.getDataObject()

    def initInstances(self):
        self.inst.initSalvar()
        self.inst.initDiretorio(self.path)
        widgets = self.tkDrawWidgets()
        self.inst.initGrafico(widgets=widgets)

    def tkDrawWidgets(self):
        campos = iGT.TextWidgets([])
        camposTexto = self.inst.ISalvar.colunas
        campos.generateWidgets(camposTexto, iGT.CampoTexto)
        anterior, proximo, salvar = self.tkDrawBotoes(camposTexto)
        return [campos, salvar, proximo, anterior]

    def tkDrawBotoes(self, camposTexto):
        salvar = iGT.Botao("Ok", len(camposTexto), 0, lambda: self.coletarDados(), [])
        anterior = iGT.Botao("Anterior", salvar.row, 1, lambda: self.inst.anteriorArquivo())
        proximo = iGT.Botao("Proximo", salvar.row, anterior.column + 1, lambda: self.inst.proximoArquivo())
        # erro = gtk.Botao("Erro",proximo.row+1,0,lambda:)
        return anterior, proximo, salvar


def main():
    return None

# # main 


if __name__ == "__main__":
    main()