import subprocess
import pytest
import sys

def run_exp1(input_value):
    # Runs the student's main script as a separate process
    process = subprocess.Popen(
        [sys.executable, 'exp1_main.py'], # Student's file
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=str(input_value))
    return stdout.lower()

def test_even_odd_logic():
    # Test for Even [cite: 31]
    output = run_exp1(4)
    assert "even" in output, "Input 4 should trigger 'even' message"

    # Test for Odd [cite: 31]
    output_odd = run_exp1(7)
    assert "odd" in output_odd, "Input 7 should trigger 'odd' message"

def test_multiplication_table():
    # Test for Loop logic [cite: 32]
    output = run_exp1(5)
    # Check if '5 x 10' exists in output
    assert "5 x 10" in output or "5*10" in output, "Multiplication table incomplete"
    # Ensure loop runs 10 times
    assert output.count("=") >= 10, "Loop did not print 10 equations"