import unittest
import rover as rv

class RoverTest(unittest.TestCase):

    def test_must_turn_to_left(self):
        x, y, drc = rv.turn_left(1, 2, 5)
        self.assertEqual((x, y, drc), (1,2,4))

    def test_must_turn_to_right(self):
        x, y, drc = rv.turn_right(1, 2, 1)
        self.assertEqual((x, y, drc), (1,2,2))

    def test_must_turn_from_west_to_north(self):
        x, y, drc = rv.turn_right(1, 2, 5)
        self.assertEqual((x, y, drc), (1,2,1))

    def test_must_turn_from_north_to_west(self):
        x, y, drc = rv.turn_left(1, 2, 1)
        self.assertEqual((x, y, drc), (1,2,4))

    def test_must_move(self):
        x, y, drc = rv.move(1, 2, 3)
        self.assertEqual((x, y, drc), (1,1,3))
    
    def test_must_exec(self):
        prms = "33E"
        insts = "MMRMMRMRRM"
        res = rv.exec(prms, insts)
        self.assertEqual(res, (5, 1, 'E'))

if __name__ == '__main__':
    unittest.main()