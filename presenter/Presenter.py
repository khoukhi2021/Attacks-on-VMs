class Presenter:

    def start(self):
        # Launch the graphic user interface
        pass

    def display_results(self):
        # Gives the results to the graphic user interface with the right format
        pass

    def get_results(self):
        # Gets the results form the attack and transform them in the right format
        pass

    def init(self):
        # Should be used to set all the things we could need on the app launch
        pass

    def launch_attack(self, attack_type: str):
        # Launch the attack selected, is called by the graphic user interface when an attack launch is clicked
        # I know if, elseif clause isn't sexy but for now I have no other idea
        pass
