# Python Start

class Player(object):
    health = []
    # Player turn function. This is what is called when running "pythonwarrior"
    def play_turn(self, warrior):
        import time
        # Check current hp at start of turn and report to screen
        start_hp = warrior.health()
        print(start_hp)
        looked_ahead = []
        looked_ahead = warrior.look()
        print looked_ahead
        print "looked_ahead[0]: ", looked_ahead[0]
        print "looked_ahead[0]: ", looked_ahead[1]
        time.sleep(5) # pause for 5 seconds
        if warrior.feel().is_wall():
            warrior.pivot_()
            self.health=start_hp
            return
        if warrior.feel('backward').is_captive():
            warrior.rescue_('backward')
            self.health=start_hp
            return
        if warrior.feel('backward').is_wall():
            if start_hp < 20:
                if warrior.feel().is_enemy():
                    warrior.attack_()
                else:
                    warrior.rest_()
            else:
                if warrior.feel().is_enemy():
                    warrior.attack_()
                else:
                    for x in looked_ahead:
                        if x == 'Captive':
                            if warrior.feel().is_empty:
                                warrior.walk_()
                            else:
                                warrior.rescue_()
                            self.health = start_hp
                            return
                        if x == "Wizard":
                            warrior.shoot_()
                            self.health = start_hp
                            return
                    if looked_ahead[1] == "Captive":
                        warrior.walk_()
                        self.health=start_hp
                        return
                    if looked_ahead[2] == "Wizard":
                        warrior.shoot_()
                        self.health=start_hp
                        return
                    else:
                        if looked_ahead[2] == "Wizard":
                            warrior.shoot_()
                        else:
                            warrior.walk_()
            self.health = start_hp
            print(self.health)
            print("End of turn, back was to the wall at start.")
            return
        if self.health > start_hp:
            if start_hp < 16:
                if warrior.feel().is_enemy():
                    warrior.attack_()
                else:
                    warrior.walk_('backward')
                    print("Walked backward A")
            else:
                if warrior.feel().is_enemy():
                    warrior.attack_()
                else:
                    warrior.walk_()
                    print("Walked forward on first turn or after being hurt.")
            self.health = start_hp
            print(self.health)
            print("End of turn from getting hit")
            return
        else:
            if warrior.feel().is_enemy():
                warrior.attack_()
                self.health = start_hp
                return
            if warrior.feel().is_captive():
                warrior.rescue_()
                self.health = start_hp
                return
            else:
                if start_hp < 20:
                    if warrior.feel('backward').is_empty():
                        warrior.walk_('backward')
                    else:
                        warrior.rest_()
                else:
                    if looked_ahead[1] == "Wizard":
                        warrior.shoot_()
                        self.health=start_hp
                        return
                    else:
                        if looked_ahead[2] == "Wizard":
                            warrior.shoot_()
                        else:
                            warrior.walk_()
        self.health = start_hp
        print(self.health)
        print("End of turn, wasn't hit and wasn't back to the wall.")
