numero1 = 1
numero2 = 2
print(f"Tentativa {numero1} de {numero2} ")

print("Tentativa {1} de {0} ".format(1, 2))

print("R$ {:.2f}".format(1.59))  # R$ 1.59
print("R$ {:7.2f}".format(1.59))  # R$    1.59
print("R$ {:07.2f}".format(1.59))  # R$ 0001.59

print("R$ {:07d}".format(46))  # R$ 0000046
print("R$ {:7d}".format(46))  # R$      46

print("Data {:02d}/{:02d}".format(9, 4))  # Data 09/04
