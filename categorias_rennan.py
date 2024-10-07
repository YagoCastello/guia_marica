from tkinter import *

import ui







# Funções individuais de exploração
def explorar_praia():
    praias = [
        {"name": "Praia de Ponta negra", "image": "images/praia1.png", "description": "A Praia de Ponta Negra, em Maricá, é um verdadeiro paraíso carioca, conhecida por suas águas cristalinas e paisagens deslumbrantes. Com um extenso trecho de areia fina e dourada.", "gallery": ["images/praia1.png", "images/praia1_1.png"]},
        {"name": "Praia da Barra", "image": "images/praia2.png", "description": "A Praia da Barra de Maricá é um verdadeiro paraíso para os amantes da natureza e da tranquilidade. Localizada na costa do Rio de Janeiro.", "gallery": ["images/praia2.png","images/praia2_1.png"]},
        {"name": "Praia do Francês", "image": "images/praia2.png", "description": "A Praia do Francês, em Maricá, é um destino encantador que combina natureza exuberante com uma atmosfera relaxante. Com suas águas claras e mornas.", "gallery": ["images/praia2.png","images/praia2_1.png"]}
    ]

    global all_items
    ui.all_items.extend(praias)  # Adiciona a lista global

    # Retorna o nome do botão e os itens
    return "Praias", praias

def explorar_bares():
    bares = [
        {"name": "Bar 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Bar 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items
    ui.all_items.extend(bares)  # Adiciona a lista global

    # Retorna o nome do botão e os itens
    return "Bares", bares


def explorar_restaurantes():
    restaurantes = [
        {"name": "Bar 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Bar 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items
    ui.all_items.extend(restaurantes)  # Adiciona a lista global

    # Retorna o nome do botão e os itens
    return "Restaurantes", restaurantes

def explorar_trilhas():
    trilhas = [
        {"name": "Trilha da pedra do Macaco", "image": "images/bar1.png", "description": "A Trilha da Pedra do Macaco, em Maricá, é um passeio imperdível para os amantes da natureza e da aventura. Com cerca de 1,5 km de extensão, a trilha leva os visitantes por uma caminhada em meio à vegetação exuberante da Mata Atlântica.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Trilha da Pedra do elefante", "image": "images/bar2.png", "description": "A Trilha da Pedra do Elefante, em Maricá, é uma experiência única para os amantes da natureza e do trekking. Com uma extensão de aproximadamente 1,5 km, essa trilha leva os visitantes por um caminho repleto de vegetação nativa da Mata Atlântica.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items
    ui.all_items.extend(trilhas)  # Adiciona a lista global

    # Retorna o nome do botão e os itens
    return "Trilhas", trilhas

def explorar_cultura():
    cultura = [
        {"name": "Bar 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Bar 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items
    ui.all_items.extend(cultura)  # Adiciona a lista global

    # Retorna o nome do botão e os itens
    return "Cultura", cultura


def explorar_lagoas():
    lagoas = [
        {"name": "Bar 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Bar 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items
    ui.all_items.extend(lagoas)  # Adiciona a lista global

    # Retorna o nome do botão e os itens
    return "Lagoas", lagoas


def explorar_boates():
    boates = [
        {"name": "Bar 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Bar 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items
    ui.all_items.extend(boates)  # Adiciona a lista global

    # Retorna o nome do botão e os itens
    return "Boates", boates


def explorar_hoteis_e_pousados():
    hoteis_e_pousados = [
        {"name": "Pousada Casa e mar", "image": "images/bar1.png", "description": "A Pousada Casa e Mar, em Maricá, é um refúgio encantador que combina conforto e aconchego em um ambiente à beira-mar..", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Pousada Potigua", "image": "images/bar2.png", "description": "Com uma arquitetura charmosa e aconchegante, a pousada oferece um ambiente acolhedor, ideal para famílias, casais e grupos de amigos.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items
    ui.all_items.extend(hoteis_e_pousados)  # Adiciona a lista global

    # Retorna o nome do botão e os itens
    return "Hoteis_e_pousados", hoteis_e_pousados


def explorar_estacionamento():
    estacionamento  = [
        {"name": "Bar 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Bar 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items
    ui.all_items.extend(estacionamento )  # Adiciona a lista global

    # Retorna o nome do botão e os itens
    return "Estacionamento ", estacionamento