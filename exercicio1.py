class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponibilidade = True
        
    def emprestar(self):
        self.__disponibilidade = False
        print(f"Livro {self.__titulo} emprestado.\n")
        
    def devolver(self):
        self.__disponibilidade = True
        print(f"Livro {self.__titulo} devolvido.\n")
        
    def mostrar_info(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        if self.__disponibilidade == True:
            print("Disponibilidade: disponível.\n")
        else:
            print("Disponibilidade: não disponível.\n")
        
    def pegar_titulo(self):
        return self.__titulo
    def pegar_disponibilidade(self):
        return self.__disponibilidade
    
class Livraria:
    def __init__(self):
        self.__livros = []
        print("\n\n\n*******LIVRARIA CRIADA*******\n\n\n")
        
    def adicionar_livro(self, livro:Livro):
        self.__livros.append(livro)
        print(f"Livro {livro.pegar_titulo()} adicionado.\n")
    
    def emprestar_livro(self, titulo):
        for livro in self.__livros:
            
            if livro.pegar_titulo() == titulo:
                if livro.pegar_disponibilidade() == True:
                    livro.emprestar()
                else:
                    print("Livro indisponivel para empréstimo")
        
    def mostrar_inventario(self):
        for livro in self.__livros:
            livro.mostrar_info()
            
#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

livraria = Livraria()
livro1 = Livro("livro1", "Luís Phillipe Ruiz Gama")
livro2 = Livro("livro2", "Luís Phillipe Ruiz Gama")
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)
livraria.mostrar_inventario()
livro3 = Livro("livro3", "Larissa Ribeiro Savino")
livraria.adicionar_livro(livro3)
livraria.emprestar_livro("livro3")
livraria.emprestar_livro("livro1")
livro1.devolver()
livraria.mostrar_inventario()


