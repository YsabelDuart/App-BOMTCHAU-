#Telas

from tkinter import *

#------------TELA 4-------------

class PoemaBolha(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Poema Bolha')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Poema Bolha de\nSabão', bg='#A8E86E', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.12, rely = 0.05)



        text = Label(self, text='A bolinha de sabão\nVai voando lá no céu.\nO menino estica a mão\nMas estoura é no chapéu.\nEla é toda redondinha\nBrilha como diamante\nDiferente da andorinha\nQue some no horizonte.\nSe você já brincou\nTem boa lembrança\nNão deixem que digam que é coisa\nde criança.',
        
        bg='#7030A0', fg='#ffffff', font=('Poppins', 12, 'bold'))
        text.place(relx = 0.01,rely = 0.27)


        text = Label(self, text = '– Natália Crispim', bg='#7030A0', fg='#fff', font=('Poppins', 10, 'bold'))
        text.place(relx = 0.55, rely = 0.8)


        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.88,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def voltar(self):
        self.hide()
        self.volta = Infantil(self)

class PoemaSonhos(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Sonhos Agonizantes')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Sonhos Agonizantes', bg='#A8E86E', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.02, rely = 0.05)


        text = Label(self, text='Há dias que para mim,\nA vida é sem sentido,\nEntão me sinto assim:\nUm cão de rua perdido!\nUm animal sem dono,\nMinha alma então vagueia,\nVazia no abandono,\nSem paz, sem rumo, alheia!\nÀs vezes penso até\nQue o céu me esqueceu,\nQue já perdi a fé…\nMas sei que os sonhos meus,\nEmbora agonizantes,\nNão vão morrer sem Deus!',
        
        bg='#7030A0', fg='#ffffff', font=('Poppins', 12, 'bold'))
        text.place(relx = 0.11,rely = 0.15)
        
        text = Label(self, text = '– Elizeu Petrelli de Vitor ', bg='#7030A0', fg='#fff', font=('Poppins', 10, 'bold'))
        text.place(relx = 0.45, rely = 0.8)


        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.88,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def voltar(self):
        self.hide()
        self.volta = Drama(self)

class PoemaPlanta(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Poema Planta')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Poema Planta', bg='#A8E86E', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.2, rely = 0.05)


        text = Label(self, text='Sou a raiz que do mundo não vejo\nnada.\nPois estou enterrada.\nMeu caule é o tronco e o sustento,\nDos galhos para o crescimento.\nÉ na folha da planta que\nfunciona o pulmão.\nAjudar a respirar é minha função.\nA flor perfuma e enfeita a vegetação\nPara as crianças que nascerão.\nNo fruto as sementes estão\nno interior\nNovas plantinhas vêm do\nmeu amor.',
        
        bg='#7030A0', fg='#ffffff', font=('Poppins', 12, 'bold'))
        text.place(relx=0.01, rely = 0.2)


        text = Label(self, text = '– Natália Crispim', bg='#7030A0', fg='#fff', font=('Poppins', 10, 'bold'))
        text.place(relx = 0.55, rely = 0.8)


        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.88,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def voltar(self):
        self.hide()
        self.volta = Cultural(self)

class PoemaTransporte(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Poema Transporte')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Poema Transporte', bg='#A8E86E', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.07, rely = 0.05)


        textT = Label(self, text='O homem inventou a roda\nE logo surgiu a carroça.\nO carro precisa de motorista,\nMas a bike só um ciclista.\nA maria-fumaça\nFicou na lembrança.\nPosso ir de navio\nAté a França.\nSantos Dumont inventou o avião\nViagens surgiram de montão.\nPara chegar na lua,\nNão dá para ser de balão,\nSomente de foguete\nRealizo essa expedição.',
        
        bg='#7030A0', fg='#ffffff', font=('Poppins', 12, 'bold'))
        textT.place(relx=0.05, rely = 0.2)

        text = Label(self, text = '– Natália Crispim', bg='#7030A0', fg='#fff', font=('Poppins', 10, 'bold'))
        text.place(relx = 0.55, rely = 0.8)


        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.88,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def voltar(self):
        self.hide()
        self.volta = Cultural(self)

class PoemaEletricidade(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Poema Eletricidade')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Poema Eletricidade', bg='#A8E86E', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.04, rely = 0.05)

        text = Label(self, text='Se você usa geladeira\nNão marque bobeira\nUse com inteligência\nPara ela não faltar!\nNossa energia vem d’água\nÉ melhor economizar.\nEsse recurso precioso\nUm dia pode acabar.',
        
        bg='#7030A0', fg='#ffffff', font=('Poppins', 12, 'bold'))
        text.place(relx=0.15, rely = 0.3)

        text = Label(self, text = '– Natália Crispim', bg='#7030A0', fg='#fff', font=('Poppins', 10, 'bold'))
        text.place(relx = 0.55, rely = 0.8)


        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.88,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def voltar(self):
        self.hide()
        self.volta = Cultural(self)

