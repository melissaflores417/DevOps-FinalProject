from hand import Card
from hand import Hand
class Player():

    def Check_Hand(hand):
        
        if Hand.RoyalFlush(hand):
            
            return 1
        
                                    
        if Hand.Straight(hand):
            
            return 2
                                    
        if Hand.FourofaKind(hand):
            
            return 3
                                    
        if Hand.Full(hand):
        
            return 4
                                    
        if Hand.Check_Flush(hand):
            
            return 5
                
        if Hand.Check_Straight(hand):
            
            return 6
                                    
        if Hand.ThreeofaKind(hand):
            
            return 7
        
        if Hand.Check_Two_Pairs(hand):
            
            return 8
        
        if Hand.Check_Pair(hand):
            
            return 9
        
    
        return 10 
                                    

    def Sort_Hand(hand):
        for i in range(len(hand)-1):
            for j in range(i+1, len(hand)):
                if Card.Ranks.get(hand[i][0]) > Card.Ranks.get(hand[j][0]):
                    temp= hand[i]
                    hand[i] = hand[j]
                    hand[j] = temp

        return hand
                    