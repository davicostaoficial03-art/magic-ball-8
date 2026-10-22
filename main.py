# Importa o módulo random, utilizado para selecionar uma resposta aleatória.
import random

# Importa o módulo time, utilizado para controlar pausas na execução do programa.
import time


# Define a função principal do jogo, responsável por executar toda a experiência.
def magic_ball():

    # Cria uma lista com todas as respostas possíveis da Magic Ball 8.
    # Cada elemento é uma string que pode ser escolhida aleatoriamente.
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

    # Exibe a mensagem inicial de boas-vindas no terminal.
    print("Sejam bem-vindos ao Magic Ball 8!")

    # Suspende a execução por 1,5 segundo antes de continuar.
    # Isso cria um intervalo entre as mensagens para deixar a apresentação
    # mais gradual, em vez de exibir tudo de uma vez.
    time.sleep(1.5)

    # Apresenta uma introdução para quem ainda não conhece o jogo.
    print("Ah, não sabe o que é? Eu posso dar uma breve explicação sobre isso:")

    # Aguarda 2 segundos antes de exibir a próxima mensagem.
    time.sleep(2)

    # Explica o que é a Magic Ball 8.
    print(
        "É uma esfera de plástico feita para se parecer com uma bola oito "
        "de tamanho grande, usada para adivinhação ou busca de conselhos."
    )

    # Cria outra pausa de 2 segundos para separar as explicações.
    time.sleep(2)

    # Explica as regras básicas: fazer uma pergunta de sim ou não
    # e receber uma resposta fornecida aleatoriamente pelo programa.
    print(
        "Pra jogar, você precisa fazer uma pergunta de 'sim ou não', "
        "virar a bola e ler a resposta. Entendeu?"
    )

    # Aguarda mais 2 segundos antes de iniciar a interação com o jogador.
    time.sleep(2)

    # Inicia um laço infinito para permitir várias perguntas na mesma partida.
    # O laço continuará até que o jogador escolha não fazer outra pergunta.
    while True:

        # Solicita ao jogador que digite uma pergunta.
        # O caractere \n insere uma quebra de linha antes do texto,
        # deixando um espaço visual entre as interações.
        pergunta = input("\nFaça sua pergunta: ")

        # Escolhe aleatoriamente um dos elementos da lista "respostas".
        # A função random.choice() recebe uma sequência e devolve
        # um de seus elementos.
        resposta = random.choice(respostas)

        # Exibe no terminal a resposta que foi selecionada.
        print(resposta)

        # Pergunta se o jogador deseja fazer outra pergunta.
        # strip() remove espaços em branco no início e no final da entrada.
        # lower() converte as letras para minúsculas, permitindo reconhecer
        # respostas como "SIM", "Sim" e "sim" da mesma maneira.
        continuar = input(
            "\nQuer fazer outra pergunta? (sim/não): "
        ).strip().lower()

        # Verifica se a resposta do jogador é diferente de "sim".
        # Se for qualquer outra entrada, o programa encerra a partida.
        if continuar != "sim":

            # Exibe uma mensagem de despedida.
            print("Tchau! Espero ter ajudado.")

            # Interrompe o laço while, encerrando a repetição das perguntas.
            break


# Chama a função principal para iniciar o jogo.
# Sem esta chamada, a função seria definida, mas seu conteúdo não seria
# executado automaticamente.
magic_ball()
