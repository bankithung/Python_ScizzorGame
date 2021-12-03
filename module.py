import random
class Sgame:
    def __init__(self,name):
        self.name =name
    def game(self):
        gam = ['st','p','s']
        a=" "
        while True:
            print("-"*15)
            while True:
                usrinputs =input("st-stone\np-paper\ns-scizzor\ne-exit\n> ").lower()
                if usrinputs.isalpha() and (usrinputs =='s' or usrinputs == 'p' or usrinputs == 'st'or 'e'):
                    
                    break
                else:
                    print("Re-enter\n")
                    continue
            compinputs = random.choice(gam)
            if(usrinputs=='e'):
                print("Exiting...")
                exit()
            else:
                print(f"{self.name} input: {usrinputs}\nComp input: {compinputs}")
                print("-"*15)
                if usrinputs == compinputs:
                    print(f"{a:20}Draw!!!")
                    continue
                elif (usrinputs == 'st' and compinputs == 's') or (usrinputs == 'p' and compinputs == 'st') or (usrinputs == 's' and compinputs == 'p'):
                    print(f"{a:20}{self.name} Wins")
                elif (compinputs == 'st' and usrinputs == 's') or (compinputs == 'p' and usrinputs == 'st') or (compinputs == 's' and usrinputs == 'p'):
                    print(f"{a:20}Comp wins")
            