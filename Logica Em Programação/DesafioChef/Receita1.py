# --------------------------------------------
# RECEITA 1 - CHEESECAKE DE FRUTAS CÍTRICAS
# --------------------------------------------

print("\n==========================================")
print("       FICHA TÉCNICA DIGITAL - DEVCHEF")
print("==========================================")

print("\nReceita: Cheesecake de frutas cítricas")


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

ovo = 1
iogurte = 1
requeijao = 1
baunilha = 5

suco_laranja = 1
suco_tangerina = 0.5
suco_limao = 2
mel = 2
amido = 1


# ---------------- NOVAS QUANTIDADES ----------------

novo_ovo = ovo * fator
novo_iogurte = iogurte * fator
novo_requeijao = requeijao * fator
nova_baunilha = baunilha * fator

novo_suco_laranja = suco_laranja * fator
novo_suco_tangerina = suco_tangerina * fator
novo_suco_limao = suco_limao * fator
novo_mel = mel * fator
novo_amido = amido * fator


# ---------------- TEMPO DE PREPARO ----------------

tempo_preparo = int(
    input("\nQuantos minutos serão usados no preparo da base? ")
)

tempo_forno = 20

tempo_calda = int(
    input("Quantos minutos serão usados no preparo da calda? ")
)

tempo_total = tempo_preparo + tempo_forno + tempo_calda


# ---------------- FICHA TÉCNICA ----------------

print("\n==========================================")
print("              FICHA TÉCNICA")
print("==========================================")

print(f"Receita: Cheesecake de frutas cítricas")
print(f"Cozinheiro: {nome}")
print(f"Rendimento: {porcoes_desejadas} porções")
print(f"Fator de proporção: {fator:.2f}")
print(f"Tempo total estimado: {tempo_total} minutos")


# ---------------- INGREDIENTES ----------------

print("\n------------------------------------------")
print("INGREDIENTES NECESSÁRIOS")
print("------------------------------------------")

print(f"{novo_ovo:.1f} ovo(s)")
print(
    f"{novo_iogurte:.1f} colher(es) de sopa "
    "de iogurte desnatado"
)
print(
    f"{novo_requeijao:.1f} colher(es) de sopa "
    "de requeijão light"
)
print(f"{nova_baunilha:.1f} gotas de baunilha")


print("\nPARA A CALDA CÍTRICA:")

print(
    f"{novo_suco_laranja:.1f} xícara(s) "
    "de suco de laranja natural"
)

print(
    f"{novo_suco_tangerina:.1f} xícara(s) "
    "de suco de tangerina"
)

print(
    f"{novo_suco_limao:.1f} colher(es) de sopa "
    "de suco de limão"
)

print(
    f"{novo_mel:.1f} colher(es) de sopa "
    "de mel ou xilitol"
)

print(
    f"{novo_amido:.1f} colher(es) de sopa "
    "de amido de milho"
)


# ---------------- MODO DE PREPARO ----------------

print("\n------------------------------------------")
print("MODO DE PREPARO")
print("------------------------------------------")

print("""
1 - Coloque em uma tigela o ovo, o iogurte,
o requeijão, a baunilha e o adoçante.

2 - Misture bem com um fouet ou garfo até
obter uma mistura lisa e homogênea.

3 - Divida a mistura em ramequins próprios
para forno ou air fryer.

4 - Leve ao forno preaquecido a 250 °C
por aproximadamente 15 a 20 minutos.

5 - Retire do forno, deixe esfriar e leve
à geladeira.

6 - Para a calda, coloque em uma panela
os sucos de laranja, tangerina e limão.

7 - Acrescente o mel ou xilitol.

8 - Adicione o amido de milho diluído
em água e mexa até engrossar.

9 - Deixe a calda esfriar.

10 - Coloque a calda sobre o cheesecake
e sirva.
""")


print("==========================================")
print("              AGORA É SÓ VC FAZER")
print("==========================================")