import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return f'{self.name} (Distance: {self.distance})'

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', speed=10)
        self.runner2 = Runner('Андрей', speed=9)
        self.runner3 = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f'{key}:')
            for place, runner in result.items():
                print(f'  {place}: {runner.name}')

    def test_usain_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.__class__.all_results['usain_and_nik'] = results
        self.assertTrue(list(results.values())[-1].name == 'Ник')

    def test_andrey_and_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.__class__.all_results['andrey_and_nik'] = results
        self.assertTrue(list(results.values())[-1].name == 'Ник')

    def test_usain_and_andrey_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.__class__.all_results['usain_and_andrey_and_nik'] = results
        self.assertTrue(list(results.values())[-1].name == 'Ник')


if __name__ == '__main__':
    unittest.main()
