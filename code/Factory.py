from tkinter import *
import UserInterface

UI = Tk()
UI.configure(bg='lightgreen')


class Checkbar(Frame):
    def __init__(self, parent=None, picks=[]):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            check = Checkbutton(self, text=pick, variable=var)
            check.configure(bg='lightgreen', bd=1)
            check.pack(anchor=W, expand=YES)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)


class UIFactory(object):
    def factory(type):
        if type == "Button": return ButtonBuilder()
        if type == "Label": return LabelBuilder()
        if type == "Radio": return RadioBuilder()
        if type == "Entry": return EntryBuilder()
        if type == "Matrix": return MatrixBuilder()
        assert 0, "Bad element: " + type

    factory = staticmethod(factory)


class ButtonBuilder(UIFactory):
    def build(self, text, command, column, row, fg='black', bg='lightgrey',
              sticky=N + S + W + E, padx=0, pady=0, ipadx=0, ipady=0):
        b = Button(UI, text=text, command=command)
        b.configure(bg=bg, fg=fg)
        b.grid(column=column, row=row, sticky=sticky,
               padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)


class LabelBuilder(UIFactory):
    def build(self, vtext, column, row, columnspan=1, rowspan=1,
              font="12", bg='lightgreen', fg='black',
              sticky=N + S, padx=0, pady=0, ipadx=0, ipady=0):
        l = Label(UI, text=vtext, font=font)
        l.configure(bg=bg, fg=fg)
        l.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan,
               sticky=sticky, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)


class RadioBuilder(UIFactory):
    def build(self, vtext, indicatoron, variable, value,
              column, row, sticky=N + S + W + E, padx=0, pady=2, ipadx=0, ipady=0):
        r = Radiobutton(UI, text=vtext, indicatoron=indicatoron,
                        variable=variable, value=value)
        r.grid(column=column, row=row, sticky=sticky,
               padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)


class EntryBuilder(UIFactory):
    def build(self, name, col, row, padx=0):
        name.grid(column=col, row=row, padx=padx)


class MatrixBuilder(UIFactory):
    matrix = []
    data = []

    def build(self, col, vrow):
        matrix = [Checkbar(UI, ['', '', '', '', '', '', '', '']), Checkbar(UI, ['', '', '', '', '', '', '', '']),
                  Checkbar(UI, ['', '', '', '', '', '', '', '']), Checkbar(UI, ['', '', '', '', '', '', '', '']),
                  Checkbar(UI, ['', '', '', '', '', '', '', '']), Checkbar(UI, ['', '', '', '', '', '', '', '']),
                  Checkbar(UI, ['', '', '', '', '', '', '', '']), Checkbar(UI, ['', '', '', '', '', '', '', ''])]
        for create in range(0, len(matrix)):
            matrix[create].grid(column=create + col, row=vrow, rowspan=10)
        self.matrix = matrix
        return self

    def getstates(self):
        data = []
        for i in range(len(self.matrix)):
            data.append(list(self.matrix[i].state()))
        self.data = data


#####__Test-Stuff__####        
if __name__ == "__main__":
    abc = IntVar()
    abc.set(0)
    def destroy():
        print('ende')
    def hello():
        matrix1.getstates()
        print(matrix1.data)
    # matrix1 = UIFactory.factory('Matrix').build(0, 0)
    UIFactory.factory('Button').build('HI', hello, 10).frow(1)
    UI.mainloop()
