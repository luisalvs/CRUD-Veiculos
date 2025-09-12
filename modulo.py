
LISTA_VEICULOS_NOVOS = []
LISTA_VEICULOS_SEMINOVOS = []


class Carro:
    # Simula dados do veículo
    def __init__(self, modelo, marca, ano):
        self.placa = str
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.hodometro = 0

    def cadastrar_veiculo(self):
        placa = input('Placa: ')
        LISTA_VEICULOS_NOVOS.append(placa)
        print(LISTA_VEICULOS_NOVOS)

    def exibir_veiculo(self):
        print(
            f'Modelo: {self.modelo} \nMarca: {self.marca} \nAno: {self.ano}')


veiculo1 = Carro('Civic', 'Honda', '2020')
veiculo1.cadastrar_veiculo()
