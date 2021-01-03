from attack import AttackInterface


class ResultManagerInterface:

    def create_results(self, attack: AttackInterface):
        if attack == 'VoIP Eavesdropping':
            return "Test.wav"
        if attack == 'ARP Poisoning':
            return "ARP.xlsx"
        if attack == 'DHCP Poisoning':
            return "DHCP.xlsx"
        else:
            return " "
