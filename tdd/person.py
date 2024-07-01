import requests


class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.data_retrieved = False

    def retrieve_all_data(self):
        response = requests.get(
            'https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/17822418#overview'
        )

        if response.ok:
            self.data_retrieved = True
            return 'Success'
        else:
            self.data_retrieved = False
            return 'Error 404'
