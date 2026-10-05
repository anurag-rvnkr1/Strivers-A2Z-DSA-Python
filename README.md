# 🧠 Striver's A2Z DSA — Python

> **A complete Python implementation of Striver's A2Z DSA Sheet, covering Data Structures & Algorithms from fundamentals to advanced problem-solving patterns.**

[![Language](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![DSA](https://img.shields.io/badge/Focus-Data%20Structures%20%26%20Algorithms-orange)](#-roadmap)
[![Practice](https://img.shields.io/badge/Practice-Interview%20Preparation-success)](#-purpose)
[![Problems](https://img.shields.io/badge/Problems-Progressive-blue)](#-progress)
[![License](https://img.shields.io/badge/License-Educational-lightgrey)](#-license)

---

## 📌 About

This repository contains my **Python solutions for Striver's A2Z DSA Sheet**.

The goal is to systematically learn, implement, and revise Data Structures & Algorithms while building strong problem-solving skills for:

- 💻 Software Engineering interviews
- 🧠 Data Structures & Algorithms fundamentals
- 🐍 Python problem solving
- 🧩 Pattern recognition
- 🎯 Competitive programming
- 📚 Technical interview preparation

Each problem is documented with a consistent structure:

```text
QUESTION
   ↓
APPROACH
   ↓
CODE
   ↓
TIME COMPLEXITY
   ↓
SPACE COMPLEXITY
```

The repository is designed to be useful both as a **learning journey** and as a **quick DSA revision reference**.

---

# 🎯 Purpose

The purpose of this repository is not simply to collect solutions.

The objective is to develop the ability to:

> **Understand → Identify the Pattern → Design the Approach → Implement → Analyze → Revise**

Instead of memorizing individual solutions, the focus is on recognizing the underlying algorithmic patterns that appear repeatedly across coding interviews.

---

# 🗂️ Repository Structure

The repository follows the progression of the A2Z DSA roadmap.

```text
Strivers-A2Z-DSA-Python/
│
├── 01_Arrays/
│   ├── 1_Easy/
│   ├── 2_Medium/
│   └── 3_Hard/
│
├── 02_Binary_Search/
│   ├── 1_Easy/
│   ├── 2_Medium/
│   └── 3_Hard/
│
├── 03_Sorting/
│
├── 04_Arrays_Part_II/
│
├── 05_Strings/
│
├── 06_Linked_List/
│
├── 07_Recursion/
│
├── 08_Bit_Manipulation/
│
├── 09_Stack_and_Queues/
│
├── 10_Sliding_Window_and_Two_Pointers/
│
├── 11_Heaps/
│
├── 12_Greedy/
│
├── 13_Binary_Trees/
│
├── 14_Binary_Search_Trees/
│
├── 15_Graphs/
│
├── 16_Dynamic_Programming/
│
├── 17_Tries/
│
└── README.md
```

> The directory structure will evolve as more sections of the A2Z roadmap are completed.

---

# 📚 A2Z Roadmap

## 01. Arrays

### Easy

- [ ] Largest Element in an Array
- [ ] Second Largest Element
- [ ] Check if Array Is Sorted and Rotated
- [ ] Remove Duplicates from Sorted Array
- [ ] Left Rotate Array by One
- [ ] Rotate Array by K Places
- [ ] Move Zeroes to End
- [ ] Linear Search
- [ ] Union of Two Sorted Arrays
- [ ] Missing Number
- [ ] Maximum Consecutive Ones
- [ ] Longest Subarray With Given Sum
- [ ] Find Element Present Only Once

### Medium

- [ ] Two Sum
- [ ] Sort an Array of 0s, 1s and 2s
- [ ] Majority Element
- [ ] Maximum Subarray
- [ ] Best Time to Buy and Sell Stock
- [ ] Rearrange Array Elements by Sign
- [ ] Next Permutation
- [ ] Leaders in an Array
- [ ] Longest Consecutive Sequence
- [ ] Set Matrix Zeroes
- [ ] Rotate Matrix
- [ ] Spiral Matrix

### Hard

- [ ] Count Inversions
- [ ] Reverse Pairs
- [ ] Maximum Product Subarray
- [ ] Merge Overlapping Intervals
- [ ] Merge Two Sorted Arrays Without Extra Space
- [ ] Find the Repeating and Missing Number
- [ ] Count Subarrays With Given XOR
- [ ] Maximum Subarray Sum

---

# 🧩 Problem Format

Every solution follows a consistent documentation format.

### 1. Question

The problem statement is documented at the beginning of the file.

### 2. Approach

The algorithm is explained using short, practical steps.

### 3. Code

The Python implementation follows the approach.

### 4. Complexity

Every solution includes:

```text
TIME COMPLEXITY
SPACE COMPLEXITY
```

Example:

```python
# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```

This makes every solution easy to understand and revise quickly.

---

# 🐍 Why Python?

Python is used as the primary language because it allows algorithmic ideas to be expressed clearly while maintaining concise and readable implementations.

The focus is on:

- Clean code
- Pythonic implementation
- Algorithmic clarity
- Efficient solutions
- Interview-ready patterns
- Easy revision

Where appropriate, Python's built-in data structures such as:

```text
list
set
dict
tuple
heapq
collections
```

are used to implement efficient solutions.

---

# 🧠 Core DSA Patterns

A major objective of this repository is **pattern recognition**.

Some of the important patterns covered throughout the roadmap include:

### Arrays

```text
Traversal
Two Pointers
Prefix Sum
Hashing
Kadane's Algorithm
Dutch National Flag
```

### Binary Search

```text
Classic Binary Search
Lower Bound
Upper Bound
Search in Rotated Array
Binary Search on Answer
```

### Linked Lists

```text
Fast & Slow Pointers
Reversal
Merge Techniques
Cycle Detection
Multiple Pointer Techniques
```

### Stack & Queue

```text
Monotonic Stack
Monotonic Queue
Next Greater Element
Expression Evaluation
```

### Trees

```text
DFS
BFS
Preorder
Inorder
Postorder
Level Order
Diameter
Height
Lowest Common Ancestor
```

### Graphs

```text
BFS
DFS
Dijkstra
Bellman-Ford
Floyd-Warshall
Topological Sort
Kruskal
Prim
Disjoint Set Union
```

### Dynamic Programming

```text
1D DP
2D DP
Grid DP
Knapsack
Subsequence DP
Partition DP
String DP
State Transition
Space Optimization
```

### Greedy

```text
Activity Selection
Interval Problems
Scheduling
Optimal Local Choices
```

### Bit Manipulation

```text
AND
OR
XOR
Left Shift
Right Shift
Bit Masks
Bit Counting
```

---

# 📈 Learning Methodology

The repository follows a simple learning cycle:

```text
                ┌──────────────┐
                │ Learn Topic  │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ Understand   │
                │ the Pattern  │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ Solve        │
                │ the Problem  │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ Implement    │
                │ in Python    │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ Analyze      │
                │ Complexity   │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ Revise       │
                │ the Pattern  │
                └──────┬───────┘
                       │
                       └──────────────→ Repeat
```

The long-term goal is to move from:

```text
"What is the solution?"
```

to:

```text
"What pattern does this problem use?"
```

---

# 📊 Progress

This repository is a **work in progress**.

The sheet is being completed progressively, topic by topic.

| Section | Status |
|---|---|
| Arrays — Easy | 🟡 In Progress |
| Arrays — Medium | ⬜ Not Started |
| Arrays — Hard | ⬜ Not Started |
| Binary Search | ⬜ Not Started |
| Sorting | ⬜ Not Started |
| Strings | ⬜ Not Started |
| Linked List | ⬜ Not Started |
| Recursion | ⬜ Not Started |
| Bit Manipulation | ⬜ Not Started |
| Stack & Queue | ⬜ Not Started |
| Sliding Window | ⬜ Not Started |
| Heaps | ⬜ Not Started |
| Greedy | ⬜ Not Started |
| Binary Trees | ⬜ Not Started |
| Binary Search Trees | ⬜ Not Started |
| Graphs | ⬜ Not Started |
| Dynamic Programming | ⬜ Not Started |
| Tries | ⬜ Not Started |

> Progress indicators will be updated as new problems are completed.

---

# 🔎 LeetCode Connection

Many problems in the A2Z roadmap correspond directly to problems available on **LeetCode**.

Where applicable, the implementations follow the expected LeetCode function style.

For example:

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ...
```

The repository may also contain standalone implementations for problems originating from other DSA platforms.

The goal is to maintain **algorithmically correct, interview-ready Python solutions** rather than simply reproducing platform-specific boilerplate.

---

# 🧪 Testing Philosophy

Solutions are designed with common edge cases in mind.

Testing considerations include:

- Empty arrays where allowed
- Single-element arrays
- Duplicate values
- Negative values
- Zero values
- Already sorted input
- Reverse-sorted input
- Large input sizes
- Boundary conditions
- Minimum and maximum constraints

The objective is to understand not only the normal case, but also the situations where an implementation can fail.

---

# ⚡ Complexity Analysis

Every solution includes time and space complexity.

For example:

```text
TIME COMPLEXITY = O(N)
SPACE COMPLEXITY = O(1)
```

Complexity analysis is treated as an essential part of every solution because an algorithm is not considered complete until its efficiency is understood.

---

# 🛠️ Running the Solutions

Clone the repository:

```bash
git clone https://github.com/anurag-rvnkr1/Strivers-A2Z-DSA-Python.git
```

Move into the repository:

```bash
cd Strivers-A2Z-DSA-Python
```

Run any Python solution:

```bash
python 01_Arrays/1_Easy/01.Largest_element_in_array.py
```

For Python 3:

```bash
python3 01_Arrays/1_Easy/01.Largest_element_in_array.py
```

---

# 📖 Recommended Study Order

The repository follows a progressive learning order:

```text
Arrays
   ↓
Sorting
   ↓
Binary Search
   ↓
Strings
   ↓
Linked Lists
   ↓
Recursion
   ↓
Bit Manipulation
   ↓
Stack & Queue
   ↓
Sliding Window & Two Pointers
   ↓
Heaps
   ↓
Greedy
   ↓
Binary Trees
   ↓
Binary Search Trees
   ↓
Graphs
   ↓
Dynamic Programming
   ↓
Tries
```

The recommended approach is to avoid jumping randomly between advanced topics.

Build the fundamentals first, then progressively move toward more complex patterns.

---

# 🎯 Interview Preparation

This repository is intended to support preparation for technical interviews by developing proficiency in:

### Problem Solving

- Breaking problems into smaller components
- Identifying constraints
- Selecting appropriate data structures
- Recognizing algorithmic patterns

### Optimization

- Improving brute-force solutions
- Reducing unnecessary operations
- Understanding time-space tradeoffs
- Choosing optimal approaches

### Implementation

- Writing clean Python
- Handling edge cases
- Producing readable code
- Understanding platform-specific function signatures

### Communication

For each problem, the intended thought process is:

```text
Problem
   ↓
Observation
   ↓
Pattern
   ↓
Approach
   ↓
Implementation
   ↓
Complexity
```

---

# 🔄 Revision Strategy

For effective revision, problems should be reviewed by **pattern**, not only by problem number.

For example:

### Need Two Pointer practice?

Review:

```text
Arrays
Linked Lists
Strings
Sliding Window
```

### Need Hashing practice?

Review:

```text
Arrays
Strings
Subarrays
Frequency Problems
```

### Need Binary Search practice?

Review:

```text
Classic Search
Rotated Arrays
Bounds
Search Space
Binary Search on Answer
```

### Need Dynamic Programming practice?

Review:

```text
1D DP
2D DP
Subsequences
Knapsack
Grid DP
Partition DP
```

This helps convert individual problems into reusable problem-solving patterns.

---

# 📌 Repository Philosophy

The repository follows three principles:

```text
Consistency > Intensity

Understanding > Memorization

Patterns > Individual Problems
```

The goal is not to solve hundreds of problems once.

The goal is to solve problems well enough that the underlying patterns become familiar.

---

# 📚 Reference

This repository follows the structure and progression of:

**Striver's A2Z DSA Sheet**

Reference repository:

https://github.com/Codensity30/Strivers-A2Z-DSA-Sheet

The implementations in this repository are independently written in Python for learning and practice.

---

# 🔗 Useful Resources

### Striver's A2Z DSA Sheet

https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z

### LeetCode

https://leetcode.com/

### Python

https://www.python.org/

### My GitHub

https://github.com/anurag-rvnkr1

---

# 👨‍💻 Author

**Anurag**

Cybersecurity & Software Engineering Learner

GitHub:

https://github.com/anurag-rvnkr1

---

# ⭐ Support

If this repository helps you with your own DSA preparation, consider giving it a ⭐.

You can also use the repository as a revision guide for:

- Data Structures
- Algorithms
- Python
- Competitive Programming
- Coding Interviews
- Technical Interviews

---

# 📜 Disclaimer

This repository is maintained for **educational and interview-preparation purposes**.

The original problem statements and A2Z roadmap belong to their respective authors and platforms.

This repository contains Python implementations created for learning, practice, revision, and portfolio purposes.

---

<div align="center">

### 🧠 Learn the Pattern.  
### 💻 Solve the Problem.  
### 🚀 Build the Skill.

**Striver's A2Z DSA — Python**

</div>
