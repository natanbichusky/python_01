import os #biblioteca que já vem com o python
restaurantes = [{'nome':'Don Marino', 'categoria':'Pizzaria', 'ativo':False},
                {'nome':'Kozan', 'categoria':'Japonesa', 'ativo':True},
                {'nome':'Restarante ao Cubo', 'categoria':'Diversos', 'ativo':True},
                {'nome':'La Terrasse', 'categoria':'Gourmet', 'ativo':False}
                ] #array
#no python ao invés de function é def

def alternar_estado():
    exibir_subtitulo('Alterando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    for restaurante in restaurantes:
        restaurante_encontrado = True
        restaurante['ativo'] = not restaurante['ativo']
        mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
        exibir_subtitulo({mensagem})
    voltar_ao_menu()

def voltar_ao_menu():
    print('\nDigite uma tecla para retornar ao menu inicial ')
    input()
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto)) #len conta a quantidade de letras em texto
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_nome_programa() -> None:
        print('\n')
        print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar Estado do Restaurante')
    print('4. Sair')

def encerrar_app():      
    exibir_subtitulo('Encerrando APP')

def opcao_invalida():
    exibir_subtitulo('Opção Inválida')
    voltar_ao_menu()

def cadastrar_restaurante():
    os.system('cls')
    print('CADASTRO DE NOVO RESTAURANTE\n')
    nome_do_restaurante = input('Digite o nome do Restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do Restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante,'categoria': categoria_do_restaurante, 'ativo':False} #False é padrão
    restaurantes.append(dados_do_restaurante) #adicionar no array
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes: ')
    print(f'{'Nome do Restaurante:'.ljust(22)}|{'Categoria:'.ljust(20)}| Status:')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)}|{categoria_restaurante.ljust(20)}|{ativo_restaurante.ljust(20)}')
    voltar_ao_menu()

def escolher_opcao():
    try:
        print('\n')
        opcao_escolhida = int(input('Escolha uma opção: ')) #se não colocar o int o python entenderá como uma string, e string não funcionará nos ifs e elses
        print('\n')
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:       #elif = else if
            listar_restaurantes()
        elif opcao_escolhida == 3:  
            alternar_estado()
        elif opcao_escolhida == 4:
            encerrar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': #arquivo será main, o principal, não será exportado para outros
        main()
 