from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('MexiCu', 'Mexicana')
restaurante_japones = Restaurante('Diapa', 'Japonesa')

restaurante_mexicano.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
