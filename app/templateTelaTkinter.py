class Tela9(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('text')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='text', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.055, rely = 0.1)

        self.botao = Button(self, text='text', font = 'Poppins-Regular.ttf', command=self.aa).place(relx=0.17,rely=0.6,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()