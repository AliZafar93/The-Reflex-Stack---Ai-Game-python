import time
import unittest
from src.utils.timer import Timer

class TestTimer(unittest.TestCase):
    def test_timer_initialization(self):
        timer = Timer()
        self.assertEqual(timer.start_time, None)
        self.assertEqual(timer.end_time, None)

    def test_start_timer(self):
        timer = Timer()
        timer.start()
        self.assertIsNotNone(timer.start_time)

    def test_stop_timer(self):
        timer = Timer()
        timer.start()
        time.sleep(1)  # Sleep for a second to simulate time passing
        timer.stop()
        self.assertIsNotNone(timer.end_time)
        self.assertGreater(timer.end_time, timer.start_time)

    def test_elapsed_time(self):
        timer = Timer()
        timer.start()
        time.sleep(1)  # Sleep for a second
        timer.stop()
        elapsed = timer.elapsed_time()
        self.assertAlmostEqual(elapsed, 1, delta=0.1)  # Allow a small delta for timing inaccuracies

    def test_reset_timer(self):
        timer = Timer()
        timer.start()
        timer.stop()
        timer.reset()
        self.assertEqual(timer.start_time, None)
        self.assertEqual(timer.end_time, None)

if __name__ == '__main__':
    unittest.main()