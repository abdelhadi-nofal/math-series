
from math_series.series import fibonacci,lucas,sum_series


def test_fibonacci_4():
    assert fibonacci(4) == 3
    

def test_fibonacci_8():
    assert fibonacci(8) == 21


def test_lucas_4():
    assert lucas(4) == 7
    

def test_lucas_7():
    assert lucas(7) == 29

def test_sum_series_4_01():
    assert sum_series(4) == 3

def test_sum_series_8():
    assert sum_series(8) == 21


def test_sum_series_4_21():
    assert sum_series(4,2,1) == 7    

def test_sum_series_7():
    assert sum_series(7,2,1) == 29   


def test_sum_series_2():
    assert sum_series(4,3,7) == 27



