
def filtro_conteudo(comentario):
    if comentario == 'bosta' or comentario == 'cu':
        print(f'Comentario: {comentario}')
    else:
        return comentario

comentario_usuario = input('Comente sua opinião sem palavrões: ').lower().replace('bosta', '*****' ).replace('cu', '***')

update = filtro_conteudo(comentario_usuario)

print(f'Comentario: {update}')