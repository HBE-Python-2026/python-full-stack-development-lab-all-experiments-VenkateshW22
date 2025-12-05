import os
import sys

# Path setup to run student script
EXP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../exp05'))

def test_file_creation():
    # 1. Create a dummy input.txt in the student folder
    with open(f'{EXP_DIR}/input.txt', 'w') as f:
        f.write("hello world hello")

    # 2. Run student script
    os.chdir(EXP_DIR)
    os.system(f'{sys.executable} main.py')

    # 3. Check if output.txt was created and has correct dict string
    assert os.path.exists('output.txt'), "output.txt was not created"

    with open('output.txt', 'r') as f:
        content = f.read()

    assert "'hello': 2" in content, "Word count logic is incorrect"