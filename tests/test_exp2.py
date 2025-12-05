import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../exp02')))
from exp1.main import contact_book  # Assumes student defines this dictionary

def test_dictionary_structure():
    # Check if it's actually a dictionary
    assert isinstance(contact_book, dict), "contact_book must be a dictionary"

def test_contacts_exist():
    # Check for required names from problem statement
    assert "Alice" in contact_book, "Alice is missing from contact_book"
    assert contact_book["Alice"] == "555-1234", "Alice's number is incorrect"

def test_emergency_list():
    from exp1.main import emergency_list
    assert "Alice" in emergency_list, "Alice missing from emergency_list"