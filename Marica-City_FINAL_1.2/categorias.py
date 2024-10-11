all_items = []

# Funções individuais de exploração
def explorar_praia():
    praias = [
        {"name": "Praia de Ponta negra", "image": "images/praia1.png", "description": "A Praia de Ponta Negra, em Maricá, é um verdadeiro paraíso carioca, conhecida por suas águas cristalinas e paisagens deslumbrantes. Com um extenso trecho de areia fina e dourada.", "gallery": ["images/praia1.png", "images/praia1_1.png", "images/praia1_2.png"]},
        {"name": "Praia da Barra", "image": "images/praia2.png", "description": "A Praia da Barra de Maricá é um verdadeiro paraíso para os amantes da natureza e da tranquilidade. Localizada na costa do Rio de Janeiro.", "gallery": ["images/praia2.png","images/praia2_1.png","images/praia2_2.png"]},
        {"name": "Praia de Itaipuaçu", "image": "images/praia3.png", "description": "A Praia do Corderinho, em Maricá, é um destino encantador que combina natureza exuberante com uma atmosfera relaxante. Com suas águas claras e mornas.", "gallery": ["images/praia3.png","images/praia3_1.png","images/praia3_2.png"]}
   ]

    global all_items

    all_items.extend(praias)
    return "Praias", praias,r"images\praia_cat.jpg"


def explorar_bares():
    bares = [
        {"name": "Bora Bora", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png","images/bar1_2.png"]},
        {"name": "Skull Beer Bar", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png","images/bar2_2.png"]},
        {"name": "Maltz Beer Garden", "image": "images/bar3.png", "description": "Bar histórico, funcionando a mais de 50 anos na cidade", "gallery": ["images/bar3.png","images/bar3_1.png","images/bar3_2.png"]},
    ]
    global all_items

    all_items.extend(bares)
    return "Bares", bares,r"images\bar_cat.jpg"


def explorar_restaurantes():
    restaurantes = [
        {"name": "Horus", "image": "images/restaurante1.png", "description": "Lorem ipsum bla bla bla ", "gallery": ["images/restaurante1.png", "images/restaurante1_1.png", "images/restaurante1_2.png"]},
        {"name": "Ze Carlos", "image": "images/restaurante2.png", "description": "Lorem ipsum bla bla bla ", "gallery": ["images/restaurante2.png","images/restaurante2_1.png","images/restaurante2_2.png"]},
        {"name": "Casa grill", "image": "images/restaurante3.png", "description": "Lorem ipsum bla bla bla ", "gallery": ["images/restaurante3.png","images/restaurante3_1.png","images/restaurante3_2.png"]},
    ]


    global all_items

    all_items.extend(restaurantes)
    return "Restaurantes", restaurantes,r"images\restaurante_cat.jpg"

def explorar_trilhas():
    trilhas = [
        {"name": "Trilha da pedra do Macaco", "image": "images/trilha1.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/trilha1.png","images/trilha1_1.png","images/trilha1_2.png"]},
        {"name":"Trilha da Pedra do elefante", "image": "images/trilha2.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/trilha2.png","images/trilha2_1.png","images/trilha2_2.png"]},
        {"name":"Trilha do Spar", "image": "images/trilha3.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/trilha3.png","images/trilha3_1.png","images/trilha3_2.png"]},
       ]
    global all_items

    all_items.extend(trilhas)
    return "Trilhas", trilhas,r"images\trilhas_cat.jpg"

def explorar_cultura():
    cultura = [
        {"name": "Casa Darcy Ribeiro", "image": "images/cultura1.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/cultura1.png","images/cultura1_1.png","images/cultura1_2.png"]},
        {"name":"Casa de cultura", "image": "images/cultura2.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/cultura2.png","images/cultura2_1.png","images/cultura2_2.png"]},
        {"name":"Fazenda Joaquim P", "image": "images/cultura3.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/cultura3.png","images/cultura3_1.png","images/cultura3_2.png"]},
        ]
    global all_items

    all_items.extend(cultura)
    return "Cultura", cultura,r"images\cultura_cat.jpg"


def explorar_lagoas():
    lagoas = [
        {"name": "Lagoa de Jacaroa", "image": "images/lagoa1.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/lagoa1.png","images/lagoa1_1.png","images/lagoa1_2.png"]},
        {"name": "Lagoa de araçatiba ", "image": "images/lagoa2.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/lagoa2.png","images/lagoa2_1.png","images/lagoa2_2.png"]},
        {"name": "Lagoa da Garota", "image": "images/lagoa3.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/lagoa3.png","images/lagoa3_1.png","images/lagoa3_2.png"]},
        ]
    global all_items

    all_items.extend(lagoas)
    return "Lagoas", lagoas,r"images\lagoas_cat.jpg"


def explorar_boates():
    boates = [
        {"name": "Mahalo", "image": "images/boate1.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/boate1.png","images/boate1_1.png","images/boate1_2.png"]},
        {"name": "Império", "image": "images/boate2.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/boate2.png","images/boate2_1.png","images/boate2_2.png"]},
        {"name":"Maria do Céu", "image": "images/boate3.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/boate3.png","images/boate3_1.png","images/boate3_2.png"]},
        ]
    global all_items

    all_items.extend(boates)
    return "Boates", boates,r"images\boates_cat.jpg"


def explorar_hoteis_e_pousados():
    hoteis_e_pousados = [
        {"name": "Casa&Mar", "image": "images/pousada1.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/pousada1.png","images/pousada1_1.png","images/pousada1_2.png"]},
        {"name": "Pousada Potigua", "image": "images/pousada2.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/pousada2.png","images/pousada2_1.png","images/pousada2_2.png"]},
        {"name":"Pousada Maricá", "image": "images/pousada3.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/pousada3.png","images/pousada3_1.png","images/pousada3_2.png"]},
        ]
    global all_items

    all_items.extend(hoteis_e_pousados)
    return "Hoteis/ Pousadas", hoteis_e_pousados,r"images\hotel_cat.jpg"


def explorar_estacionamento():
    estacionamento  = [
        {"name": "Estacionamento do Zé", "image": "images/estacionamento1.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/estacionamento1.png","images/estacionamento1_1.png","images/estacionamento1_2.png"]},
        {"name": "Estacionamento da Maria", "image": "images/estacionamento2.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/estacionamento2.png","images/estacionamento2_1.png","images/estacionamento2_2.png"]},
        {"name":"Estacionamento do Bil", "image": "images/estacionamento3.png", "description": "Lorem ipsum bla bla bla .", "gallery": ["images/estacionamento3.png","images/estacionamento3_1.png","images/estacionamento3_2.png"]},
      ]
    global all_items

    all_items.extend(estacionamento)
    return "Estacionamento ", estacionamento, r"images\estacionamento_cat.jpg"

