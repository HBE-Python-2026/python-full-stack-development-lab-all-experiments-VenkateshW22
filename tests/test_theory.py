import os

def test_theory_file_exists():
    assert os.path.exists("THEORY.md"), "THEORY.md file is missing!"

def test_theory_is_filled():
    with open("THEORY.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Check if they removed the placeholder text
    # Or check if the file length is sufficient (e.g., > 500 characters)
    assert "[Type your answer here]" not in content, "You left '[Type your answer here]' placeholders in THEORY.md"
    assert len(content) > 1000, "Your answers in THEORY.md seem too short. Please elaborate."