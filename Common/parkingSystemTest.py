import unittest

from Common.parkingSystem import ParkingSystem


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = ParkingSystem(1, 1, 0)
        self.assertEqual(s.addCar(1), True)
        self.assertEqual(s.addCar(2), True)
        self.assertEqual(s.addCar(3), False)
        self.assertEqual(s.addCar(1), False)


if __name__ == "__main__":
    unittest.main()
