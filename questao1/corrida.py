class Corrida:

    def __init__(self, hora_ini, min_ini, seg_ini, hora_fim, min_fim, seg_fim, distancia):
        self.hora_ini = hora_ini
        self.min_ini = min_ini
        self.seg_ini = seg_ini
        self.hora_fim = hora_fim
        self.min_fim = min_fim
        self.seg_fim = seg_fim
        self.distancia = distancia

    def informarTempoTotal(self):
        horas_seg = abs((self.hora_fim * 3600) - (self.hora_ini * 3600))
        min_seg = abs((self.min_fim * 60) - (self.min_ini * 60))
        seg_totais = abs(self.seg_fim - self.seg_ini)
        horas_totais = horas_seg / 3600
        min_totais = min_seg / 60
        print(f"O tempo total foi de {horas_totais}h {min_totais}min {seg_totais}seg")

    def informarVelocidadeMedia(self):
        horas_seg = abs((self.hora_fim * 3600) - (self.hora_ini * 3600))
        min_seg = abs((self.min_fim * 60) - (self.min_ini * 60))
        horas_totais = horas_seg / 3600
        min_totais = min_seg / 60
        if min_totais > 30:
            horas_totais += 1
        velocidade_media = round(self.distancia / horas_totais, 2)
        print(
            f"A velocidade média foi de aproximadamente {velocidade_media}km/h")
