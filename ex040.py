n1 = float(input('primeira nota:'))
n2 = float(input('segunda nota:'))
média = (n1 + n2) / 2
print(f'tirando {n1} e {n2} a média do aluno é {média}')
if média > 7:
    print('O aluno está \033[1;32mAPROVADO!\033[m')
elif média >= 5 and média <7:  #se a média for igual ou maior a 5 e se a média for menor que 7
    print('O aluno está de \033[1;33mRECUPERAÇÃO!\033[m')
else:
    print('O aluno está \033[1;31mREPROVADO!\033[m')

#média 7.0 ou superior: APROVADO
#média entre 5.0 e 6.9: RECUPERAÇÃO
#média abaixo de 5.0: REPROVADO



