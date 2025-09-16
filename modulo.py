
LISTA_VEICULOS_NOVOS = []
LISTA_VEICULOS_SEMINOVOS = []


class Carro:
    # Simula dados do veículo
    def __init__(self):
        self.placa = input('Placa: ')
        self.modelo = input('Modelo: ')
        self.marca = input('Marca: ')
        self.ano = int(input('Ano: '))
        self.hodometro = 0

    def cadastrar_veiculo(self):
        LISTA_VEICULOS_NOVOS.append(
            {'Placa': self.placa, 'Modelo': self.modelo, 'Marca': self.marca, 'Ano': self.ano})

    def exibir_veiculo(self):
        print(
            f'Placa: {self.placa} \nModelo: {self.modelo} \nMarca: {self.marca} \nAno: {self.ano}')


veiculo1 = Carro()
veiculo1.cadastrar_veiculo()
veiculo1.exibir_veiculo()
