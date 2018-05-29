## Crie um programa que leia o nome de uma cidade
# ## diga se ela começa ou não com o nome "SANTO".
cidade = (input('digite o nome de uma cidade')).strip()##### retira todos os espaços
cidade = cidade.upper() ### transforma tudo em maiuscula
cidade = 'SANTO' in cidade ####procura SANTO em cidade
print(cidade)
