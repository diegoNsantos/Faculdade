# --------------------------------------------
# RECEITA 3 - NUGGETS SAUDÁVEIS
# --------------------------------------------

print("\n==========================================")
print("       FICHA TÉCNICA DIGITAL - DEVCHEF")
print("==========================================")

print("\nReceita: Nuggets Saudáveis")


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

frango = 500
azeite = 4
sal = 0.5
alho = 3
cebola = 0.5
paprica = 0.5
curcuma = 0.5
cheiro_verde = 2

ovos = 2
panko = 1


# ---------------- NOVAS QUANTIDADES ----------------

novo_frango = frango * fator
novo_azeite = azeite * fator
novo_sal = sal * fator
novo_alho = alho * fator
nova_cebola = cebola * fator
nova_paprica = paprica * fator
nova_curcuma = curcuma * fator
novo_cheiro_verde = cheiro_verde * fator

novos_ovos = ovos * fator
novo_panko = panko * fator


# ---------------- TEMPO DE PREPARO ----------------

tempo_preparo = int(
    input("\nQuantos minutos serão usados para preparar os nuggets? ")
)

tempo_forno = 30

tempo_total = tempo_preparo + tempo_forno


# ---------------- FICHA TÉCNICA ----------------

print("\n==========================================")
print("              FICHA TÉCNICA")
print("==========================================")

print(f"Receita: Nuggets Saudáveis")
print(f"Cozinheiro: {nome}")
print(f"Rendimento: {porcoes_desejadas} porções")
print(f"Fator de proporção: {fator:.2f}")
print(f"Tempo total estimado: {tempo_total} minutos")


# ---------------- INGREDIENTES ----------------

print("\n------------------------------------------")
print("INGREDIENTES NECESSÁRIOS")
print("------------------------------------------")

print(f"{novo_frango:.1f} g de peito de frango")
print(f"{novo_azeite:.1f} colher(es) de sopa de azeite")
print(f"{novo_sal:.1f} colher(es) de chá de sal")
print(f"{novo_alho:.1f} dente(s) de alho")
print(f"{nova_cebola:.1f} cebola(s)")
print(f"{nova_paprica:.1f} colher(es) de chá de páprica")
print(f"{nova_curcuma:.1f} colher(es) de chá de cúrcuma")
print(
    f"{novo_cheiro_verde:.1f} colher(es) de sopa "
    "de cheiro-verde"
)


# ---------------- PARA EMPANAR ----------------

print("\nPARA EMPANAR:")

print(f"{novos_ovos:.1f} ovo(s) batido(s)")
print(f"{novo_panko:.1f} xícara(s) de panko")


# ---------------- MODO DE PREPARO ----------------

print("\n------------------------------------------")
print("MODO DE PREPARO")
print("------------------------------------------")

print("""
1 - Corte o peito de frango em pedaços.

2 - Coloque o frango em um processador
ou liquidificador potente.

3 - Acrescente o azeite, sal, alho,
cebola, páprica, cúrcuma, cheiro-verde
e pimenta-do-reino.

4 - Processe até formar uma massa
homogênea.

5 - Com as mãos levemente untadas com
azeite, modele pequenas porções em
formato de nuggets.

6 - Coloque os ovos batidos em um prato
e o panko em outro.

7 - Passe cada nugget primeiro no ovo
batido e depois no panko.

8 - Coloque os nuggets em uma assadeira.

9 - Leve ao forno preaquecido a 200 °C
por aproximadamente 25 a 30 minutos.

10 - Vire os nuggets na metade do tempo
para que dourem por igual.
""")


print("==========================================")
print("              AGORA É SÓ VC FAZER")
print("==========================================")