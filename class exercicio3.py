"""
Exercício - Informações de Frutas em uma Mercearia

Em uma mercearia, várias frutas são vendidas, e você deseja criar um
sistema simples para gerenciar as informações sobre essas frutas.

Objetivos:

    1. Definir uma classe chamada Fruta.
    2. Instanciar um ou mais objetos desta classe.
    3. Acessar e exibir os atributos dos objetos instanciados.

Instruções:

    1. Crie uma classe chamada Fruta com os seguintes atributos:
        - nome: o nome da fruta (ex: "Maçã", "Banana").
        - preco_por_kg: o preço da fruta por quilograma.
        - quantidade_em_estoque: a quantidade da fruta em estoque (em quilogramas).

    2. Instancie pelo menos duas frutas diferentes, fornecendo valores específicos para seus atributos.

    3. Acesse os atributos das frutas instanciadas e exiba suas informações de forma organizada, como:

        Nome da Fruta: [nome da fruta]
        Preço por Kg: [preço da fruta por quilograma]
        Quantidade em Estoque: [quantidade da fruta em estoque]

"""
class frutas:

    def __init__(self,fruta,preco_por_kg,quantidade_em_estoque_kg):
        self.fruta = fruta
        self.preco_por_kg = preco_por_kg
        self.quantidade_em_estoque_kg = quantidade_em_estoque_kg

    def status(self):
        print(f'\nFruta: {self.fruta}\n Preço por kg: {self.preco_por_kg}\n quantidade em estoque: {self.quantidade_em_estoque_kg} kg')

    def mostrar_preso(self):

        print(f' O preço da {self.fruta} e de R$ {self.preco_por_kg}')

    def venda(self):

        while True:
          try:

            kg = float(input('Quantos kg você deseja comprar: '))

            if kg > 0 and kg <= self.quantidade_em_estoque_kg:

              self.quantidade_em_estoque_kg -= kg

              print('Venda realizado com sucesso!')

              break

            else:

                print('quantidade superior ao estoque')

          except ValueError:

            print('entrada invalida')
    def comprar (self):

        while True:

            try:

              compra = float(input('Digite a quantidade de kg para adcionar no estoque:'))

              if compra > 0 :

                self.quantidade_em_estoque_kg += compra

                print('Estoque atualizado com sucesso!')
                break
              else:
                  print('quantidade invalida')

            except ValueError:

             print('entrada invalida')

lista_frutas = []

while True:

     print('\n--MENU--')
     print('1 - Adicionar Fruta ao estoque')
     print('2 - conferir estoque de fruntas')
     print('3 - Vender fruta')
     print('4 - comprar fruta')
     print('5 - valor do KG da fruta')
     print('6 - Sair ')

     try:

         entrada = int(input('Digite uma opção: '))

     except ValueError:
         print ('Entrada invalida')
         continue

     if entrada == 1 :
         fruta = str(input('Digite o nome da fruta: '))
         preco_por_kg = float(input('Digite o preço do kg da fruta :'))
         quantidade_por_kg = float(input('Digite o quantidade de kg da fruta :'))

         nova_fruta = frutas(fruta,preco_por_kg,quantidade_por_kg)
         lista_frutas.append(nova_fruta)

     elif entrada == 2 :

         if lista_frutas:

             for fruta in lista_frutas:

                 fruta.status()

         else:
             print('Fruta não encontrado no estoque')

     elif entrada == 4:

         nova_fruta = input('Digite o nome da fruta para verificar se existe no estoque: ')
         encontrada = False

         for fruta in lista_frutas:

             if fruta.fruta == nova_fruta:

                 fruta.comprar()

                 encontrada = True

                 break

         if not encontrada:

             print('fruta não encontrada, Vamos cadastrar ela')

             fruta = str(input('Digite o nome da fruta: '))
             preco_por_kg = float(input('Digite o preço do kg da fruta :'))
             quantidade_por_kg = float(input('Digite o quantidade de kg da fruta :'))

             nova_fruta = frutas(fruta, preco_por_kg, quantidade_por_kg)
             lista_frutas.append(nova_fruta)

     elif entrada == 5 :

         pesquisar_fruta = str(input('Digite o nome da fruta: '))

         entrada = False

         for fruta in lista_frutas:

             if fruta.fruta == lista_frutas:

                 fruta.mostrar_preco()

                 entrada = True

                 break
             else:

                 print('Fruta não encontrada')

     elif entrada == 6 :

         print('Programa finalizado com sucesso!')

     else:

         print('Opção invalida')
         
