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
        self.rootInst.geometry("{}x{}".format(width,height))
        self.rootInst.attributes("-topmost", True)

    def desenharInterface(self):
        self.desenharWidgets()
        self.rootInst.mainloop()

    def desenharWidgets(self):
        for widget in self.Widgets:
            widget.draw(self.rootInst)

    def coletarDados(self):
        result = {}
        for widget in self.Widgets:
            result[widget] = widget.coletarDados()
        return result

    def fecharInterface(self):
        try:
            self.rootInst.destroy()
        except Exception as e:
            print("Interface já foi fechada: \n{}".format(e))


class Botao(interface.DrawableWidget):
    def __init__(self,titulo, row, column, funcao,args=None):
        self.titulo = titulo
        self.funcao = funcao
        self.row = row
        self.column = column
        if args is None:
            args = list()  # Initializing mutable objects as default parameters cause them to be evaluated at compile
            #                time, causing instances to share the mutable, instead of creating their own.
        self.args = args
        self.botao = None

    def draw(self, root):
        self.botao = tk.Button(root,text=self.titulo, command=lambda: self.funcao(*self.args)).grid(row=self.row, column=self.column, pady=4)

    def coletarDados(self):
        return self.botao


class WidgetList(interface.DrawableWidget):
    def __init__(self, widgets):
        self.widgets = widgets

    def draw(self, inst):
        for widget in self.widgets:
            widget.draw(inst)

    def coletarDados(self):
        resultado = {}
        for widget in self.widgets:
            resultado[widget.titulo] = widget.coletarDados()
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
        self._fazerLinhaTitulo(root)
        campo = self._fazerCampoTexto(root)
        self.campo = campo

    def _fazerCampoTexto(self, root):
        campo = tk.StringVar()
        entradaTexto = tk.Entry(root, textvariable=campo)
        entradaTexto.grid(row=self.row, column=self.column + 1)
        return campo

    def _fazerLinhaTitulo(self, root):
        tk.Label(root, text=self.titulo).grid(row=self.row, column=self.column)

    def coletarDados(self):
        return self.campo.get()


class TextoTitulo(CampoTexto):
    def __init__(self, titulo, row, column):
        super().__init__(titulo, row, column)

    def draw(self, root):
        self._fazerLinhaTitulo(root)

    def coletarDados(self):
        return self.titulo

# # classes

# # functions

# # functions

# # main
def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()