class PoemaAgua(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Poema Agua')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Poema Agua', bg='#A8E86E', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.22, rely = 0.05)

        text = Label(self, text='Ela é uma beleza,\nFonte de grande riqueza,\nEstá em toda parte na natureza,\nTome cuidado na correnteza!\nSabe de quem estou falando?\nÉ a água escoando...',
        
        bg='#7030A0', fg='#ffffff', font=('Poppins', 12, 'bold'))
        text.place(relx=0.05, rely = 0.3)

        text = Label(self, text = '– Natália Crispim', bg='#7030A0', fg='#fff', font=('Poppins', 10, 'bold'))
        text.place(relx = 0.55, rely = 0.8)


        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.88,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def voltar(self):
        self.hide()
        self.volta = Cultural(self)

class GenerosP(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Escolha o conteúdo')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Escolha o genero ', bg='#7030A0', fg = '#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.1, rely = 0.07)

        self.imaG7 = PhotoImage(file='p1.png')
        self.imaG8 = PhotoImage(file='p2.png')
        self.imaG9 = PhotoImage(file='p3.png')

        self.botao1 = Button(self, image = self.imaG7, height = 75, width = 75, command = self.Cbtn1, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.02, rely=0.18, width=140, height=195)

        self.botao2 = Button(self, image = self.imaG8, width = 10, height = 10, command = self.Cbtn2, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.52, rely=0.18, width=140, height=195)

        self.botao3 = Button(self, image = self.imaG9, command = self.Cbtn3, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.28, rely=0.5, width=140, height=195)

        self.botaovoltar = Button(self, text='← Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.82,relwidth=0.7, relheight = 0.1)

    def Cbtn1(self):
        self.hide()
        self.abrir = Drama(self)

    def Cbtn2(self):
        self.hide()
        self.abrir = Infantil(self)

    def Cbtn3(self):
        self.hide()
        self.abrir = Cultural(self)

    def voltar(self):
        self.hide()
        self.volta = Escolha(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class Drama(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Dramatico')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Dramatico', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.28, rely = 0.03)

        self.poemaSonho = Button(self, bg = '#ED7D31', fg = '#fff', activebackground='#ED7D31', activeforeground = '#fff', text='Sonhos Agonizantes', font = 'Poppins-Regular.ttf', command=self.avancar).place(relx=0.17,rely=0.37,relwidth=0.7, relheight = 0.1)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def avancar(self):
        self.hide()
        self.avanca = PoemaSonhos(self)

    def voltar(self):
        self.hide()
        self.volta = GenerosP(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class Infantil(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Infantil')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Infantil', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.35, rely = 0.03)

        #self.poemaInfantil1 = Button(self, bg = '#ED7D31', fg = '#fff', activebackground='#ED7D31', activeforeground = '#fff', text='Poema da Criança', font = 'Poppins-Regular.ttf', command=self.pCrianca).place(relx=0.17,rely=0.25,relwidth=0.7, relheight = 0.1)

        self.poemaInfantil3 = Button(self, bg = '#ED7D31', fg = '#fff', activebackground='#ED7D31', activeforeground = '#fff', text='Poema da bolha de sabão', font = 'Poppins-Regular.ttf', command=self.pBolha).place(relx=0.17,rely=0.37,relwidth=0.7, relheight = 0.1)

        #self.poemaInfantil4 = Button(self, bg = '#ED7D31', fg = '#fff', activebackground='#ED7D31', activeforeground = '#fff', text='Poema dos Avós', font = 'Poppins-Regular.ttf', command=self.pAvos).place(relx=0.17,rely=0.49,relwidth=0.7, relheight = 0.1)


        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    '''def pCrianca(self):
        self.hide()
        self.avanca = PoemaCrianca(self)'''

    def pBolha(self):
        self.hide()
        self.avanca = PoemaBolha(self)

    '''def pAvos(self):
        self.hide()
        self.avanca = PoemaAvos(self)'''



    def voltar(self):
        self.hide()
        self.volta = GenerosP(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class Cultural(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Cultural')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Cultural', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.3, rely = 0.03)


        self.poemaCultural1 = Button(self, bg = '#ED7D31', fg = '#fff', activebackground='#ED7D31', activeforeground = '#fff', text='Poema da Planta', font = 'Poppins-Regular.ttf', command=self.pPlanta).place(relx=0.17,rely=0.25,relwidth=0.7, relheight = 0.1)

        self.poemaCultural2 = Button(self, bg = '#ED7D31', fg = '#fff', activebackground='#ED7D31', activeforeground = '#fff', text='Poema dos meios \nde transporte', font = 'Poppins-Regular.ttf', command=self.pTransporte).place(relx=0.17,rely=0.37,relwidth=0.7, relheight = 0.1)

        self.poemaCultural3 = Button(self, bg = '#ED7D31', fg = '#fff', activebackground='#ED7D31', activeforeground = '#fff', text='Poema da eletricidade', font = 'Poppins-Regular.ttf', command=self.pEletricidade).place(relx=0.17,rely=0.49,relwidth=0.7, relheight = 0.1)

        self.poemaCultural4 = Button(self, bg = '#ED7D31', fg = '#fff', activebackground='#ED7D31', activeforeground = '#fff', text='Poema Água', font = 'Poppins-Regular.ttf', command=self.pAgua).place(relx=0.17,rely=0.61,relwidth=0.7, relheight = 0.1)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)


    def pPlanta(self):
        self.hide()
        self.avanca = PoemaPlanta(self)

    def pTransporte(self):
        self.hide()
        self.avanca = PoemaTransporte(self)

    def pEletricidade(self):
        self.hide()
        self.avanca = PoemaEletricidade(self)

    def pAgua(self):
        self.hide()
        self.avanca = PoemaAgua(self)


    def voltar(self):
        self.hide()
        self.volta = GenerosP(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class Escolha(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('História ou Poema?')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Escolha', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.32, rely = 0.20)

        self.imghistoria = PhotoImage(file='historia.png')
        self.imgpoema = PhotoImage(file='poema.png')


        self.botaoH = Button(self, image = self.imghistoria,command=self.historia, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.02, rely=0.38, width=140, height=195)

        self.botaoP = Button(self, image = self.imgpoema,command=self.poema, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.52, rely=0.38, width=140, height=195)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def voltar(self):
        self.hide()
        self.volta = Tela7(self)
        

    def historia(self):
        self.hide()
        self.proxtela = GenerosH(self)

    def poema(self):
        self.hide()
        self.proxtela = GenerosP(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class Aventura(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Aventura')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Aventura', bg='#ED7D31', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.28, rely = 0.03)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

        self.hAventura = Button(self, bg = '#ED7D31', fg = '#fff', activebackground='#ED7D31', activeforeground = '#fff', text='O medo', font = 'Poppins-Regular.ttf', command=self.medo).place(relx=0.17,rely=0.37,relwidth=0.7, relheight = 0.1)


    def medo(self):
        self.hide()
        self.avanca = AventuraCasa(self)

    def voltar(self):
        self.hide()
        self.volta = GenerosH(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class AventuraCasa(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('O medo')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='O medo', bg='#ED7D31', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.35, rely = 0.05)


        text = Label(self, text=f'Bob era um menino sonhador. Sonhava\nviajar de avião. Mas também tinha medo\nde altura. No natal do ano 2014, Bob\nrecebeu um convite de um amigo para\npassar o natal em sua casa. o seu amigo\nmorava no Ceará. Bob ficou muito feliz\ncom o convite e decidiu enfrentar seus\nmedos.Então comprou sua passagem,\nfoi se preparando até o dia da viajem.\nChegou o grande dia, ele estava com\nmuito medo, mas não podia desistir.\nJá no aeroporto, ouviram a chamada:\n—Voo 588 o avião está abordo. Bob olha \npara o avião, seu coração bate forte,\nlogo após entra nele e deixa o medo para\ntrás. Chega ao seu destino, reencontra seu\namigo e teve uns dos seus melhores natais.\nApós essa viajem Bob nunca mais\nteve medo de altura.',
        
        bg='#7030A0', fg='#ffffff', font=('Poppins', 10, 'bold'), justify=CENTER)
        text.place(relx = 0.01,rely = 0.15)
        
        '''text = Label(self, text = '– Elizeu Petrelli de Vitor ', bg='#7030A0', fg='#fff', font=('Poppins', 10, 'bold'))
        text.place(relx = 0.45, rely = 0.8)'''


        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.88,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def voltar(self):
        self.hide()
        self.volta = Aventura(self)

class Fantasia(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Fantasia')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Fantasia', bg='#FE66CB', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.28, rely = 0.03)

        self.hFantasia = Button(self, bg = '#ED7D31', fg = '#fff', activebackground='#ED7D31', activeforeground = '#fff', text='Chapeuzinho Vermelho', font = 'Poppins-Regular.ttf', command=self.avancar).place(relx=0.17,rely=0.37,relwidth=0.7, relheight = 0.1)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)


    def avancar(self):
        self.hide()
        self.avanca = FantasiaChapeuzinho(self)

    def voltar(self):
        self.hide()
        self.volta = GenerosH(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class FantasiaChapeuzinho(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Chapeuzinho Vermelho')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Chapeuzinho Vermelho', bg='#FE66CB', fg='#ffffff', font=('Poppins', 18, 'bold'))
        text.place(relx=0.01, rely = 0.02)

        text = Label(self, text=f'Uma menina chamada Chapeuzinho\nVermelho foi visitar sua avó que morava\ndistante e estava doente. Sua mãe queria\nnotícias da velha senhora e mandou a\nfilha fazer-lhe uma visita, levando alguns\ndoces. O caminho era longo e passava por\numa floresta. Matreiro o Lobo-Mau, dizendo\nser o guarda da floresta abordou a menina\nno caminho, fingindo ser amigo, pois sua\nintenção era comer a neta e a avó.\nAo chegar à casa da avó Chapeuzinho\nVermelho foi tomada de surpresa, pois\nachou-a um tanto diferente de como a\nconhecia. O Lobo-Mau já tinha comido a\nvelhinha e vestido sua roupa, metendo-se\nem sua cama esperava para dar o bote\nfinal na menina. Você vai ter momentos de\nternura, medo, alegria e muita diversão ao\nler este clássico da literatura infantil.',
        
        bg='#7030A0', fg='#ffffff', font=('Poppins', 10, 'bold'), justify=LEFT)
        text.place(relx = 0.01,rely = 0.15)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.88,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def voltar(self):
        self.hide()
        self.volta = Fantasia(self)

class FabulaRato(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('O Leão e o Rato')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='O Leão e o Rato', bg='#ED7D31', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.15, rely = 0.02)


        text = Label(self, text=f'Certo dia, estava um Leão a dormir a sesta\nquando um ratinho começou a correr por\ncima dele. O Leão acordou, pôs-lhe a pata\nem cima, abriu a bocarra e preparou-se\npara o engolir. Perdoa-me! - gritou o\nratinho - Perdoa-me desta vez e eu nunca\no esquecerei. Quem sabe se um dia não\nprecisarás de mim? O Leão ficou tão\ndivertido com esta ideia que levantou a\npata e o deixou partir. Dias depois o Leão\ncaiu numa armadilha. Como os caçadores\no queriam oferecer vivo ao Rei, amarra-\nram-no a uma árvore e partiram à procura\nde um meio para o transportarem. Nisto,\napareceu o ratinho. Vendo a triste situação\nem que o Leão se encontrava, roeu as\ncordas que o prendiam. E foi assim que um\nratinho pequenino salvou o Rei dos Animais.\nPara refletir: Nunca devemos subestimar\nninguém. Todo ser humano é capaz de\nalgo extraordinário',
        
        bg='#7030A0', fg='#ffffff', font=('Poppins', 10, 'bold'), justify=LEFT)
        text.place(relx = 0.01,rely = 0.1)
        
        '''text = Label(self, text = '– Elizeu Petrelli de Vitor ', bg='#7030A0', fg='#fff', font=('Poppins', 10, 'bold'))
        text.place(relx = 0.45, rely = 0.8)'''


        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.88,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def voltar(self):
        self.hide()
        self.volta = Fabula(self)

class Fabula(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Fabulas')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Fabulas', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.3, rely = 0.03)

        self.hFabula = Button(self, bg = '#ED7D31', fg = '#fff', activebackground='#ED7D31', activeforeground = '#fff', text='O Leão e o Rato', font = 'Poppins-Regular.ttf', command=self.avancar).place(relx=0.17,rely=0.37,relwidth=0.7, relheight = 0.1)


        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def avancar(self):
        self.hide()
        self.avanca = FabulaRato(self)


    def voltar(self):
        self.hide()
        self.volta = GenerosH(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class GenerosH(Toplevel): #Pagina do cadastro
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Escolha o conteúdo')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0") 

        text = Label(self, text='Escolha o genero ', bg='#7030A0', fg = '#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.1, rely = 0.07)

        self.imaG4 = PhotoImage(file='h1.png')
        self.imaG5 = PhotoImage(file='h2.png')
        self.imaG6 = PhotoImage(file='h3.png')

        self.botao1 = Button(self, image = self.imaG4, height = 75, width = 75, command = self.Cbtn1, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.02, rely=0.18, width=140, height=195)

        self.botao2 = Button(self, image = self.imaG5, width = 10, height = 10, command = self.Cbtn2, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.52, rely=0.18, width=140, height=195)

        self.botao3 = Button(self, image = self.imaG6, command = self.Cbtn3, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.28, rely=0.5, width=140, height=195)

        self.botaovoltar = Button(self, text='← Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.82,relwidth=0.7, relheight = 0.1)

    def Cbtn1(self):
        self.hide()
        self.abrir = Aventura(self)

    def Cbtn2(self):
        self.hide()
        self.abrir = Fantasia(self)

    def Cbtn3(self):
        self.hide()
        self.abrir = Fabula(self)

    def Cbtn4(self):
        self.hide()
        self.abrir = Drama(self)

    def voltar(self): # Comando para ir a próxima tela
        self.hide()
        self.abrir = Escolha(self)
    def hide(self):  # Esconde a janela root
        self.withdraw()

class Tela7(Toplevel): #Pagina do cadastro
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Escolha o conteúdo')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0") 

        text = Label(self, text='Escolha o conteúdo ', bg='#7030A0', fg = '#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.04, rely = 0.07)

        self.imaG4 = PhotoImage(file='1.png')
        self.imaG5 = PhotoImage(file='2.png')
        self.imaG6 = PhotoImage(file='3.png')


        botao5 = Button(self, image = self.imaG4, command = self.abrirBotao5, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.02, rely=0.18, relwidth=0.46, relheight=0.3)

        botao6 = Button(self, image = self.imaG5, command = self.abrirBotao6, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.52, rely=0.18, relwidth=0.46, relheight=0.3)

        botao7 = Button(self, image = self.imaG6, command = self.abrirBotao7, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.29, rely=0.5, relwidth=0.46, relheight=0.3)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def abrirBotao5(self):
        self.hide()
        self.abrir = Escolha(self)

    def abrirBotao6(self):
        self.hide()
        self.abrir = FormasGeometricas(self)

    def abrirBotao7(self):
        self.hide()
        self.abrir = ProblemasMatematicos(self)

    def voltar(self): # Comando para ir a próxima tela
        self.destroy()
        self.janela = Tela1()

    def show(self):  # Comando para mostrar essa tela novamente SE ela estiver no HIDE
        self.update()
        self.deiconify()

    def hide(self):  # Esconde a janela root
        self.withdraw()

class ProblemasMatematicos(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Problemas Matematicos')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Problemas Matematicos', bg='#FF4747', fg='#ffffff', font=('Poppins', 17, 'bold'))
        text.place(relx=0.006, rely = 0.03)

        self.adicao = PhotoImage(file='adicao.png')
        self.subtracao = PhotoImage(file='subtracao.png')
        self.multiplicacao = PhotoImage(file='multiplicacao.png')
        self.divisao = PhotoImage(file='divisao.png')



        self.BtnAdicao = Button(self, image = self.adicao, command = self.Tadicao, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.02, rely=0.18, relwidth=0.46, relheight=0.3)

        self.BtnSubtracao = Button(self, image = self.subtracao, command = self.Tsubtracao, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.52, rely=0.18, relwidth=0.46, relheight=0.3)

        self.BtnMultiplicacao = Button(self, image = self.multiplicacao, command = self.Tmultiplicacao, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.02, rely=0.5, relwidth=0.46, relheight=0.3)

        self.BtnDivisao = Button(self, image = self.divisao, command = self.Tdivisao, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.52, rely=0.5, relwidth=0.46, relheight=0.3)





        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf',command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def Tadicao(self):
        self.hide()
        self.avanca = Adicao(self)


    def Tsubtracao(self):
        self.hide()
        self.avanca = Subtracao(self)

    def Tmultiplicacao(self):
        self.hide()
        self.avanca = Multiplicacao(self)

    def Tdivisao(self):
        self.hide()
        self.avanca = Divisao(self)

    def voltar(self):
        self.hide()
        self.voltar = Tela7(self)

class Adicao(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Adição')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Adição', bg='#FF4747', fg='#ffffff', font=('Poppins', 17, 'bold'))
        text.place(relx=0.4, rely = 0.03)


        text = Label(self, text='quanto é 3 + 3', bg='#FF4747', fg='#ffffff', font=('Poppins', 14, 'bold'))
        text.place(relx=0.3, rely = 0.3)


        self.resposta1 = Button(self, text = 6, font = 'Poppins-Regular.ttf', command = self.acertou).place(relx=0.17, rely = 0.4, relwidth=0.3, relheight = 0.1)

        self.resposta2 = Button(self, text = 9, font = 'Poppins-Regular.ttf', command = self.errou).place(relx=0.57, rely = 0.4, relwidth=0.3, relheight = 0.1)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf',command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def acertou(self):
        self.hide()
        self.respostaC = Correto(self)

    def errou(self):
        self.hide()
        self.respostaE = Errado(self)

    def voltar(self):
        self.hide()
        self.voltar = ProblemasMatematicos(self)

class Subtracao(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Subtração')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Subtracao', bg='#FF4747', fg='#ffffff', font=('Poppins', 17, 'bold'))
        text.place(relx=0.3, rely = 0.03)


        text = Label(self, text='quanto é 3 - 3', bg='#FF4747', fg='#ffffff', font=('Poppins', 14, 'bold'))
        text.place(relx=0.3, rely = 0.3)


        self.resposta1 = Button(self, text = 6, font = 'Poppins-Regular.ttf', command = self.errou).place(relx=0.17, rely = 0.4, relwidth=0.3, relheight = 0.1)

        self.resposta2 = Button(self, text = 0, font = 'Poppins-Regular.ttf', command = self.acertou).place(relx=0.57, rely = 0.4, relwidth=0.3, relheight = 0.1)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf',command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def acertou(self):
        self.hide()
        self.respostaC = Correto(self)

    def errou(self):
        self.hide()
        self.respostaE = Errado(self)

    def voltar(self):
        self.hide()
        self.voltar = ProblemasMatematicos(self)

class Multiplicacao(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Multiplicacao')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Multiplicacao', bg='#FF4747', fg='#ffffff', font=('Poppins', 17, 'bold'))
        text.place(relx=0.25, rely = 0.03)


        text = Label(self, text='quanto é 3 x 3', bg='#FF4747', fg='#ffffff', font=('Poppins', 14, 'bold'))
        text.place(relx=0.3, rely = 0.3)


        self.resposta1 = Button(self, text = 0, font = 'Poppins-Regular.ttf', command = self.errou).place(relx=0.17, rely = 0.4, relwidth=0.3, relheight = 0.1)

        self.resposta2 = Button(self, text = 9, font = 'Poppins-Regular.ttf', command = self.acertou).place(relx=0.57, rely = 0.4, relwidth=0.3, relheight = 0.1)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf',command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def acertou(self):
        self.hide()
        self.respostaC = Correto(self)

    def errou(self):
        self.hide()
        self.respostaE = Errado(self)

    def voltar(self):
        self.hide()
        self.voltar = ProblemasMatematicos(self)

class Divisao(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Divisão')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Divisão', bg='#FF4747', fg='#ffffff', font=('Poppins', 17, 'bold'))
        text.place(relx=0.35, rely = 0.03)


        text = Label(self, text='quanto é 12 ÷ 4', bg='#FF4747', fg='#ffffff', font=('Poppins', 14, 'bold'))
        text.place(relx=0.3, rely = 0.3)


        self.resposta1 = Button(self, text = 3, font = 'Poppins-Regular.ttf', command = self.acertou).place(relx=0.17, rely = 0.4, relwidth=0.3, relheight = 0.1)

        self.resposta2 = Button(self, text = 8, font = 'Poppins-Regular.ttf', command = self.errou).place(relx=0.57, rely = 0.4, relwidth=0.3, relheight = 0.1)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf',command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def acertou(self):
        self.hide()
        self.respostaC = Correto(self)

    def errou(self):
        self.hide()
        self.respostaE = Errado(self)

    def voltar(self):
        self.hide()
        self.voltar = ProblemasMatematicos(self)

class Correto(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Você Acertou')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Você acertou!', bg='#FF4747', fg='#ffffff', font=('Poppins', 17, 'bold'))
        text.place(relx=0.25, rely = 0.3)


        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf',command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def voltar(self):
        self.hide()
        self.voltar = ProblemasMatematicos(self)

class Errado(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Você Errou')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Você Errou!', bg='#FF4747', fg='#ffffff', font=('Poppins', 17, 'bold'))
        text.place(relx=0.27, rely = 0.3)


        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf',command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def voltar(self):
        self.hide()
        self.voltar = ProblemasMatematicos(self)

class FormasGeometricas(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Formas Geometricas')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Formas Geometricas', bg='#FF4747', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.002, rely = 0.03)

        self.triangulo = PhotoImage(file='forma1.png')
        self.quadrado = PhotoImage(file='forma2.png')
        self.retangulo = PhotoImage(file='forma3.png')
        self.circulo = PhotoImage(file='forma4.png')


        self.BtnTriangulo = Button(self, image = self.triangulo, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.02, rely=0.18, relwidth=0.46, relheight=0.3)

        self.BtnQuadrado = Button(self, image = self.quadrado, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.52, rely=0.18, relwidth=0.46, relheight=0.3)

        self.BtnRetangulo = Button(self, image = self.retangulo, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.02, rely=0.5, relwidth=0.46, relheight=0.3)

        self.BtnCirculo = Button(self, image = self.circulo, borderwidth=0, bg='#7030A0', activebackground = '#7030A0').place(relx=0.52, rely=0.5, relwidth=0.46, relheight=0.3)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf',command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def hide(self):  # Esconde a janela root
        self.withdraw()

    def avancar(self):
        pass

    def voltar(self):
        self.hide()
        self.voltar = Tela7(self)

#------------TELA 3----------------
class Tela3(Toplevel): #Pagina do cadastro
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('LOGIN')             # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0") 
        # Inserindo texto
        Label(self, text='Nome de usuário: ', bg='#7030A0').place(relx=0.1, rely=0.67)
        Label(self, text='Senha:', bg='#7030A0').place(relx=0.1, rely=0.75)
        # Comando para mudar escrita inserida na lacuna
        self.senha = StringVar()
        # Inserindo lacunas
        self.entra = Entry(self, bd=2).place(relx=0.1, rely=0.70, relwidth = 0.78)
        self.entra2= Entry(self, textvariable = self.senha, show = '*', bd=2).place(relx=0.1, rely=0.78, relwidth = 0.78)
        #Inserindo botão
        self.avancar = Button(self, text='ENTRAR', font=('Arial', 10, 'bold'),bg = '#7030A0', command= self.onClose).place(relx=0.35,rely=0.93,relwidth=0.3,)
        
        
        self.buton = Button(self, text='⇦', bg='#7030A0', bd=5, command=self.onbotao
        ).place(relx=0.05, rely=0.027,relwidth=0.088,relheight=0.037)
        #Inserindo imagem
        self.imaG = PhotoImage(file='login.png')
        self.imaG = self.imaG.subsample(4, 4)
        self.imag = Label(self, image=self.imaG, bd=1, bg = '#7030A0' ).place(relx=0.064, rely=0.12, relwidth=0.85, relheight=0.5)
    def onClose(self): # Comando para ir a próxima tela
        self.hide()
        self.abrir = Tela7(self)
    def onbotao(self): # Comando para ir voltar a tela anterior
        self.hide()
        self.inicio = self.frame_original.show()
    def hide(self):  # Esconde a janela root
        self.withdraw()


    def show(self):  # Comando para destruir tela
        self.update()
        self.deiconify()
#------------TELA 2-----------
class Tela2(Toplevel): #Pagina do cadastro
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('CADASTRO')             # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")       # Inserindo cor da tela
        # Inserindo texto
        Label(self, text='Nome de usuário: ', bg='#7030A0').place(relx=0.1, rely=0.67)
        Label(self, text='Senha:', bg='#7030A0').place(relx=0.1, rely=0.75)
        Label(self, text='Confirmar senha:', bg='#7030A0').place(relx=0.1, rely=0.83)
        # Comando para mudar escrita inserida na lacuna
        self.senha = StringVar()
        self.senha1 = StringVar()
        # Inserindo lacunas
        self.entra = Entry(self, bd=2).place(relx=0.1, rely=0.70, relwidth = 0.78)
        self.entra2= Entry(self, textvariable = self.senha, show = '*', bd=2).place(relx=0.1, rely=0.78, relwidth = 0.78)
        self.entra3 = Entry(self, textvariable = self.senha1, show = '*', bd=2).place(relx=0.1, rely=0.86, relwidth = 0.78)
        #Inserindo botão
        self.avancar = Button(self, text='LOGAR', font=('Arial', 10, 'bold'),bg = '#7030A0', command= self.onClose).place(relx=0.35,rely=0.93,relwidth=0.3,)
        
        self.buton = Button(self, text='⇦', bg='#7030A0', bd=5, command= self.voltar).place(relx=0.05, rely=0.027,relwidth=0.088,relheight=0.037)
        #Inserindo imagem
        self.imaG = PhotoImage(file='login.png')
        self.imaG = self.imaG.subsample(4, 4)
        self.imag = Label(self, image=self.imaG, bd=1, bg = '#7030A0' ).place(relx=0.064, rely=0.12, relwidth=0.85, relheight=0.5)
    def onClose(self): # Comando para ir a próxima tela
        self.hide()
        self.abrir = Tela7(self)

    def voltar(self): # Comando para ir para a proxima tela
        self.hide()
        self.inicio = self.frame_original.show()


    def hide(self):  # Esconde a janela root
        self.withdraw()


    def show(self):  # Comando para destruir tela
        self.update()
        self.deiconify()
#------------------TELA 1---------------
class Tela1:
    def __init__ (self): #Inserindo funções
        self.root = root
        self.telinha()
        self.frame()
        self.wid()
        self.texto()
        self.imagem()
        root.mainloop()
    def telinha(self):
        self.root.title('BOMTCHAU')       # Inserindo nome da janela
        self.root.geometry('300x647+540+15')    # Inserindo tamanho da janela
        #Inserindo cores na tela
    def frame(self):
        self.frame1 = Frame(self.root, bg='#7030A0').place(relx=0.001, rely=0.001, relwidth=1, relheight=1)
        # Inserindo botão
    def wid(self):
        self.login = Button (self.frame1,text='Login',font=('Arial', 12, 'bold'), bg = '#ED7D31', command= self.clica2).place(relx=0.54, rely=0.9, relwidth=0.4, relheight=0.05)
        self.cadastrar = Button (self.frame1,text='Cadastrar',font=('Arial', 12, 'bold'), bg = '#ED7D31', command= self.clica).place(relx=0.06, rely=0.9, relwidth=0.4, relheight=0.05)
        #Inserindo Texto
    def texto(self):
        root.titulo= Label(self.frame1,text='BOMTCHAU',font='PoppinsBlack 16',bg='#7030A0').place(x=90, y=40)
        root.palavrinha = Label(self.frame1, text = 'Seja bem-vinda(o)', font = 'PoppinsBlack 12',bg='#7030A0').place(x= 85, y= 430)
        #Inserindo imagem
    def imagem(self):
        self.imagem = PhotoImage(file= 'mascote.png')
        self.imagem = self.imagem.subsample(2, 2)
        self.imageg= Label(self.frame1, image=self.imagem, bd=0, bg ='#7030A0').place(relx=0.1, rely=0.17, relwidth=0.82, relheight=0.4)
    def clica(self): #Comando para próxima tela
        self.hide()
        self.subTela = Tela2(self)
    def clica2(self): #Comando para próxima tela
        self.hide()
        self.subTela = Tela3(self)
    def hide(self): # Escondendo tela
        self.root.withdraw()
    def show(self):  # Comando para destruir tela
        self.root.update()
        self.root.deiconify()


class Tela5(Toplevel): #Pagina do cadastro
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('LOGIN')             # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")       # Inserindo cor da tela
        # Inserindo texto
        Label(self, text='Nome de usuário: ', bg='#7030A0').place(relx=0.1, rely=0.67)
        Label(self, text='Senha:', bg='#7030A0').place(relx=0.1, rely=0.75)
        Label(self, text='Confirmar senha:', bg='#7030A0').place(relx=0.1, rely=0.83)
        # Comando para mudar escrita inserida na lacuna
        self.senha = StringVar()
        self.senha1 = StringVar()
        # Inserindo lacunas
        self.entra = Entry(self, bd=2).place(relx=0.1, rely=0.70, relwidth = 0.78)
        self.entra2= Entry(self, textvariable = self.senha, show = '*', bd=2).place(relx=0.1, rely=0.78)
        self.entra3 = Entry(self, textvariable = self.senha1, show = '*', bd=2).place(relx=0.1, rely=0.86)
        #Inserindo botão
        self.avancar = Button(self, text='LOGAR', font=('Arial', 10, 'bold'),bg = '#7030A0', command= self.onClose).place(relx=0.35,rely=0.93,relwidth=0.3,)
        self.buton = Button(self, text='⇦', command= self.onbotao, bg='#7030A0', bd=5).place(relx=0.05, rely=0.027,relwidth=0.088,relheight=0.037)
        #Inserindo imagem
        self.imaG = PhotoImage(file='login.png')
        self.imaG = self.imaG.subsample(4, 4)
        self.imag = Label(self, image=self.imaG, bd=1, bg = '#7030A0' ).place(relx=0.064, rely=0.12, relwidth=0.85, relheight=0.5)
    def onClose(self): # Comando para ir a próxima tela
        self.hide()
        self.abrir = Tela7(self)
    def onbotao(self): # Comando para voltar a tela anterior
        self.hide()
        self.abrir = Tela1(self)
    def hide(self):  # Esconde a janela root
        self.withdraw()

root = Tk()
Tela1()