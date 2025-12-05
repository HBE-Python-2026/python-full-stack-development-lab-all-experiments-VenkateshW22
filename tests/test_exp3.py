import pytest
# Assumes student file is named 'exp3_main.py'
from exp3_main import safe_divide

def test_safe_divide_success():
    # Test normal division [cite: 177]
    assert safe_divide(10, 2) == 5.0

def test_zero_division():
    # Test ZeroDivisionError handling [cite: 164]
    # Function should print error and return None
    assert safe_divide(10, 0) is None

def test_type_error():
    # Test TypeError handling [cite: 171]
    assert safe_divide("ten", 2) is None