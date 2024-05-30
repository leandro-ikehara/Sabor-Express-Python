from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Abacaxi', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paodequeijo = Prato('Pão de Queijo', 3.0, 'O melhor pão de queijo da cidade')
prato_paodequeijo.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paodequeijo)

def main():
    # Restaurante.listar_restaurantes()
    # print(bebida_suco)
    # print(prato_paodequeijo)
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
