#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

vis = Visitor("Phil")
vis2 = Visitor('Luca')
yosemite = NationalPark("Yosemite")
rocky_mountain = NationalPark("Rocky Mountain")
Trip(vis, yosemite, "May 5th", "May 9th")
Trip(vis, yosemite, "May 20th", "May 27th")
Trip(vis, yosemite, "January 5th", "January 20th")
Trip(vis, rocky_mountain, "January 5th", "January 20th")
Trip(vis2, yosemite, "January 5th", "January 20th")


if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    ipdb.set_trace()
