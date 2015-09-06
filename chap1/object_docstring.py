__author__ = 'v-wjia'
# coding=utf8

import math

class Point:
    'Represents a point in two-dimensional geomatric coodinates'

    def __int__(self, x=0, y=0):
        '''initialize the position of a new point. The x and y coodinates can be specified.
        if they are not, the point defaults to the origin.'''

        self.move(x, y)

    def move(self, x, y):
        "asdfasdfasdfasdfasd."
        self.x = x
        self.y = y

    def reset(self):
        'asdfasdfaf'
        self.x = 0
        self.y = 0

    def calculate_distance(self, other_point):
        """我们是害虫！！"""
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2
        )