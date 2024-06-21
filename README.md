# SDEV 120 Summer Study Group

Welcome to the Software Development Study Group Repository! This repository is dedicated to our collaborative learning journey as we tackle coding exercises, debug challenges, and LeetCode problems together. Here, you'll find a collection of resources and solutions designed to support our learning and growth.

## Repository Contents

1. **Coding Exercises**:
   - Solutions to our class's coding exercises.
   - Contributions from members with their unique approaches.

2. **Debug Challenges**:
   - Solutions to debugging tasks.
   - Tips and tricks for efficient debugging.

3. **LeetCode Challenges**:
   - Solutions to various LeetCode problems.
   - Strategies and explanations for different problem-solving techniques.

# Online Resources for Learning and Development

## Programming Tutorials and Platforms:
- [W3Schools](https://www.w3schools.com) - Web tutorials and references.
- [TutorialsPoint](https://www.tutorialspoint.com) - Comprehensive tutorials on various programming languages and technologies.
- [FreeCodeCamp](https://www.freecodecamp.org) - Free coding lessons and interactive learning experiences.
- [Real Python](https://realpython.com/) - Python tutorials and articles for all skill levels.
- [LeetCode](https://leetcode.com) - Practice coding challenges and prepare for technical interviews.

## Integrated Development Environments (IDEs):
- [Thonny Editor Download](https://thonny.org/) - Beginner-friendly Python IDE.
- [Unofficial Thonny Documentation](https://python.quectel.com/doc/Application_guide/en/dev-tools/Thonny/index.html) - Additional resources for Thonny.
- [VS Code Editor Download](https://visualstudio.microsoft.com/downloads/) - Visual Studio Code, a versatile code editor.
- [VS Code Documentation](https://code.visualstudio.com/docs) - Official documentation for VS Code.
- [PyCharm Editor Download](https://www.jetbrains.com/pycharm/download/) - IDE for Python development.
- [PyCharm Documentation](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) - Official documentation for PyCharm.

## Python Resources:
- [Python 3.12.4 Download](https://www.python.org/downloads/) - Download Python 3.12.4.
- [Official Python 3.12.4 Documentation](https://docs.python.org/3.12/) - Documentation for Python 3.12.4.

## Version Control and Collaboration:
- [The Git Repository Tool](https://www.git-scm.com/) - Download Git for version control.
- [Git Documentation](https://www.git-scm.com/book/en/v2) - Comprehensive documentation for Git.
- [GitHub Documentation](https://docs.github.com/en) - Documentation for GitHub

## Community and Communication:
- [Discord Server @ Summer-SDEV120-IvyTech-server](https://discord.com/) - Link to the Discord server for our study group.
- [Python Reddit](https://www.reddit.com/r/Python/) - Subreddit for Python discussions, news, and questions.
- [StackOverflow](https://stackoverflow.com/) - Q&A community for programming questions.

## Collaboration and Contribution

This repository serves as a central hub for our study group. Members are encouraged to:

- **Upload their own solutions**: Share your code for exercises and challenges to receive feedback and help others learn from your approach.
- **Seek assistance**: If you're stuck on a problem, upload your code, and we can work through the issues together.
- **Review and collaborate**: Provide constructive feedback on your peers' submissions, suggest improvements, and discuss alternative solutions.

## Weekly Meetings

Our study group meets weekly via Google Meet to discuss our progress, address any challenges, and share insights. This repository will serve as a supplement to our meetings, ensuring continuous support and collaboration throughout the week.

## Getting Started
# Getting Started with Our GitHub Repository

### Step 1: Install Git on Your Machine

To start using Git and GitHub, you need to have Git installed on your machine. Follow the instructions below for your operating system:

- **Windows:**
  1. Download Git for Windows from the official site: [Git for Windows](https://git-scm.com/download/win).
  2. Run the installer and follow the setup instructions.
  3. Confirm the installation by opening Command Prompt and typing into command prompt:
     ```
     git --version
     ```

- **macOS:**
  1. Open the Terminal.
  2. Install Git using Homebrew (if you don't have Homebrew installed, follow the instructions at [brew.sh](https://brew.sh)):
     ```
     brew install git
     ```
  3. Confirm the installation by typing in the Terminal:
     ```
     git --version
     ```

- **Linux:**
  1. Open your Terminal.
  2. Install Git using the package manager for your distribution. For example, on Ubuntu:
     ```
     sudo apt update
     sudo apt install git
     ```
  3. Confirm the installation by typing in the Terminal:
     ```
     git --version
     ```

### Step 2: Clone the Repository

Once Git is installed, clone the repository to your local machine:

1. Open your terminal (Command Prompt, Git Bash, or Terminal).
2. Run the following command:

```
git clone https://github.com/Cedric-Lard/studygroup.git
```

### Step 3: Navigate to Relevant Folders

Explore the repository’s folders to find:

- **CodingExercises:** Solutions to class exercises.
- **DebuggingChallenges:** Solutions and discussions on debugging.
- **LeetCodeProblems:** Solutions to LeetCode challenges.
- **Resources:** Useful links to tutorials, documentation, and tools.

### Step 4: Contribute and Collaborate

- **Upload Your Solutions:** If you have solutions to share, upload your files to the respective folders.
- **Discuss Issues:** Use GitHub Issues to ask questions or discuss problems encountered.
- **Review and Comment:** Review others’ solutions and provide constructive feedback.

### Step 5: Add, Commit, Push, and Pull

- ## Git Add
To stage changes for a commit in Git, you use `git add -A` command. This will add all the files you modified to Git
```
git add -A
```
- ## Git Commit
Next commit the changes in Git using the `git commit -m "<Your commit message>" command
Replace "<Your commit message>" with a brief description of what files you have added.
```
git commit -m "Added files to debugging_exercises"
```
- ## Git Push
Finally, type the command: 
```
git push origin
```
- ## Git Pull
If you want an update to date version of what everyone has type: 
```
git pull origin
```
And then watch your folders update with everything everyone pushed to github.
This will add everything to this repo for everyone to see.

### Step 6: Stay Engaged

- **Weekly Meetings:** Participate in our weekly Google Meet sessions to discuss challenges and solutions.
- **Use Discord:** Join our Discord server for real-time discussions and updates.

### Step 7: Learn and Grow

Take advantage of the curated resources in the **Resources** folder for additional learning.


## Need Help?

If you have any questions or need assistance with the repository, feel free to reach out to Cedric via cedriclard76@gmail.com or other members via Discord or GitHub Issues.

## Repository Structure

The repository is organized into the following main directories:

### Coding_Exercises

Contains all coding exercises from our class.

- **Completed**: Post your solutions and let's talk about it. It is important to realize that everyone thinks a bit differently and there is technically no "right" answer to coding patterns, conventions, or algorithm usage. Some things work better than others. If you develope a solution that works on your own please share it. It can help you grow to discuss what you did and how you thought of the problem and give us more perspectives.
  - `member_name/`: Subfolder for each member to keep their solutions organized.
    - `exercise_name/`: Specific exercise folder containing the solution files.
      - `solution.py`: The solution file.
      - `notes.md`: Notes and explanations.

- **To_Review**: Exercises that need review and feedback.
  - `member_name/`: Subfolder for each member.
    - `exercise_name/`: Specific exercise folder containing the files needing review.
      - `attempt.py`: The initial attempt at solving the exercise.
      - `notes.md`: Notes and explanations.

### Debug_Challenges

Contains debugging challenges from our class.

- **Completed**: Solutions that have been finalized.
  - `member_name/`: Subfolder for each member to keep their solutions organized.
    - `challenge_name/`: Specific challenge folder containing the solution files.
      - `fixed_bug.py`: The fixed bug solution file.
      - `explanation.md`: Explanation of the bug and the fix.

- **Need_Help**: Challenges that need assistance.
  - `member_name/`: Subfolder for each member.
    - `challenge_name/`: Specific challenge folder containing the problematic files.
      - `bug_code.py`: The code with the bug.
      - `error_log.txt`: Error log or description of the issue.

### LeetCode_Challenges

Contains LeetCode problems.

- **Completed**: Solutions that have been finalized.
  - `member_name/`: Subfolder for each member to keep their solutions organized.
    - `problem_name/`: Specific problem folder containing the solution files.
      - `solution.py`: The solution file.
      - `explanation.md`: Explanation of the solution.

- **To_Review**: Problems that need review and feedback.
  - `member_name/`: Subfolder for each member.
    - `problem_name/`: Specific problem folder containing the files needing review.
      - `attempt.py`: The initial attempt at solving the problem.
      - `questions.md`: Questions or issues faced.

### Resources

Contains markdown files with links and descriptions of useful online resources.

- `W3Schools.md`: Links and descriptions for W3Schools resources.
- `TutorialsPoint.md`: Links and descriptions for TutorialsPoint resources.
- `FreeCodeCamp.md`: Links and descriptions for FreeCodeCamp resources.
- `LeetCode.md`: Links and descriptions for LeetCode resources.

## Example Structure

Here's an example of how the structure would look with some populated data:

```plaintext
study-group-repo/
├── README.md
├── Coding_Exercises/
│   ├── Completed/
│   │   └── Alice/
│   │       └── Exercise1/
│   │           ├── solution.py
│   │           └── notes.md
│   └── To_Review/
│       └── Bob/
│           └── Exercise1/
│               ├── attempt.py
│               └── notes.md
├── Debug_Challenges/
│   ├── Completed/
│   │   └── Carol/
│   │       └── Challenge1/
│   │           ├── fixed_bug.py
│   │           └── explanation.md
│   └── Need_Help/
│       └── Dave/
│           └── Challenge1/
│               ├── bug_code.py
│               └── error_log.txt
├── LeetCode_Challenges/
│   ├── Completed/
│   │   └── Alice/
│   │       └── TwoSum/
│   │           ├── solution.py
│   │           └── explanation.md
│   └── To_Review/
│       └── Bob/
│           └── TwoSum/
│               ├── attempt.py
│               └── questions.md
├── Resources/
│   ├── W3Schools.md
│   ├── TutorialsPoint.md
│   ├── FreeCodeCamp.md
│   └── LeetCode.md
└── .gitignore
