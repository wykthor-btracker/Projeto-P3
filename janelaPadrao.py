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
    def __init__(self, inst):
        self.inst = inst

        widgets = self.tkDrawWidgets()
        self.inst.initGrafico(widgets=widgets)

    def coletarDados(self):
        dados = self.inst.coletarDados()
        for widget, fields in dados.items():
            if isinstance(widget, iGT.TextWidgets):
                self.inst.adicionarDados(fields)
        self.proximoArquivo()

    def tkDrawWidgets(self):
        campos = iGT.TextWidgets([])
        camposTexto = self.inst.ISalvar.colunas
        campos.generateWidgets(camposTexto, iGT.CampoTexto)
        botoes = self.tkDrawBotoes(camposTexto)
        return [campos]+botoes

    def proximoArquivo(self):
        self.inst.proximoArquivo()
        self.inst.abrirArquivoAtual()

    def anteriorArquivo(self):
        self.inst.anteriorArquivo()
        self.inst.abrirArquivoAtual()

    def tkDrawBotoes(self, camposTexto):
        salvar = iGT.Botao("Salvar", len(camposTexto), 0, lambda: self.coletarDados(), [])
        anterior = iGT.Botao("Anterior", salvar.row+1, 0, lambda: self.anteriorArquivo())
        proximo = iGT.Botao("Proximo", anterior.row,   1, lambda: self.proximoArquivo())
        finalizar = iGT.Botao("Finalizar", salvar.row, 1, lambda : self.inst.fecharInterface())
        # erro = gtk.Botao("Erro",proximo.row+1,0,lambda:)
        return [salvar, anterior, proximo, finalizar]


class JanelaTkPadraoFicha(JanelaTkPadrao):
    def tkDrawBotoes(self, camposTexto):
        botoes = super().tkDrawBotoes(camposTexto)
        row = max(botao.row for botao in botoes)
        iGT.TextoTitulo("Data: {}".format(self.inst))

def main():
    return None

# # main 


if __name__ == "__main__":
    main()