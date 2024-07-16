
consumo = float(input("Informe o seu consumo médio mensal de dados em GB: "))

def recomendar_plano(consumo_mensal):
        if consumo_mensal <= 10:
            return "Plano Essencial Fibra - 50Mbps"
        elif 10 < consumo_mensal <= 20:
            return "Plano Prata Fibra - 100Mbps"
        elif 20 < consumo_mensal <= 30:
            return "Plano Premium Fibra - 300Mbps"
        else: 
            return "Consulte nosso gerente para planos diferenciados."
    
    # Recomendar o plano adequado
plano_recomendado = recomendar_plano(consumo)
print(plano_recomendado)
