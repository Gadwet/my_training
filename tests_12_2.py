import module_12_2 as m12
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = m12.Runner('Усейн', 10)
        self.r2 = m12.Runner('Андрей', 9)
        self.r3 = m12.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    def test_run_1(self):
        self.tournament = m12.Tournament(90, self.r1, self.r3)
        self.all_results = self.tournament.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    def test_run_2(self):
        self.tournament_2 = m12.Tournament(90, self.r2, self.r3)
        self.all_results = self.tournament_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    def test_run_3(self):
        self.tournament_3 = m12.Tournament(90, self.r1, self.r2, self.r3)
        self.all_results = self.tournament_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[3] = self.all_results

if __name__ == '__main__':
    unittest.main()