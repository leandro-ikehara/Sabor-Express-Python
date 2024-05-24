from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Abacaxi', 5.0, 'grande')
prato_paodequeijo = Prato('Pão de Queijo', 3.0, 'O melhor pão de queijo da cidade')

def main():
    # Restaurante.listar_restaurantes()
    print(bebida_suco)
    print(prato_paodequeijo)


if __name__ == '__main__':
    main()
