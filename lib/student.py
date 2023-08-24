#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name):
        # Call the constructor of the parent class
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, teaching):
        # Add the provided teaching to the student's knowledge list
        self.knowledge.append(teaching)