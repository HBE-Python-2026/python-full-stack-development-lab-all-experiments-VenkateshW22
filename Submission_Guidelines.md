Here is the updated `SUBMISSION.md` file with the **Theory Questions** section included.

````markdown
# 📘 Student Submission Guidelines

Welcome to the **Python Full Stack Development Lab**. This repository contains all 10 experiments for the semester. 

**Read these guidelines carefully.** The grading system is **automated**. If you misplace a file or name it incorrectly, the autograder will not find your code, and you will receive a **0**.

---

## 📂 Required Directory Structure

**DO NOT** rename or delete the experiment folders (`exp01`, `exp02`, etc.).
**DO NOT** touch the `tests/` folder or `.github/` folder.

Your repository must look exactly like this:

```text
Your-Repo-Name/
├── exp01/
│   └── main.py              <-- Exp 1: Basics & Loops
├── exp02/
│   └── main.py              <-- Exp 2: Data Structures
├── exp03/
│   └── main.py              <-- Exp 3: Functions & Exceptions
├── exp04/
│   └── main.py              <-- Exp 4: OOP (Vehicle/Car)
├── exp05/
│   ├── analyzer.py          <-- Exp 5: Module
│   ├── main.py              <-- Exp 5: Script
│   └── input.txt            <-- Exp 5: Data file
├── exp06/
│   └── main.py              <-- Exp 6: MySQL Database
├── exp07/
│   ├── app.py               <-- Exp 7: Flask Basic
│   └── templates/
│       └── profile.html     <-- Exp 7: HTML Template
├── exp08/
│   ├── app.py               <-- Exp 8: Flask Database
│   └── templates/
│       └── index.html       <-- Exp 8: HTML Template
├── exp09/
│   ├── manage.py            <-- Exp 9: Django Project Root
│   ├── myproject/           <-- Exp 9: Project Settings
│   └── blog/                <-- Exp 9: App Folder
├── exp10/
│   └── app.py               <-- Exp 10: REST API
├── requirements.txt         <-- DO NOT DELETE
├── THEORY.md                <-- Theory Questions
└── README.md
````

-----

## 🚀 How to Submit

1.  **Clone the Repo:** Download the code to your local machine.
2.  **Navigate to the Folder:** Open the specific folder for the week (e.g., `cd exp01`).
3.  **Write Code:** Complete the assignment in the specific file listed above.
4.  **Test Locally:** Run your code to ensure it works as expected.
    ```bash
    # Example for Exp 1
    python exp01/app.py
    ```
5.  **Commit & Push:**
    ```bash
    git add .
    git commit -m "Completed Experiment 1"
    git push origin main
    ```
6.  **Check Your Grade:** Go to the "Actions" tab in your GitHub repository to see if the autograder passed. Green checkmark = Pass.

-----

## ⚠️ Crucial Coding Rules

### 1\. The `if __name__ == "__main__":` Block

For script-based labs (Exp 1, 2, 5, 6), you **must** wrap your execution logic in this block. If you don't, the autograder will freeze when it tries to import your code.

**WRONG:**

```python
name = input("Enter Name: ") # Autograder freezes here!
print(f"Hello {name}")
```

**CORRECT:**

```python
def main():
    name = input("Enter Name: ")
    print(f"Hello {name}")

if __name__ == "__main__":
    main()
```

### 2\. Variable Naming

For data structure labs (Exp 2), use the **exact** variable names requested in the problem statement.

* **Exp 2:** Dictionary must be named `contact_book`. List must be named `emergency_list`.
* **Exp 4:** Class names must be `Vehicle` and `Car`.


### 3\. Modifying Protected Files

Modifying the contents of **Any File** or **Creating new files unless asked for** will invalidate the marks gained on a particular assignment.

* Modifying any of the test files unless asked for will invalidate the marks gained on a particular assignment.


-----

## 📝 Theory Questions

For every experiment, you must answer the theory questions provided in the repository.

1.  Open `THEORY.md`.
2.  Type your answers **directly into the file** under each question.
3.  **Do not change the question text.**
4.  **Note:** If you leave the placeholder text `[Type your answer here]` in the file, the autograder will mark it as incomplete.

-----

## 📝 Experiment-Specific Notes

### **Exp 1: Python Basics**

* **File:** `exp01/main.py`
* **Input:** The program must accept exactly one integer input when prompted.
* **Output:** Ensure the multiplication table prints 10 lines (1 to 10).

### **Exp 3: Functions**

* **File:** `exp03/main.py`
* **Requirement:** You must define the function `safe_divide(numerator, denominator)`.
* **Returns:** Return `None` if an error occurs (ZeroDivision or TypeError).

### **Exp 5: File I/O**

* **Files:** `exp05/main.py`, `exp05/analyzer.py`, `exp05/input.txt`.
* **Note:** Your code must create `output.txt` when it runs. Do not upload `output.txt`; let your code generate it.

### **Exp 6: MySQL**

* **File:** `exp06/main.py`
* **Grading:** The autograder uses a "Mock" database. It checks if your SQL queries are written correctly (e.g., `INSERT INTO employees...`). It does not connect to a real live database on GitHub.

### **Exp 7 & 8: Flask**

* **Files:** `app.py` inside the respective folders.
* **Templates:** You **must** create a folder named `templates` inside `exp07` and `exp08` for your HTML files (`profile.html`, `index.html`).

### **Exp 9: Django**

* **Structure:** This is a full Django project. Ensure `manage.py` is inside `exp09/`.
* **Model:** Ensure your `Post` model has `title` and `content` fields.

-----

## ❓ Troubleshooting

**My code runs on my laptop but fails on GitHub.**

1.  Did you hardcode a file path? (e.g., `C:/Users/Name/Desktop/file.txt`). Use relative paths (`input.txt`).
2.  Did you wrap your main code in `if __name__ == "__main__":`?
3.  Did you rename the main file? (It must be `main.py` or `app.py` as listed above).
4.  Check the **Actions** tab logs. Click on the red "X", then "Autograding", and read the error message (e.g., `AssertionError: Expected 'even', found 'odd'`).

**Good Luck \!**

```