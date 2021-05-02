import  abc


class MedicPersonal(metaclass=abc.ABCMeta):

    def __init__(self, successor=None):
        self._successor = successor

    @staticmethod
    def ask_to_pacient():
        return input("De acuerdo con el diagnostico? yes/no")

    @abc.abstractmethod
    def handle_consult(self):
        pass
