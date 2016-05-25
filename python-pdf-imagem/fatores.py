class Fatores(object):
    #
    # Converte a pontuação do objeto pesquisado em dicionário
    #
    def converter_pontuacao(self, pesq):
        return {
            'lid': pesq.perfil.lid,
            'empr': pesq.perfil.empr,
            'com': pesq.perfil.com,
            'arg': pesq.perfil.arg,
            'vel': pesq.perfil.vel,
            'prat': pesq.perfil.prat,
            'det': pesq.perfil.det,
            'orga': pesq.perfil.orga,
            'cnor': pesq.perfil.cnor,
            'perc': pesq.perfil.perc,
            'intu': pesq.perfil.intu,
            'crit': pesq.perfil.crit,
            'decir': pesq.perfil.decir,
            'cria': pesq.perfil.cria,
            'ener': pesq.perfil.ener,
        }

    #
    # Retorna a pontuação do fator do pesquisado
    #
    def retornar_pontuacao(self, pesq, sigla):
        pontuacao = self.converter_pontuacao(pesq)

        if sigla in pontuacao:
            return pontuacao[sigla]
        else:
            return None

    #
    # Retorna o dicionário com todos os valores de cada fator
    #
    def retornar_fatores(self):
        lid = {
            'id'        : 1,
            'sigla'     : "lid",
            'titulo'    : "Liderança",
            'alto'      : "Espírito de chefia, liderança, autoridade, ascendência, habilidade para coordenar ou comandar grupos, exercer influências sobre o pensamento e comportamento de outras pessoas. Capacidade para conduzir pessoas na busca pelos resultados que se pretende.",
            'alto_pres' : "Capacidade de ouvir quando questionado, controle da competitividade. Não ser individualista.",
            'baixo'     : "Harmonia e cooperação.",
            'baixo_pres': "Competição externa.",
        }

        empr = {
            'id'        : 2,
            'sigla'     : "empr",
            'titulo'     : "Empreendedorismo",
            'alto'       : "Iniciativa para se envolver em novos negócios, não temer correr riscos e seguir em frente na busca de resultados.",
            'alto_pres'  : "Capacidade para trabalhar em equipe.",
            'baixo'      : "Trabalha bem sob comando direto ou indireto.",
            'baixo_pres' : "Oportunidades de novos. Negócios e mercados.",
        }

        com = {
            'id'        : 3,
            'sigla'     : "com",
            'titulo'     : "Comunicação",
            'alto'       : "Demonstrar habilidade, tendência ou vocação para se comunicar, dialogar e se fazer entender, de forma oral ou escrita. Improvisar,desenvolver e aplicar processos de comunicação a partir de um ou pouco elementos.",
            'alto_pres'  : "Poder de síntese, objetividade, ser fiel aos objetivos da mensagem.",
            'baixo'      : "Foco em produtos. Reserva, quietude.",
            'baixo_pres' : "Oralidade para apresentações, empatia.",
        }

        arg = {
            'id'        : 4,
            'sigla'     : "arg",
            'titulo'     : "Argumentação",
            'alto'       : "Capacidade para levar o outro a mudar de atitude, convencer, persuadir. Não significa necessariamente alto nível de extroversão.",
            'alto_pres'  : "Limite dos objetivos que deseja atingir.",
            'baixo'      : "Não significa necessariamente baixo nível de comunicação e sim baixo nível de convencimento.",
            'baixo_pres' : "Capacidade de ajudar a equipe a decidir",
        }

        vel = {
            'id'        : 5,
            'sigla'     : "vel",
            'titulo'     : "Velocidade",
            'alto'       : "Capacidade para administrar várias atividades obtendo sinergia entre elas. Competência para entrar logo em ação. Economiza ou ganha tempo entre as várias etapas de uma tarefa.",
            'alto_pres'  : "Controle da impulsividade.",
            'baixo'      : "Paciência, tranqüilidade, estabilidade, executa bem trabalhos rotineiros e repetitivos, calmo, deliberado.",
            'baixo_pres' : "Capacidade para priorizar trabalhos e cumprimento de prazos e entregas.",
        }

        prat = {
            'id'        : 6,
            'sigla'     : "prat",
            'titulo'     : "Praticidade",
            'alto'       : "Administra várias atividades obtendo sinergia entre elas. Competência para entrar logo em ação, sem desperdiçar tempo em elucubrações e detalhes.  Economiza ou ganha tempo entre as várias etapas de uma tarefa.",
            'alto_pres'  : "Atenção aos detalhes críticos.",
            'baixo'      : "Foco em uma atividade paralela a estratégia.",
            'baixo_pres' : "Cumpre prazos.",
        }

        det = {
            'id'        : 7,
            'sigla'     : "det",
            'titulo'     : "Detalhe",
            'alto'       : "Observa detalhes. Faz exposição de forma minuciosa, pormenorizada, com minudência.",
            'alto_pres'  : "Objetividade, capacidade para delegar.",
            'baixo'      : "Facilidade para delegar, tem macro visão das situações",
            'baixo_pres' : "Cuidado ao subestimar os detalhes considerados críticos de todo e qualquer processo.",
        }

        orga = {
            'id'        : 8,
            'sigla'     : "orga",
            'titulo'     : "Organização",
            'alto'       : "Visão macro e micro dos processos. Mantém a ordem. Não significa necessariamente cumprimento de prazos. O que determina cumprimento de prazos é o fator \"velocidade\". Planeja para melhor realização de tarefas. Realiza com métodos. Tem visão sistêmica dos processos.",
            'alto_pres'  : "Não perder tempo desnecessário com fatores que não agregam valor.",
            'baixo'      : "Atinge resultados isolados de uma estratégia macro.",
            'baixo_pres' : "Atingir resultados através de começo meio e fim dos processos.",
        }

        cnor = {
            'id'        : 9,
            'sigla'     : "cnor",
            'titulo'     : "Cumprimento à Normas",
            'alto'       : "Acata procedimentos ou atos, regras, princípios e padrões pré-estabelecidos.",
            'alto_pres'  : "Flexibilidade",
            'baixo'      : "Quebra normas e regras, não sente obrigação de seguir estritamente as regras pré-estabelecidas.",
            'baixo_pres' : "Senso de julgamento",
        }

        perc = {
            'id'        : 10,
            'sigla'     : "perc",
            'titulo'     : "Percepção",
            'alto'       : "Capacidade para perceber a diferença entre dados, fatos e movimentos. Formar ideias, entender e compreendê-las.",
            'alto_pres'  : "Ponderação",
            'baixo'      : "Trabalha melhor com “inputs” da equipe",
            'baixo_pres' : "Considerar relação dos fatos",
        }

        intu = {
            'id'        : 11,
            'sigla'     : "intu",
            'titulo'     : "Intuição",
            'alto'       : "Ato de ver, perceber, discernir independente de raciocínio, análise ou verificação.",
            'alto_pres'  : "Lógica ao tomar decisões de alta criticidade",
            'baixo'      : "Utiliza razão, dados, fatos na tomada de decisão",
            'baixo_pres' : "Detecção de novas oportunidades",
        }

        crit = {
            'id'        : 12,
            'sigla'     : "crit",
            'titulo'     : "Criticidade",
            'alto'       : "Observar, entender, julgar e avaliar. Propõe examinar um princípio ou ideia, fato ou percepção, com a finalidade de produzir umaapreciação logica.",
            'alto_pres'  : "Liberdade de ação da equipe",
            'baixo'      : "Baixo nível de observação de idéias ou fatos.",
            'baixo_pres' : "Capacidade para discernir entre o que é de acordo ou não com os objetivos e metas.",
        }

        decir = {
            'id'        : 13,
            'sigla'     : "decir",
            'titulo'     : "Decisão Racional",
            'alto'       : "Utiliza a razão e fatos concretos para entender situações e tomar decisões.",
            'alto_pres'  : "Empatia e trabalho em equipe.",
            'baixo'      : "Subjetivo, emocional na tomada de decisões.",
            'baixo_pres' : "Atenção para não procrastinar ao ter que tomar decisões que evolvam pessoas.",
        }

        cria = {
            'id'        : 14,
            'sigla'     : "cria",
            'titulo'     : "Criatividade",
            'alto'       : "Talento para criar, ousadia para mudar o pré-estabelecido. Improvisar, buscar caminhos ainda não trilhados. Aventurar novas soluções. Distinguir-se pela aptidão intelectual para criar , inovar. Transformar a curiosidade em ação. Ver de forma nova aquilo quejá existe e não ficar preso a padrões. Pensar além.",
            'alto_pres'  : "Visão sistêmica, processual.",
            'baixo'      : "Segue padrões e normas pré-estabelecidos.",
            'baixo_pres' : "Aproveitar oportunidades de mudanças e resolução de problemas, considerando formas diferentes das já existentes.",
        }

        ener = {
            'id'        : 15,
            'sigla'     : "ener",
            'titulo'     : "Energia",
            'alto'       : "Vigor físico e/ou mental. Disposição e capacidade para se manter atento e  na realização de tarefas com a mesma energia.",
            'alto_pres'  : "Administração do tempo entre atuação profissional e lazer",
            'baixo'      : "Pode estar dispersivo.",
            'baixo_pres' : "Atenção especial aos trabalhos de alta periculosidade, críticos e de alto grau de detalhe.",
        }

        return [lid, empr, com, arg, vel, prat, det, orga, cnor, perc, intu, crit, decir, cria, ener]