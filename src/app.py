# Assistente de Currículo e Vagas de Emprego

base_conhecimento = """
CURRÍCULO: Deve conter nome, contato, objetivo, experiência, formação e habilidades.
EXPERIÊNCIA: Pode incluir projetos pessoais, cursos e voluntariado.
VAGAS: Júnior exige pouca experiência.
ENTREVISTA: Pesquise a empresa e treine respostas.
"""

def assistente(pergunta):
    pergunta = pergunta.lower()

    if "currículo" in pergunta or "curriculo" in pergunta:
        return "Um currículo deve ser objetivo e conter suas principais experiências, formação e habilidades."

    elif "vaga" in pergunta:
        return "Vagas júnior geralmente exigem pouca experiência e valorizam vontade de aprender."

    elif "entrevista" in pergunta:
        return "Pesquise a empresa e treine respostas sobre suas experiências profissionais."

    elif "experiência" in pergunta:
        return "Você pode incluir projetos pessoais, cursos e trabalhos voluntários como experiência."

    else:
        return "Não tenho informações suficientes sobre isso. Tente perguntar sobre currículo, vagas ou entrevistas."

while True:
    user_input = input("Você: ")

    if user_input.lower() == "sair":
        print("Encerrando o assistente...")
        break

    resposta = assistente(user_input)
    print("Assistente:", resposta)
