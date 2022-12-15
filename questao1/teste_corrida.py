from corrida import Corrida

hora_ini = int((input("Digite a hora de início da corrida: ")))
min_ini = int((input("Digite os minutos de início da corrida: ")))
seg_ini = int((input("Digite os segundos de início da corrida: ")))
hora_fim = int((input("Digite a hora de fim da corrida: ")))
min_fim = int((input("Digite os minutos de fim da corrida: ")))
seg_fim = int((input("Digite os segundos de fim da corrida: ")))
distancia = int((input("Digite a distância percorrida: ")))

corrida1 = Corrida(hora_ini, min_ini, seg_ini, hora_fim,
                   min_fim, seg_fim, distancia)

corrida1.informarTempoTotal()
corrida1.informarVelocidadeMedia()
