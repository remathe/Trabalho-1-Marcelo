# Matheus Soares da Costa - 2414290057
# Lucas de Carvalho Melo - 2324290088
# Clifton Pereira Barbosa - 2414290162
# Luiz Enrique Carrilho Rego - 2414290126

def calcular_iof(dias):
    if dias <= 1:
        return 0.0038
    elif dias <= 15:
        return 0.0199
    elif dias <= 30:
        return 0.0300
    elif dias <= 60:
        return 0.0330
    elif dias <= 90:
        return 0.0360
    elif dias <= 180:
        return 0.0380
    elif dias <= 360:
        return 0.0410
    else:
        return 0.0450

def calcular_ir(rendimento):
    if rendimento <= 1000:
        return 0.0
    elif rendimento <= 5000:
        return 0.075
    elif rendimento <= 10000:
        return 0.15
    elif rendimento <= 30000:
        return 0.225
    else:
        return 0.275

def calcular_investimento(valor_investido, tempo_em_dias):
    taxa_rendimento_ano = 14.15 / 100
    rendimento = valor_investido * (1 + taxa_rendimento_ano) ** (tempo_em_dias / 365) - valor_investido
    percentual_iof = calcular_iof(tempo_em_dias)
    valor_iof = rendimento * percentual_iof
    rendimento_apos_iof = rendimento - valor_iof
    percentual_ir = calcular_ir(rendimento_apos_iof)
    valor_ir = rendimento_apos_iof * percentual_ir
    rendimento_liquido = rendimento_apos_iof - valor_ir
    return rendimento, valor_iof, valor_ir, rendimento_liquido

valor_investido = float(input("Digite o valor que você quer investir (em R$): "))
tempo_em_dias = int(input("Informe por quantos dias você deseja deixar seu dinheiro investido: "))

rendimento_bruto, valor_iof, valor_ir, rendimento_liquido = calcular_investimento(valor_investido, tempo_em_dias)

print("\nResumo do investimento:")
print(f"Valor investido: R$ {valor_investido:.2f}")
print(f"Rendimento bruto (antes de impostos): R$ {rendimento_bruto:.2f}")
print(f"Valor do IOF descontado: R$ {valor_iof:.2f}")
print(f"Valor do Imposto de Renda descontado: R$ {valor_ir:.2f}")
print(f"Rendimento líquido final: R$ {rendimento_liquido:.2f}")