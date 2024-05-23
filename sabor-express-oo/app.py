from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Leandro', 8)
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 4)

restaurante_mexicano = Restaurante('MexiCu', 'Mexicana')
restaurante_mexicano.receber_avaliacao('Paulo', 3)
restaurante_japones = Restaurante('Diapa', 'Japonesa')
restaurante_japones.receber_avaliacao('Ana Paula', 5)

restaurante_mexicano.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
