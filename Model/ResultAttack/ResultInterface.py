from Model.Attack import AttackInterface
from Model.ResultAttack.ResultCreator import ResultCreator
from Model.ResultAttack.ImagePCAP import Recapper


class ResultInterface:

    def create_results(self, attack, content):
        if attack == 'VoIP Eavesdropping':
            return ResultCreator(attack,"Test.wav", content)
        elif attack == 'ARP Poisoning':
            return ResultCreator(attack,"ARP.xlsx",content)
        elif attack == 'DHCP Poisoning':
            return ResultCreator(attack,"DHCP.xlsx",content)
        elif attack == 'Extract Images':
            Recapper("Model/ResultAttack/Results/PCAPs/"+content)
        else:
            return " "
