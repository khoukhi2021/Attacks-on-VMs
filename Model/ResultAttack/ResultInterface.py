from Model.Attack import AttackInterface
from Model.ResultAttack.ResultCreator import ResultCreator


class ResultInterface:

    def create_results(self, attack, content):
        if attack == 'VoIP Eavesdropping':
            return ResultCreator(attack,"Test.wav", content)
        if attack == 'ARP Poisoning':
            return ResultCreator(attack,"ARP.xlsx",content)
        if attack == 'DHCP Poisoning':
            return ResultCreator(attack,"DHCP.xlsx",content)
        else:
            return " "
