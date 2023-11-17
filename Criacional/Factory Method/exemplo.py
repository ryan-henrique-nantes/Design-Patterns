# Função que simula a criação de uma guitarra baseada no tipo selecionado
import tkinter as tk
from tkinter import scrolledtext
from abstract_factory import Tipo

# Classe para a interface de usuário
class GuitarApp:
    def __init__(self, master):
        self.master = master
        self.setup_ui()
        #self.factory = ConcreteGuitarFactory()

    def setup_ui(self):
        self.master.title("Seleção de Guitarra")

        # Variável para armazenar o tipo selecionado
        self.tipo_var = tk.IntVar(value=1)

        # RadioButtons
        for tipo in Tipo:
            tk.Radiobutton(self.master, text=tipo.name.replace("_", " "), variable=self.tipo_var, value=tipo.value).pack()

        # Memo
        self.memo = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=40, height=10)
        self.memo.pack()

        # Botão
        button = tk.Button(self.master, text="Criar Guitarra", command=self.on_button_click)
        button.pack()

    def on_button_click(self):
        selected_tipo = Tipo(self.tipo_var.get())
        resultado = self.factory.criar_guitarra(selected_tipo)
        self.memo.delete(1.0, tk.END)
        self.memo.insert(tk.INSERT, resultado)
    
root = tk.Tk()
app = GuitarApp(root)
root.mainloop()