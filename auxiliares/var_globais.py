import datetime

lista_de_documentos = ["", "Ato", "Nota Técnica"] # BARRA LATERAL

lista_de_tipos_de_ato = ["","Nomeação de CD", "Exoneração de CD", 
                            "Substitução de CD", "Recondução de CD", 
                            "Designação de FG", "Dispensa de FG", "Substitução de FG", 
                            "Designação de FCC", "Dispensa de FCC", "Substitução de FCC", "FCC não remunerada"] # FORMULÁRIO

lista_de_setores = ["", "DGP", "DGP/DAP", "REITORIA"] # FORMULÁRIO

lista_de_cds = ["","CD-01", "CD-02", "CD-03", "CD-04"]

lista_de_fgs = ["","FG-01", "FG-02", "FG-03"]

lista_finalidades_do_ato = ["", "Manutenção de Funções"]

lista_de_nome_funcoes = ["",
                         "Coordenador(a) de Pós-graduação", "Coordenador(a) de Graduação",
                         "Diretor(a)", "Vice-diretor(a)",
                         "Secretário(a)", "Decano(a)", "Prefeito"]

lista_de_tipos_funcoes = ["", "FCC", "FUNÇÃO NÃO REMUNERADA", "CD-01", "CD-02", "CD-03", "CD-04", "FG-01", "FG-02", "FG-03"] # FORMULÁRIO

lista_de_categorias_funcionais = ["", 
                                  "o servidor", "a servidora",
                                  "o docente", "a docente",
                                  "o Professor do Magistério Superior", "a Professora do Magistério Superior",]

###########################################################################################################################

# capturando ano
data_atual = datetime.date.today()
ano_atual = data_atual.year