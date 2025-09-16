
LISTA_VEICULOS_NOVOS = []
LISTA_VEICULOS_SEMINOVOS = []


class Carro:
    # Simula dados do veículo
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