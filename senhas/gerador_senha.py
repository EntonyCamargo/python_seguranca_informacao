import random

import string

tamanho = int(input('Digite o tamanho de senha que voce deseja: '))

chars = string.ascii_letters + string.digits + 'ç^~[]!@#$%&*'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))