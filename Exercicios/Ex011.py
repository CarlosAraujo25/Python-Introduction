l = float(input('Qual a largura da sua parade?'))
h = float(input('Qual a altura ?'))
a = l*h
t = a/2
print('Sua parede tem as dimensões {}x{} e sua área é de {}m², '
      'você precisará {}l de tinta para pinta-la'
      .format(l, h, a, t))
