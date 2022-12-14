#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    ax = float(input('Введите координаты первой вершины:\n'))
    ay = float(input())
    bx = float(input('Введите координаты второй вершины:\n'))
    by = float(input())
    cx = float(input('Введите координаты третьей вершины:\n'))
    cy = float(input())
    xx = float(input('Введите координаты точки:\n'))
    xy = float(input())

    # Если точка лежит внутри треугольника, то сумма
    # площадей образованных ею треугольников равна
    # площади данного треугольника.
    s = abs((ax - cx)*(by - cy) - (bx - cx)*(ay - cy))
    s1 = abs((ax - xx)*(by - xy) - (bx - xx)*(ay - xy))
    s2 = abs((ax - cx)*(xy - cy) - (xx - cx)*(ay - cy))
    s3 = abs((xx - cx)*(by - cy) - (bx - cx)*(xy - cy))
    if (s1 + s2 + s3) == s:
        print('Точка ВХОДИТ в треугольник')
    else:
        print('Точка НЕ ВХОДИТ в треугольник')
