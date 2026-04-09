# Coding Prep Repository

This repository contains my preparation across different types of technical interviews.

It is split into two main parts:
- LeetCode-style algorithmic practice
- OA-style / quant-style applied coding practice

---

## Repository structure

    LeetCode/
    ├── leetcodesols/
    ├── OA_Prep/
    └── README.md

---

## leetcodesols/

This folder contains all my LeetCode-style problems.

Each problem folder follows the naming convention:

    <difficulty_rating>_<leetcode_id>_<problem_name>

- difficulty_rating: based on the Zerotrac LeetCode rating
  https://zerotrac.github.io/leetcode_problem_rating/#/
- leetcode_id: the official LeetCode problem number
- problem_name: a readable version of the problem title

### Example

    1316_2348_NumberOfZeroFilledSubarrays

This means:
- difficulty ≈ 1316 (Zerotrac rating)
- LeetCode problem 2348
- problem name: Number of Zero Filled Subarrays

Problems are further grouped into folders like:

    1000_1199/
    1200_1399/
    1400_1599/

based on the difficulty rating range.

Each problem typically contains:
- notes.txt -> problem description, thoughts, examples
- solution.py -> implementation

---

## OA_Prep/

This folder contains miscellaneous practice that is not standard LeetCode.

It is focused on:
- pandas / dataframe manipulation
- linear regression and basic modeling
- data processing tasks
- quant-style approximation problems
- HackerRank / OA-style questions

Each subfolder is a self-contained exercise with:
- notes.txt -> full prompt, dataset, expected outputs
- solution.py -> starter template + automated tests

You can run each exercise with:

    python solution.py

---

## Purpose

LeetCode alone is not enough for many quant / data-focused roles.

This repo is structured to train:
- algorithmic thinking (leetcodesols)
- fast implementation on real data tasks (OA_Prep)

---



## Notes

The OA_Prep section is intentionally open-ended and will keep evolving over time as I encounter new types of problems and gaps in my preparation.
