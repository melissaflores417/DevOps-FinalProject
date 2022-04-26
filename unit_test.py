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
   
class TestStraight(unittest.TestCase):

    def test_Straight_Flush_1(self):
        result = Hand.Straight(["2H", "3H", "4H", "5H", "6H"])
        self.assertEqual(result, True)

    def test_Straight_Flush_2(self):
        result = Hand.Straight(["1H", "3H", "5H", "7H", "9H"])
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
     
class TestHand(unittest.TestCase):
    def test_Check_Hand(self):
        result = Player.Check_Hand(["1H", "JH", "QH", "KH", "AH"])
        self.assertEqual(result,1)

    def test_Check_Hand_2(self):
        result = Player.Check_Hand(["2H", "3H", "4H", "5H", "6H"])
        self.assertEqual(result, 2)

    def test_Check_Hand_3(self):
        result = Player.Check_Hand(["3H", "3D", "3C", "3S", "2H"])
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
