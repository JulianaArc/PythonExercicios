cid=str(input('em que cidade você nasceu?')).strip()   # O strip() remove os espaços finais e iniciais
print(cid[:5].upper() == 'SANTO')

# cidade[:5] - pega os primeiros cinco caracteres da cidade inserida pelo usuário.

# .upper() - converte esses cinco caracteres para maiúsculas, garantindo que a comparação seja feita em maiúsculas.

# 'SANTO' - é a string que estamos comparando com os primeiros cinco caracteres da cidade, mas em maiúsculas.

# Se esses cinco caracteres, após serem convertidos para maiúsculas, forem iguais a "SANTO" será TRUE.

