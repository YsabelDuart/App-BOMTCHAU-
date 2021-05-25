from tkinter import *
#----------------------TELA 2-----------------------
class Tela2(Toplevel): #Pagina do cadastro
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('CADASTRO')             # Inserindo nome da janela
        self.geometry('560x500+430+15')  # Inserindo tamanho da janela
        self.iconbitmap('bom.ico')  # Inserindo icone  # Iserindo icone
        self.configure(bg="#f7d6e0")       # Inserindo cor da tela
        # Inserindo texto
        Label(self, text='Nome de usuário: ', bg='#f7d6e0').place(relx=0.1, rely=0.67)
        Label(self, text='Senha:', bg='#f7d6e0').place(relx=0.1, rely=0.75)
        Label(self, text='Senha:', bg='#f7d6e0').place(relx=0.1, rely=0.83)
        # Comando para mudar escrita inserida na lacuna
        self.senha = StringVar()
        self.senha1 = StringVar()
        # Inserindo lacunas
        self.entra = Entry(self, bd=2).place(relx=0.1, rely=0.70)
        self.entra2= Entry(self, textvariable = self.senha, show = '*', bd=2).place(relx=0.1, rely=0.78)
        self.entra3 = Entry(self, textvariable = self.senha1, show = '*', bd=2).place(relx=0.1, rely=0.86)
        #Inserindo botão
        self.avancar = Button(self, text='LOGAR', font=('Arial', 10, 'bold'),bg = '#f7d6e0', command=exit).place(relx=0.35,rely=0.93,relwidth=0.3,)
        # Inserindo botão
        self.buton = Button(self, text='<-', command=self.onbotao, bg='#f7d6e0', bd=5).place(relx=0.05, rely=0.027,relwidth=0.088,relheight=0.037)
        #Inserindo imagem
        self.imaG = PhotoImage(file='silueta.png')
        self.imaG = self.imaG.subsample(4, 4)
        self.imag = Label(self, image=self.imaG, bd=1, bg ='#f7d6e0').place(relx=0.12, rely=0.16, relwidth=0.75, relheight=0.4)
    def onbotao(self): # Comando para voltar a tela anterior
        self.hide()
        self.abrir = Tela1
    def hide(self):  # Esconde a janela root
        self.withdraw()
#-------------------TELA 1-------------------------
class Tela1:
    def __init__ (self): #Inserindo funções
        self.root = root
        self.telinha()
        self.frame()
        self.wid()
        #self.texto()
        self.imagem()
        root.mainloop()
    def telinha(self):
        self.root.title('BOMTCHAU')       # Inserindo nome da janela
        self.root.geometry('560x500+430+15')    # Inserindo tamanho da janela
        self.root.iconbitmap('bom.ico')  # Inserindo icone
        #Inserindo cores na tela
    def frame(self):
        self.frame1 = Frame(self.root, bg='#c05299').place(relx=0, rely=0.001, relwidth=1, relheight=1)#porda
        self.frame2 = Frame(self.frame1, bg='#CF7EC5').place(relx=0.05, rely=0.025, relwidth=0.9, relheight=0.95)#meio
        # Inserindo botão
    def wid(self):
        self.avancar = Button(self.frame1, text='ENTRAR', bd = 0, font=('Cavolini', 10, 'bold'), bg='#c05299', command=self.clica).place(relx=0.35, rely=0.93, relwidth=0.3, relheight=0.04)
        #Inserindo Texto
    '''def texto(self):
        root.titulo= Label(self.frame1,text='BOMTCHAU',font='Century 14',bg='#CF7EC5').place(x=66, y=40)
        root.palavrinha = Label(self.frame1, text = 'Seja bem-vinda(o)', font = 'Broadway 12', bg='#CF7EC5').place(x= 168, y= 420)'''
        #Inserindo imagem
    def imagem(self):
        self.imagem = PhotoImage(file='cleber2.png')
        self.imagem = self.imagem.subsample(2, 2)
        self.imageg = Label(self.frame1, image=self.imagem, bg ='#CF7EC5').place(relx=0.09, rely=0.20, relwidth=0.82, relheight=0.70)
    def clica(self): #Comando para próxima tela
        self.hide()
        self.subTela = Tela2(self)
    def hide(self): # Escondendo tela
        self.root.withdraw()
    def show(self):  # Comando para destruir tela
        self.root.update()
        self.root.deiconify()
root = Tk()
Tela1()
