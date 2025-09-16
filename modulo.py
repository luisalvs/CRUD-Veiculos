
LISTA_VEICULOS_NOVOS = []
LISTA_VEICULOS_SEMINOVOS = []


class Carro:
    # Simula dados do veículo
<<<<<<< HEAD
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
=======
    def __init__(self, placa, modelo, marca, ano):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.odometro = 0

    def exibir_veiculo(self):
        return f'Placa: {self.placa} \nModelo: {self.modelo} \nMarca: {self.marca} \nAno: {self.ano} \nOdometro: {self.odometro}'
    
    def incrementar_odometro(self, milhas):
            self.odometro += milhas

    def atualizar_odometro(self, milhas):
        if milhas > self.odometro:
            self.odometro = milhas
        else:
             print('Odômetro não pode ser menor que o valor')



user1 = Carro('IQI8593', 'Civic', 'Honda', 2020)

user1.add_odometro(100)
user1.exibir_veiculo()
>>>>>>> 139faefa12335486482ae16b0ba0e97e1dd415eb
