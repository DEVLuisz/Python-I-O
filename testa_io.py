arquivo = open('Data/contatos.csv', encoding='utf-8')

print(type(arquivo.buffer))
conteudo = arquivo.buffer.read()

texto_em_bytes = bytes('Esse é um teste', 'utf-8')
print(texto_em_bytes)
print(type(texto_em_bytes))

arquivo.close()