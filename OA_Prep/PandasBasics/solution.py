"""
BASIC PANDAS BOOTCAMP - STARTER TEMPLATE

Instructions:
- Fill in the TODO sections.
- Keep the function names unchanged.
- Run this file directly to execute the automated tests.

Command:
    python solution.py
"""

import pandas as pd


def build_base_dataframe() -> pd.DataFrame:
    """Return the base dataset for the exercise."""
    return pd.DataFrame(
        {
            "day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "NYC": [70, 72, 68, 75, 78, 80, 77, 74, 73, 76],
            "Town_1": [69, 71, 67, 74, 77, 79, 76, 73, 72, 75],
            "Town_2": [65, 67, 66, 70, 74, 82, 79, 71, 70, 72],
            "Town_3": [88, 91, 95, 89, 92, 97, 93, 87, 90, 94],
            "Town_4": [60, 62, 61, 66, 70, 73, 71, 68, 67, 69],
            "Rainfall": [0.0, 0.2, 0.0, 0.5, 0.1, 0.0, 0.3, 0.4, 0.0, 0.2],
            "Condition": [
                "sunny",
                "cloudy",
                "sunny",
                "rain",
                "cloudy",
                "sunny",
                "rain",
                "rain",
                "sunny",
                "cloudy",
            ],
        }
    )


def question_1(df: pd.DataFrame) -> tuple[int, int]:
    """
    Q1. Return the shape of the dataframe.

    Example return:
        (10, 8)
    """
    # TODO: your code goes here
    raise NotImplementedError


def question_2(df: pd.DataFrame) -> float:
    """
    Q2. Return the mean of the NYC column.

    Example return:
        74.3
    """
    # TODO: your code goes here
    raise NotImplementedError


def question_3(df: pd.DataFrame) -> int:
    """
    Q3. Return the day number on which NYC had its maximum temperature.

    Example return:
        6
    """
    # TODO: your code goes here
    raise NotImplementedError


def question_4(df: pd.DataFrame) -> int:
    """
    Q4. Return how many days Town_2 had temperature at least 75.

    Example return:
        2
    """
    # TODO: your code goes here
    raise NotImplementedError


def question_5(df: pd.DataFrame) -> float:
    """
    Q5. Return the median NYC temperature on rows where Town_3 is in [90, 95].

    Example return:
        74.5
    """
    # TODO: your code goes here
    raise NotImplementedError


def question_6(df: pd.DataFrame) -> tuple[int, int]:
    """
    Q6. Create a new column called spread:
        spread = max(Town_1, Town_2, Town_3, Town_4) - min(Town_1, Town_2, Town_3, Town_4)

    Return:
        (day_with_largest_spread, largest_spread_value)

    Example return:
        (3, 34)
    """
    town_cols = ["Town_1", "Town_2", "Town_3", "Town_4"]

    # TODO: your code goes here
    raise NotImplementedError


def question_7(df: pd.DataFrame) -> str:
    """
    Q7. Among Town_1 through Town_4, return the town with the largest sample std.

    Example return:
        "Town_2"
    """
    town_cols = ["Town_1", "Town_2", "Town_3", "Town_4"]

    # TODO: your code goes here
    raise NotImplementedError


def question_8(df: pd.DataFrame) -> float:
    """
    Q8. Return the Pearson correlation between NYC and Town_1.

    Example return:
        1.0
    """
    # TODO: your code goes here
    raise NotImplementedError


def question_9(df: pd.DataFrame) -> dict[str, int]:
    """
    Q9. Return a dictionary mapping each weather condition to its count.

    Example return:
        {"sunny": 4, "cloudy": 3, "rain": 3}
    """
    # TODO: your code goes here
    raise NotImplementedError


def question_10(df: pd.DataFrame) -> float:
    """
    Q10. Return the mean NYC temperature on rows where Condition == "sunny".

    Example return:
        72.75
    """
    # TODO: your code goes here
    raise NotImplementedError


def question_11(df: pd.DataFrame) -> list[int]:
    """
    Q11. Sort by Rainfall descending and return the first 3 day values.

    Example return:
        [4, 8, 7]
    """
    # TODO: your code goes here
    raise NotImplementedError


def question_12(df: pd.DataFrame) -> dict[str, float]:
    """
    Q12. Group rows by whether day is odd or even, then return:
        {"odd": mean_NYC_on_odd_days, "even": mean_NYC_on_even_days}

    Example return:
        {"odd": 73.2, "even": 75.4}
    """
    # TODO: your code goes here
    raise NotImplementedError


# -----------------------------------------------------------------------------
# OPTIONAL: add your scratch work below this line if you want.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

def _assert_close(actual: float, expected: float, tol: float = 1e-9) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"Expected {expected}, got {actual}")


def _assert_dict_close(actual: dict[str, float], expected: dict[str, float], tol: float = 1e-9) -> None:
    if set(actual.keys()) != set(expected.keys()):
        raise AssertionError(f"Expected keys {set(expected.keys())}, got {set(actual.keys())}")
    for key in expected:
        if isinstance(expected[key], float):
            _assert_close(float(actual[key]), float(expected[key]), tol)
        else:
            if actual[key] != expected[key]:
                raise AssertionError(f"For key {key}, expected {expected[key]}, got {actual[key]}")


def run_tests() -> None:
    df = build_base_dataframe()

    # Test 1: Q1
    ans1 = question_1(df)
    assert ans1 == (10, 8), f"Q1 failed: expected (10, 8), got {ans1}"

    # Test 2: Q2
    ans2 = question_2(df)
    _assert_close(ans2, 74.3)

    # Test 3: Q3
    ans3 = question_3(df)
    assert ans3 == 6, f"Q3 failed: expected 6, got {ans3}"

    # Test 4: Q4
    ans4 = question_4(df)
    assert ans4 == 2, f"Q4 failed: expected 2, got {ans4}"

    # Test 5: Q5
    ans5 = question_5(df)
    _assert_close(ans5, 74.5)

    # Test 6: Q6
    ans6 = question_6(df)
    assert ans6 == (3, 34), f"Q6 failed: expected (3, 34), got {ans6}"

    # Test 7: Q7
    ans7 = question_7(df)
    assert ans7 == "Town_2", f"Q7 failed: expected 'Town_2', got {ans7}"

    # Test 8: Q8
    ans8 = question_8(df)
    _assert_close(ans8, 1.0)

    # Test 9: Q9
    ans9 = question_9(df)
    expected9 = {"sunny": 4, "cloudy": 3, "rain": 3}
    assert ans9 == expected9, f"Q9 failed: expected {expected9}, got {ans9}"

    # Test 10: Q10
    ans10 = question_10(df)
    _assert_close(ans10, 72.75)

    # Test 11: Q11
    ans11 = question_11(df)
    assert ans11 == [4, 8, 7], f"Q11 failed: expected [4, 8, 7], got {ans11}"

    # Test 12: Q12
    ans12 = question_12(df)
    expected12 = {"odd": 73.2, "even": 75.4}
    _assert_dict_close(ans12, expected12)

    print("All tests passed.")
    print()
    print("Q1:", ans1)
    print("Q2:", ans2)
    print("Q3:", ans3)
    print("Q4:", ans4)
    print("Q5:", ans5)
    print("Q6:", ans6)
    print("Q7:", ans7)
    print("Q8:", ans8)
    print("Q9:", ans9)
    print("Q10:", ans10)
    print("Q11:", ans11)
    print("Q12:", ans12)


if __name__ == "__main__":
    run_tests()
