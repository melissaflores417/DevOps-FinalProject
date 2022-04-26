import random
from player import Card
from player import Player

def play_game():
            i = 0
            j = 0
            Hands = []
            best_Hand = []
            Individual = []
            
            Players = int(input("How many Players(1-10): "))
            
            
            if Players >= 1 and Players <= 10:   
                for i in Card.Ranks.keys():
                    for j in Card.Suits.values():
                        Individual.append(i+j)
                    
                random.shuffle(Individual)
                x = 5
                number_of_participants = Players
                list_of_lists = [Individual[i:i+x] for i in range(0, len(Individual), x)]


                for i in range(number_of_participants):
            
                    print('{} -> {}'.format(Player.Sort_Hand(list_of_lists[i]),Player.Check_Hand(list_of_lists[i])))
                    best_Hand.append(Player.Check_Hand(list_of_lists[i]))

                print('\n')
                print('{} is the best hand!'.format(min(best_Hand)))
                print("\n")
                print("Please Enter '0' If You'd To Exit\n")
                play_game()
                
            elif Players == 0:
                print("\nHave A Good Day!\n")
                
            else:
                print("\nMaximum Number Of Players is 10!\n")
                play_game()        
   


if __name__ == "__main__":
    play_game()
