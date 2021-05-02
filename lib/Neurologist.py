from lib.MedicPersonal import MedicPersonal


class Neurologist(MedicPersonal):

    def handle_consult(self):
        print("OK te haremos unos examenes")
        resp = self.ask_to_pacient()
        if resp == 'yes':
            print("Vuelve a consulta en 2 dias")
        elif self._successor is not None:
            self._successor.handle_request()
        else:
            print("Llamaremos a otro especialista..")