"""
TDD - Test driven development

RED
Part 1 - Creat a test and get it to FAIL

GREEN
Part 2 - Create the code and get the test to PASS

REFACTOR
Parte 3 - Improve my code
"""

import unittest
from baconandeggs import bacon_and_eggs


class TestBaconAndEggs(unittest.TestCase):
    def test_bacon_and_eggs_must_raise_assertion_error_if_n_is_not_int(self):
        with self.assertRaises(AssertionError):
            bacon_and_eggs(1.2)

    def test_bacon_and_eggs_must_return_bacon_and_eggs_for_multiples_of_3_and_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'bacon and eggs'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_and_eggs(entrada),
                                 saida,
                                 msg=f'"{entrada}" did not return "{saida}".'
                                 )

    def test_bacon_and_eggs_must_return_you_starved_for_non_multiples_of_3_and_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'you starved'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_and_eggs(entrada),
                                 saida,
                                 msg=f'"{entrada}" did not return "{saida}".'
                                 )

    def test_bacon_and_eggs_must_return_bacon_for_multiples_of_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = 'bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_and_eggs(entrada),
                                 saida,
                                 msg=f'"{entrada}" did not return "{saida}".'
                                 )

    def test_bacon_and_eggs_must_return_eggs_for_multiples_of_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida = 'eggs'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_and_eggs(entrada),
                                 saida,
                                 msg=f'"{entrada}" did not return "{saida}".'
                                 )


unittest.main(verbosity=2)
