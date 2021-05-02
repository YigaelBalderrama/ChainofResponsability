from lib.Neurologist import Neurologist
from lib.GeneralMedic import GeneralMedic


def main():
    dr_Sanchez = Neurologist()
    dr_Rodriguez = GeneralMedic(dr_Sanchez)
    dr_Rodriguez.handle_consult()


main()
