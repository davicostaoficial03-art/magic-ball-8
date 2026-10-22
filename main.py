import random
import time

def magic_ball():
    respostas = [
        "É claramente verdade",
        "Sem dúvida",
        "Definitivamente sim",
        "Pode contar com isso",
        "Na minha opinião, sim",
        "Provavelmente",
        "Perspectiva boa",
        "Sim",
        "Os sinais apontam que sim",
        "Resposta confusa, tente novamente",
        "Pergunte novamente mais tarde",
        "Melhor não te contar agora",
        "Não é possível prever agora",
        "Concentre-se e pergunte novamente",
        "Não conte com isso",
        "Minha resposta é não",
        "Minhas fontes dizem que não",
        "Perspectiva não muito boa",
        "Duvido muito"
    ]

    print("Sejam bem-vindos ao Magic Ball 8!")
    time.sleep(1.5)

    print("Ah, não sabe o que é? Eu posso dar uma breve explicação sobre isso:")
    time.sleep(2)

    print("É uma esfera de plástico feita para se parecer com uma bola oito de tamanho grande, usada para adivinhação ou busca de conselhos.")
    time.sleep(2)

    print("Pra jogar, você precisa fazer uma pergunta de 'sim ou não', virar a bola e ler a resposta. Entendeu?")
    time.sleep(2)

    while True:
        pergunta = input("\nFaça sua pergunta: ")
        resposta = random.choice(respostas)
        print(resposta)

        continuar = input("\nQuer fazer outra pergunta? (sim/não): ").strip().lower()

        if continuar != "sim":
            print("Tchau! Espero ter ajudado.")
            break

magic_ball()
