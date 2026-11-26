
import pytest
from event import calculate_fee

def test_student_fee():
    assert calculate_fee("student", 2) == 200

def test_faculty_fee():
    assert calculate_fee("faculty", 3) == 600

def test_industry_fee():
    assert calculate_fee("industry", 2) == 1000

def test_single_student():
    assert calculate_fee("student", 1) == 100

def test_invalid_category():
    with pytest.raises(ValueError):
        calculate_fee("teacher", 2)
