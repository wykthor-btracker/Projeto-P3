# -*- encoding: utf-8 -*-

# # imports
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

    def checarDatas(self):
        arquivos = self.inst.IDiretorio.listarArquivos()
        for arquivo in arquivos:
            if "descri" in arquivo:
                arquivo.abrir()

    def tkDrawBotoes(self, camposTexto):
        salvar = iGT.Botao("Salvar", len(camposTexto), 0, self.coletarDados, [])
        anterior = iGT.Botao("Anterior", salvar.row+1, 0, self.anteriorArquivo)
        proximo = iGT.Botao("Proximo", anterior.row,   1, self.proximoArquivo)
        finalizar = iGT.Botao("Finalizar", salvar.row, 1, self.inst.fecharInterface)
        # erro = gtk.Botao("Erro",proximo.row+1,0,lambda:)
        return [salvar, anterior, proximo, finalizar]


class JanelaTkPadraoFicha(JanelaTkPadrao):

    def tkDrawBotoes(self, camposTexto):
        botoes = super().tkDrawBotoes(camposTexto)
        row = max(botao.row for botao in botoes)
        data = iGT.TextoTitulo("Data = {}".format(self.inst.data), row=row+1, column=0)  # TODO FIGURE THIS OUT
        return botoes+[data]

    def coletarDados(self):
        super().coletarDados()
        self.inst.fecharInterface()


class JanelaTkPadraoProntuario(JanelaTkPadrao):
    def __init__(self,inst):
        super().__init__(inst)
        self.fichas = 0

    def coletarDados(self):
        super().coletarDados()
        self.fichas += 1
        if self.fichas == 2:
            self.inst.fecharInterface()

    def tkDrawBotoes(self, camposTexto):
        botoes = super().tkDrawBotoes(camposTexto)
        row = max(botao.row for botao in botoes)
        checarDatas = iGT.Botao("Checar Datas", row+1, 0, self.checarDatas)
        return botoes+[checarDatas]


def main():
    return None

# # main 


if __name__ == "__main__":
    main()