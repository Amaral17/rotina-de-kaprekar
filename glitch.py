import time

num = int(input("Escolha um número de 4 caracteres aleatório: "))
count = 0

if len(str(num)) != 4:
    print("O numero precisa ter 4 caracteres")
else:
    while num != 6174:
        count += 1

        a = str(num).zfill(4)

        crescente = int(''.join(sorted(a)))
        decrescente = int(''.join(sorted(a, reverse=True)))

        num = decrescente - crescente

        print(decrescente, "-", crescente, "=", num)
        time.sleep(0.5)

    print("Número de tentativas:", count)
