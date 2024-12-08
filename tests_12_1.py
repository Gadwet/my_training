import unittest
import module_12_1

class RunnerTest(unittest.TestCase):
    #is_frozen = False

    #@unittest.skipIf(is_frozen, None)
    def test_walk(self):
        walks = module_12_1.Runner('Денис')
        for i in range(10):
            walks.walk()
        self.assertEqual(walks.distance, 50)

    #@unittest.skipIf(is_frozen, None)
    def test_run(self):
        runs = module_12_1.Runner('Николай')
        for i in range(10):
            runs.run()
        self.assertEqual(runs.distance, 100)

    #@unittest.skipIf(is_frozen, None)
    def test_challenge(self):
        runs = module_12_1.Runner('Евгений')
        walks = module_12_1.Runner('Алексей')
        for i in range(10):
            runs.run()
            walks.walk()
        self.assertNotEqual(runs.distance, walks.distance)

if __name__ == '__main__':
    unittest.main()
