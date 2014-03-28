#!/usr/bin/python

import math
import shapefile

def dist(x0, y0, x1, y1):
    return math.sqrt((x0-x1)**2 + (y0-y1)**2)


def compute_length(points):
    points = list(points)
    x0, y0 = points.pop(0)
    length = 0
    for x1,y1 in points:
        length += dist(x0, y0, x1, y1)
        x0, y0 = x1, y1
    return length


def compute_crow_length(points):
    assert(len(points) > 1)
    points = list(points)
    x0, y0 = points[0]
    x1, y1 = points[-1]
    assert((x0, y0) != (x1, y1))
    return dist(x0, y0, x1, y1)


for db in ('data/ne_10m_rivers_europe',
           'data/ne_10m_rivers_lake_centerlines',
           'data/ne_10m_rivers_north_america',):
    db = shapefile.Reader(db)
    for s, r in zip(db.shapes(), db.records()):
        #import ipdb; ipdb.set_trace()
        points = tuple(s.points)
        #print r
        ratio = compute_length(points) / compute_crow_length(points)
        print ratio

