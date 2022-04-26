import numpy as np

class Card():
    Ranks = { "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "1": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    Suits = {"Clubs": "C", "Diamonds": "D", "Spades": "S", "Hearts": "H"}


class Hand():
    def RoyalFlush(array):
        
        if Hand.Check_Flush(array): 
            royal_values = [14,13,12,11,10] 
            royal_append = []
            for i in range(len(array)):
                royal_append.append(Card.Ranks.get(array[i][0]))
            
            for i in royal_values:
                if i not in royal_append: 
                    return False   
                
            return True
        return False

    def Straight(array):
        
        if not Hand.RoyalFlush(array): 
            if Hand.Check_Straight(array) and Hand.Check_Flush(array):
                return True
        
        return False
    
    def FourofaKind(array):
        if not Hand.Check_Flush(array) and not Hand.Check_Straight(array): 
            unique_values = []
            four_occurences = []
            for i in array: 
                unique_values.append(Card.Ranks.get(i[0])) 
                x = np.array(unique_values)
                for i in np.unique(x): 
        
                    if unique_values.count(i)==4: 
                
                        if i not in four_occurences:
                            four_occurences.append(i)
                
            
                if len(four_occurences)==1:
                    
                    return True
        
        return False

    def Full(array):
        new_array=[]
        for i in array: 
            new_array.append(Card.Ranks.get(i[0]))
        
        
        unique_values = []
        multiple_occurences=[]
        x = np.array(new_array)
        for i in np.unique(x): 
            
            if new_array.count(i)==2 or new_array.count(i)==3: 
                unique_values.append(i)
            
        
        
        if len(unique_values)==2: 
            
            for i in unique_values:
                if new_array.count(i)==2: 
                    multiple_occurences.insert(0,i)
                elif new_array.count(i)==3:
                    multiple_occurences.insert(1,i) 

        
        if len(multiple_occurences)==2:
            if new_array.count(multiple_occurences[0])==2 and new_array.count(multiple_occurences[1])==3:
            
                return True
            
            
        return False


    def Check_Flush(array):
        for i in range(len(array)-1):
            if array[i][1] != array[i+1][1]:
                return False
        return True
                
                                    

    def Check_Straight(array):
        
            for i in range(len(array)-1):
                if Card.Ranks.get(array[i][0])+1 != Card.Ranks.get(array[i+1][0]): 
                    return False
            return True


    def ThreeofaKind(array):
        
        if Hand.Full(array) and not Hand.FourofaKind(array): 
            return False
        else:
            unique_values = []
            multiple_occurences = []
            for i in array:
                unique_values.append(Card.Ranks.get(i[0]))
                x = np.array(unique_values)
                for i in np.unique(unique_values):
        
                    if unique_values.count(i)==3: 
                
                        if i not in multiple_occurences:
                            multiple_occurences.append(i)
                
                if len(multiple_occurences)==1:
                    
                    return True

        return False

    def Check_Two_Pairs(array):
            
        if not Hand.Full(array): 
            unique_values = []
            multiple_occurences = []
            for i in array:
                unique_values.append(Card.Ranks.get(i[0]))
                x = np.array(unique_values)
                for i in np.unique(unique_values):
        
                    if unique_values.count(i)==2: 
                
                        if i not in multiple_occurences:
                            multiple_occurences.append(i)
                
        
            if len(multiple_occurences)==2: 
                
                return True
        
        return False
            
    def Check_Pair(array):
            
        if not Hand.Full(array) and not Hand.Check_Two_Pairs(array):

            
            unique_values = []
            multiple_occurences = []
            for i in array:
                unique_values.append(Card.Ranks.get(i[0]))
                x = np.array(unique_values)
                for i in np.unique(unique_values):
        
                    if unique_values.count(i)==2:
                
                        if i not in multiple_occurences:
                            multiple_occurences.append(i)
                
        
            if len(multiple_occurences)==1:
            
                return True
        
        
        
        return False
