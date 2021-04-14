from Model.ResultAttack.ResultCreator import ResultCreator
from Model.ResultAttack.ImagePCAP import ImagePCAP


class ResultInterface:

    def create_results(self, attack, content):
        if attack == 'VoIP Eavesdropping':
            return ResultCreator(attack,"Test.wav", content)
        elif attack == 'ARP Poisoning':
            return ResultCreator(attack,"ARP.xlsx",content)
        elif attack == 'DHCP Poisoning':
            return ResultCreator(attack,"DHCP.xlsx",content)
        elif attack == 'Extract Images':
            ImagePCAP("Model/ResultAttack/Results/PCAPs/"+content)
        else:
            return " "
