from abc import ABC, abstractmethod

class Monitor(ABC):
    @abstractmethod
    def aumentarclaridade(self, numero):
        pass
    @abstractmethod
    def diminuirclaridade(self, numero):
        pass


class MonitorFullHD(Monitor):
    def aumentarclaridade(self, numero):
        print(f'Aumentando a claridade em {numero}')
    
    
    def diminuirclaridade(self, numero):
        print(f'Diminuindo a claridade em {numero}')


claridade = MonitorFullHD()
claridade.aumentarclaridade(10)
claridade.diminuirclaridade(15)
