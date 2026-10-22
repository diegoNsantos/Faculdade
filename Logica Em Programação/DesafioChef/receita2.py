# --------------------------------------------
# RECEITA 2 - GELATO DE MANGA COM MARACUJÁ
# --------------------------------------------

print("\n==========================================")
print("       FICHA TÉCNICA DIGITAL - DEVCHEF")
print("==========================================")

print("\nReceita: Gelato de manga com maracujá")


# ---------------- ENTRADA DE DADOS ----------------

nome = input("\nDigite o nome do cozinheiro: ")

porcoes_originais = int(
    input("Quantas porções a receita original rende? ")
)

porcoes_desejadas = int(
    input("Quantas porções você deseja preparar? ")
)


# ---------------- FATOR DE PROPORÇÃO ----------------

fator = porcoes_desejadas / porcoes_originais


# ---------------- INGREDIENTES ORIGINAIS ----------------

manga = 150
maracuja = 0.5
iogurte = 2


# ---------------- NOVAS QUANTIDADES ----------------

nova_manga = manga * fator
novo_maracuja = maracuja * fator
novo_iogurte = iogurte * fator


# ---------------- TEMPO DE PREPARO ----------------

tempo_descongelar = 3
tempo_bater = 3

tempo_total = tempo_descongelar + tempo_bater


# ---------------- FICHA TÉCNICA ----------------

print("\n==========================================")
print("              FICHA TÉCNICA")
print("==========================================")

print(f"Receita: Gelato de manga com maracujá")
print(f"Cozinheiro: {nome}")
print(f"Rendimento: {porcoes_desejadas} porções")
print(f"Fator de proporção: {fator:.2f}")
print(f"Tempo total estimado: {tempo_total} minutos")


# ---------------- INGREDIENTES ----------------

print("\n------------------------------------------")
print("INGREDIENTES NECESSÁRIOS")
print("------------------------------------------")

print(f"{nova_manga:.1f} g de manga picada e congelada")
print(f"{novo_maracuja:.1f} maracujá(s)")
print(
    f"{novo_iogurte:.1f} colher(es) de sopa "
    "de iogurte natural"
)


# ---------------- MODO DE PREPARO ----------------

print("\n------------------------------------------")
print("MODO DE PREPARO")
print("------------------------------------------")

print("""
1 - Retire os cubos de manga congelada
do freezer.

2 - Deixe a manga em temperatura ambiente
por aproximadamente 2 a 3 minutos.

3 - Coloque a manga em um processador
de alimentos ou liquidificador potente.

4 - Acrescente a polpa do maracujá
e o iogurte natural.

5 - Bata por aproximadamente 2 a 3 minutos,
até atingir uma textura cremosa.

6 - Se parte da mistura ficar presa nas
laterais, utilize uma espátula para colocar
tudo novamente no centro.

7 - Continue batendo até a mistura ficar
lisa e homogênea.

8 - Sirva imediatamente.
""")


print("==========================================")
print("              AGORA É SÓ VC FAZER")
print("==========================================")