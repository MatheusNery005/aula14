cabecas= int(input("Digite o número de cabeças: "))
pes= int(input("Digite o núemro de pés: "))

coelhos = int((pes - 2*cabecas)/2)
patos = int(cabecas - coelhos)

print("Coelhos: " + str(coelhos))
print("Patos: " + str(patos))