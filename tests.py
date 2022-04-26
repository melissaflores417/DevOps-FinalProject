import unittest
from hand import Hand
from player import Player

class TestRoyal(unittest.TestCase):
    def test_Royal_Flush_1(self):
        result = Hand.RoyalFlush(["1H", "JH", "QH", "KH", "AH"])
        self.assertEqual(result, True)

    def test_Royal_Flush_2(self):
        result = Hand.RoyalFlush(["1H", "3H", "JH", "KH", "AH"])
        self.assertEqual(result, False)
    
    def test_Royal_Flush_3(self):
        result = Hand.RoyalFlush(["1C", "JH", "QH", "KH", "AH"])
        self.assertEqual(result, False)

    def test_Royal_Flush_4(self):
        result = Hand.RoyalFlush(["4H", "5H", "6H", "7H", "8H"])
        self.assertEqual(result, False)
   
class TestStraight(unittest.TestCase):

    def test_Straight_Flush_1(self):
        result = Hand.Straight(["2H", "3H", "4H", "5H", "6H"])
        self.assertEqual(result, True)

    def test_Straight_Flush_2(self):
        result = Hand.Straight(["1H", "3H", "5H", "7H", "9H"])
        self.assertEqual(result, False)
    
      # Case where it's not a Flush
    def test_Straight_Flush_3(self):
        result = Hand.Straight(["2C", "3H", "4H", "5H", "6H"])
        self.assertEqual(result, False)

    # Royal Flush is true but as there is a higher rank that the hand applies to, It's been set to False as it is of a higher rank i.e Royal Flush
    def test_Straight_Flush_4(self):
        result = Hand.Straight(["1H", "JH", "QH", "KH", "AH"])
        self.assertEqual(result, False)

 
class TestFour(unittest.TestCase):
    def test_Four_Of_A_Kind_1(self):
        result = Hand.FourofaKind(["4H", "4C", "4D", "4S", "5H"])
        self.assertEqual(result, True)

    def test_Four_Of_A_Kind_2(self):
        result = Hand.FourofaKind(["4H", "4C", "4D", "7H", "9H"])
        self.assertEqual(result, False)

class TestFull(unittest.TestCase):
    def test_Check_Full_House_1(self):
        result = Hand.Full(["4H", "4C", "4D", "5S", "5H"])
        self.assertEqual(result, True)

    def test_Check_Full_House_2(self):
        result = Hand.Full(["4H", "4C", "4D", "7H", "9H"])
        self.assertEqual(result, False)

class TestFlush(unittest.TestCase):
    def test_Check_Flush_1(self):
        result = Hand.Check_Flush(["2H", "4H", "6H", "1H", "KH"])
        self.assertEqual(result, True)

    def test_Check_Flush_2(self):
        result = Hand.Check_Flush(['2S', '3D', '4S', '6S', '8S'])
        self.assertEqual(result, False)

class TestCheckStraight(unittest.TestCase):
        
    def test_Check_Check_Straight_1(self):
        result = Hand.Check_Straight(["4D", "5C", "6H", "7H", "8S"])
        self.assertEqual(result, True)
    
    def test_Check_Check_Straight_2(self):
        result = Hand.Check_Straight(['2S', '3D', '4S', '6S', '8S'])
        self.assertEqual(result, False)

class TestThree(unittest.TestCase):
    def test_Three_Of_A_Kind_1(self):
        result = Hand.ThreeofaKind(["3H", "3D", "3C", "7H", "8H"])
        self.assertEqual(result, True)
     
# integration tests


#Test the interaction between the player and hand class. checks if hand is correct such as royal flush, straight, FourofaKind.
# Test interaction between the player and Check Hand method which calls functions from the hand class.
class TestRoyalFlushHand(unittest.TestCase):
    def test_Check_Hand(self):
        result = Player.Check_Hand(["1H", "JH", "QH", "KH", "AH"])
        self.assertEqual(result,1)

    def test_Check_Hand_2(self):
        result = Player.Check_Hand(["2H", "3H", "4H", "5H", "6H"])
        self.assertEqual(result, 2)

    def test_Check_Hand_3(self):
        result = Player.Check_Hand(["3H", "3D", "3C", "3S", "2H"])
        self.assertEqual(result, 3)
 
    def test_Check_Hand_4(self):
        result = Player.Check_Hand(["2H", "2D", "2C", "3S", "3D"])
        self.assertEqual(result, 4)

    def test_Check_Hand_5(self):
        result = Player.Check_Hand(["2H", "3H", "5H", "9H", "1H"])
        self.assertEqual(result, 5)

    def test_Check_Hand_6(self):
        result = Player.Check_Hand(["3H", "4D", "5C", "6S", "7H"])
        self.assertEqual(result, 6)

    def test_Check_Hand_7(self):
        result = Player.Check_Hand(["2H", "2D", "2C", "6S", "7H"])
        self.assertEqual(result, 7)




if __name__ == "__main__":
    unittest.main()
