class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}'.upper())
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_status(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_praca._nome = 'Casa Food'
restaurante_praca.alternar_status()
restaurante_pizza = Restaurante('pizza express', 'Pasta')

Restaurante.listar_restaurantes()