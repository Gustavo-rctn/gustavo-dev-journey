def validador_arquivo_extensao(nome_do_arquivo):

    if nome_do_arquivo.endswith('.png') or nome_do_arquivo.endswith('.jpg'):
        return 'VÁLIDO'
    else:
        return 'NEGADO'



quantidade_de_arquivos = int(input('Digite a quantidade de arquivos que você quer salvar: '))


for c in range(1, quantidade_de_arquivos + 1):

    arquivo = input(f'Coloque o caminho do arquivo {c} (ex: foto.png): ').strip().lower()

    status = validador_arquivo_extensao(arquivo)

    print(f'Resultado para o arquivo {c}: {status}\n')