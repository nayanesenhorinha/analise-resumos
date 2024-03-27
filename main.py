def verifica_palavras_chave(resumo, palavras_chave):
    for palavra in palavras_chave:
        if palavra.lower() not in resumo.lower():
            return False
    return True

vagas = {
    'Vaga 1': {'palavras_chave': ['Python', 'Programação', 'Desenvolvimento'], 'candidatos': []},
    'Vaga 2': {'palavras_chave': ['Análise de dados', 'Dados', 'SQL'], 'candidatos': []}
}

while True:
    print("\n----- MENU -----")
    print("1. Cadastrar novo candidato")
    print("2. Exibir candidatos aptos para cada vaga")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '0':
        break
    elif escolha == '1':
        vaga = input("Para qual vaga você está se inscrevendo? (Digite o número da vaga): ")
        if vaga not in ['1', '2']:
            print("Vaga inválida. Por favor, escolha 1 ou 2.")
            continue
        
        nome = input("Digite seu nome: ")
        resumo = input("Digite um resumo sobre suas habilidades e experiências: ")

        if verifica_palavras_chave(resumo, vagas[f'Vaga {vaga}']['palavras_chave']):
            vagas[f'Vaga {vaga}']['candidatos'].append(nome)
            print("Você foi registrado como um candidato válido para a vaga.")
        else:
            print("Você não possui as habilidades necessárias para esta vaga.")

    elif escolha == '2':
        print("\nCandidatos aptos para cada vaga:")
        for vaga, dados in vagas.items():
            print(f"\n{vaga}:")
            for candidato in dados['candidatos']:
                print(candidato)
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
