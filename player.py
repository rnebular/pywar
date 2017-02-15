class Player(object):
    import time
    last_hp = []
    safe = True
    looked_ahead = []

    # Sub-function to check front using warrior.look()
    def check_ahead(self, warrior):
        self.looked_ahead = warrior.look()
        #print looked_ahead
        print(self.looked_ahead[0])
        print(self.looked_ahead[1])
        print(self.looked_ahead[2])
        return self.looked_ahead

    # Function to check if warrior was damaged last round.
    def safety_check(self, warrior):
        if self.last_hp > warrior.health():
            self.safe = False
            return
        else:
            self.safe = True
        return

    # Sub-function for action to take based on results from check_ahead()
    def take_action(self, warrior):
        if warrior.feel().is_stairs():
            warrior.walk_()
            return
        if 


    # Player turn function. This is what is called when running "pythonwarrior"
    def play_turn(self, warrior):
        import time
        #######################
        # Start play_turn run.
        #######################
        # Check current hp at start of turn and report to screen
        start_hp = warrior.health()
        print(start_hp)
        self.check_ahead(warrior)
        self.take_action(warrior)
        self.last_hp = start_hp
        print "End of code, waiting for action"
        time.sleep(1) # pause for 5 seconds
