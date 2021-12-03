import random
class Sgame:
    def __init__(self,name):
        self.name =name
    def sgame(self):
        gam = ['st','p','s']
        a=" "
        while True:
            
            while True:
                print("-"*15)
                usrinputs =input("st-stone\np-paper\ns-scizzor\ne-exit\n> ").lower()
                if usrinputs.isalpha() and (usrinputs =='s' or usrinputs == 'p' or usrinputs == 'st'or usrinputs =='e'):
                    
                    break
                else:
                    print("-"*15)
                    print(f"{a:20}Re-enter")
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
            
