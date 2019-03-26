# -*- encoding: utf-8 -*-

# # imports
import interface
import tkinter as tk
# # imports

# # variables

# # variables

# # classes


class JanelaTkinter(interface.InterfaceGrafica):
    def __init__(self, width, height, Widgets):
        super().__init__(width, height, Widgets)
        self.rootInst = tk.Tk()

    def desenharInterface(self):
        self.desenharWidgets()
        self.rootInst.mainloop()

    def desenharWidgets(self):
        for widget in self.Widgets:
            widget.draw(self.rootInst)

    def coletarDados(self):
        result = {}
        for widget in self.Widgets:
            result[widget] = widget.getCampos()
        return result


class Botao(interface.DrawableWidget):
    def __init__(self,titulo, row, column, funcao,args=None):
        self.titulo = titulo
        self.funcao = funcao
        self.row = row
        self.column = column
        if args is None:
            args = list()
        self.args = args
        self.botao = None

    def draw(self, root):
        self.botao = tk.Button(root,text=self.titulo, command=lambda: self.funcao(*self.args)).grid(row=self.row, column=self.column, pady=4)

    def getCampos(self):
        return self.botao


class WidgetList(interface.DrawableWidget):
    def __init__(self, widgets):
        self.widgets = widgets

    def draw(self, inst):
        for widget in self.widgets:
            widget.draw(inst)

    def getCampos(self):
        resultado = {}
        for widget in self.widgets:
            resultado[widget.titulo] = widget.getCampos()
        return resultado


class TextWidgets(WidgetList):
    def generateWidgets(self, fields, cls, orientation="vertical"):
        start = self.getWidgetsListSize()
        for index in range(len(fields)):
            if orientation=="vertical":
                self.widgets.append(cls(fields[index], index+start, 0))
            else:
                self.widgets.append(cls(fields[index], 0, index+start))

    def getWidgetsListSize(self):
        return len(self.widgets)


class CampoTexto(interface.DrawableWidget):
    def __init__(self, titulo, row, column):
        self.titulo = titulo
        self.campos = []
        self.row = row
        self.column = column
        self.campo = None

    def draw(self, root):
        tk.Label(root, text=self.titulo).grid(row=self.row)
        campo = tk.StringVar()
        entradaTexto = tk.Entry(root, textvariable=campo)
        entradaTexto.grid(row=self.row, column=1)
        self.campo = campo

    def getCampos(self):
        return self.campo.get()


# # classes

# # functions

# # functions

# # main
def main(*args, **kwargs):
    campos = ["Oi","Tudo bom","iai", "FOFOFOFOFO"]
    coisas = []
    for index in range(len(campos)):
        coisas.append(CampoTexto(campos[index],index,0))
    wid = TextWidgets(coisas)
    botao = Botao("Hi",4,0,lambda x:print(x),[5])
    botoes = WidgetList([botao])
    jan = JanelaTkinter(400,400,[wid,botoes])
    jan.desenharInterface()
    print(jan.coletarDados())
    return


# # main 

if __name__ == "__main__":
    main()