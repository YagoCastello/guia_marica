
from tkinter import *

import ui







# Funções individuais de exploração
def explorar_praia():
    praias = [
        {"name": "Praia 1", "image": "images/praia1.png", "description": "Uma das mais belas praias do Brasil.", "gallery": ["images/praia1.png", "images/praia1_1.png"]},
        {"name": "Praia 2", "image": "images/praia2.png", "description": "Famosa praia no Rio de Janeiro.", "gallery": ["images/praia2.png","images/praia2_1.png"]},
        {"name": "Praia 3", "image": "images/praia2.png", "description": "Famosa praia no Rio de Janeiro.", "gallery": ["images/praia2.png","images/praia2_1.png"]}
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
        {"name": "Bar 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Bar 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
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
        {"name": "Bar 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Bar 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
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


