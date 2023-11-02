class mensaje:
    def __init__(self, texto,fecha):
        self.texto = texto
        self.fecha = fecha
    def dump(self):
        return {
            'FECHA': self.fecha,
            'MENSAJE': self.texto
        }