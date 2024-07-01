"""
class Person    __init__
        name: str
        lastname: str
        data_retrieved: bool (starts as False)

    API:
        retrieve_all_data -> method
            OK
            404

        (data_retrieved becomes True if retrieve_all_data is successfull)
"""
try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '..\\tdd'
            )
        )
    )
except:
    raise

import unittest
from unittest.mock import patch
from person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('Vinicius', 'Justen')
        self.p2 = Person('Bruna', 'Santos')

    def test_person_attr_name_has_a_valid_value(self):
        self.assertEqual(self.p1.name, 'Vinicius')
        self.assertEqual(self.p2.name, 'Bruna')

    def test_person_attr_name_is_instance_str(self):
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p2.name, str)

    def test_person_attr_lastname_has_a_valid_value(self):
        self.assertEqual(self.p1.lastname, 'Justen')
        self.assertEqual(self.p2.lastname, 'Santos')

    def test_person_attr_lastname_is_instance_str(self):
        self.assertIsInstance(self.p1.lastname, str)
        self.assertIsInstance(self.p2.lastname, str)

    def test_person_attr_data_retrieved_starts_as_false(self):
        self.assertFalse(self.p1.data_retrieved)
        self.assertFalse(self.p2.data_retrieved)

    def test_person_retrieve_all_data_success(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.retrieve_all_data(), 'Success')
            self.assertTrue(self.p1.data_retrieved)
            self.assertEqual(self.p2.retrieve_all_data(), 'Success')
            self.assertTrue(self.p2.data_retrieved)

    def test_person_retrieve_all_data_fail(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.retrieve_all_data(), 'Error 404')
            self.assertFalse(self.p1.data_retrieved)
            self.assertEqual(self.p2.retrieve_all_data(), 'Error 404')
            self.assertFalse(self.p2.data_retrieved)

    def test_person_retrieve_all_data_success_sequential_fail(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.retrieve_all_data(), 'Success')
            self.assertTrue(self.p1.data_retrieved)
            self.assertEqual(self.p2.retrieve_all_data(), 'Success')
            self.assertTrue(self.p2.data_retrieved)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.retrieve_all_data(), 'Error 404')
            self.assertFalse(self.p1.data_retrieved)
            self.assertEqual(self.p2.retrieve_all_data(), 'Error 404')
            self.assertFalse(self.p2.data_retrieved)


if __name__ == '__main__':
    unittest.main(verbosity=2)
