palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:  #para cada palavra em palavras
    print(f'\nNa palavra {p.upper()} temos', end=' ')  #o upper() é para deixar as palavras em maiusculo
    for letra in p:
        if letra.lower() in 'aeiou':  #o lower é para deixar as vogais em minusculas
            print(letra, end=' ')
