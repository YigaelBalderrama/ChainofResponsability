from lib.MedicPersonal import MedicPersonal


class GeneralMedic(MedicPersonal):

    def handle_consult(self):
        print("Toma un poco de Sumatriptán")
        resp=self.ask_to_pacient()
        if resp == 'yes':
            pass
        elif self._successor is not None:
            print("OK, pasa con un Neurologo")
            self._successor.handle_consult()
