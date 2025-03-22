# Sophia Mai
# CIS256 Spring 2025
# EX 4 - test
#from guess_word_gameV2 import wordlist
import unittest
import logging
logger = logging.getLogger("test")
logging.basicConfig(format="%(asctime)s-%(msg)s", level = logging.DEBUG)

class TestBasics(unittest.TestCase):
    def test_equality(self):
        self.assertEqual("horse", "horse")

    def test_inlist(self):
        self.assertIn("horse",  ['bread', 'cheese', 'beef', 'chicken'])
        # self.assertIsInstance()

    def test_isofclass(self):
        self.assertIsInstance("horse", str)


    def test_logasserts(self):
        with self.assertLogs("test", level="INFO") as lm:
            logger.info("CUSTOM MESSAGE")
            # print(lm.records) - LIFO
            self.assertEqual(lm.records[0].getMessage(), "CUSTOM MESSAGE")


if __name__ == "__main__" :
    unittest.main()