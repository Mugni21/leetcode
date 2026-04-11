"""
STORE SALES REGRESSION PRACTICE - STARTER TEMPLATE

Instructions:
- Fill in the TODO sections.
- Keep the function names unchanged.
- Run this file directly to execute the automated tests.

Command:
    python solution.py
"""

from itertools import combinations

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def build_base_dataframe() -> pd.DataFrame:
    """Return the base dataset for the exercise."""
    return pd.DataFrame(
        {
            "day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "Flagship": [72, 75, 78, 80, 83, 85, 88, 84, 81, 79, 76, 74],
            "Store_1": [70, 73, 76, 79, 82, 84, 87, 83, 80, 77, 74, 72],
            "Store_2": [65, 68, 72, 77, 81, 86, 91, 89, 85, 80, 73, 69],
            "Store_3": [90, 92, 95, 99, 101, 98, 96, 94, 89, 87, 85, 88],
            "Store_4": [55, 60, 66, 71, 75, 80, 84, 82, 78, 72, 67, 61],
            "Store_5": [74, 74, 77, 79, 82, 85, 89, 86, 82, 78, 75, 73],
        }
    )


def question_1(df: pd.DataFrame) -> str:
    """
    Q1. Among Store_1 through Store_5, return the store with the largest sample std.

    Example return:
        "Store_4"
    """
    store_cols = [col for col in df.columns if col.startswith("Store_")]

    # TODO: your code goes here
    stds = df[store_cols].std()
    return stds.idxmax()



def question_2(df: pd.DataFrame) -> float:
    """
    Q2. Return the median Flagship sales on the rows where Store_3 is in [90, 100].

    Example return:
        80.0
    """
    # TODO: your code goes here
    mask = (df["Store_3"] >= 90) & (df["Store_3"] <= 100)
    return float(df.loc[mask, "Flagship"].median())



def _fit_and_mse(X: pd.DataFrame | np.ndarray, y: pd.Series | np.ndarray) -> tuple[LinearRegression, float]:
    """Fit a linear regression and return (model, mse)."""
    model = LinearRegression()
    model.fit(X, y)
    preds = model.predict(X)
    mse = float(np.mean((y - preds) ** 2))
    return model, mse



def question_3(df: pd.DataFrame) -> tuple[str, float]:
    """
    Q3. For each single store, fit a linear regression predicting Flagship.
    Return (best_store, best_mse).

    Example return:
        ("Store_1", 0.17047619047619045)
    """
    store_cols = [col for col in df.columns if col.startswith("Store_")]
    y = df["Flagship"]

    # TODO: your code goes here
    best_store = None
    best_mse = float("inf")

    for store in store_cols:
        _, mse = _fit_and_mse(df[[store]], y)
        if mse < best_mse:
            best_store = store
            best_mse = mse

    return best_store, float(best_mse)



def question_4(df: pd.DataFrame) -> tuple[tuple[str, str], float]:
    """
    Q4. For each pair of distinct stores, fit a regression predicting Flagship.
    Return (best_pair, best_mse).

    Example return:
        (("Store_1", "Store_4"), 0.14475991090933812)
    """
    store_cols = [col for col in df.columns if col.startswith("Store_")]
    y = df["Flagship"]

    # TODO: your code goes here
    best_pair = None
    best_mse = float("inf")

    for pair in combinations(store_cols, 2):
        _, mse = _fit_and_mse(df[list(pair)], y)
        if mse < best_mse:
            best_pair = pair
            best_mse = mse

    return best_pair, float(best_mse)



def question_5(df: pd.DataFrame) -> float:
    """
    Q5. Using the five single-store regressions from Q3, compute the sum of the
    absolute values of the five slope coefficients.

    Example return:
        4.073996757877766
    """
    store_cols = [col for col in df.columns if col.startswith("Store_")]
    y = df["Flagship"]

    # TODO: your code goes here
    total = 0.0
    for store in store_cols:
        model, _ = _fit_and_mse(df[[store]], y)
        total += abs(float(model.coef_[0]))
    return float(total)



def question_6_comment() -> str:
    """
    Q6. Return a short comment string describing one reasonable approximation
    strategy when P is very large and brute force subset search is too expensive.

    Example return:
        "Use lasso to shrink many coefficients to zero, then keep the selected towns."
    """
    # TODO: your code goes here
    return (
        "Use an L1-penalized regression such as lasso to shrink many coefficients "
        "to zero, then keep the selected stores as an approximate best subset."
    )


# -----------------------------------------------------------------------------
# OPTIONAL: add your scratch work below this line if you want.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

def _assert_close(actual: float, expected: float, tol: float = 1e-9) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"Expected {expected}, got {actual}")



def run_tests() -> None:
    df = build_base_dataframe()

    # Test 1: Q1
    ans1 = question_1(df)
    assert ans1 == "Store_4", f"Q1 failed: expected 'Store_4', got {ans1}"

    # Test 2: Q2
    ans2 = question_2(df)
    _assert_close(ans2, 80.0)

    # Test 3: Q3
    best_store, best_mse = question_3(df)
    assert best_store == "Store_1", f"Q3 failed: expected 'Town_1', got {best_store}"
    _assert_close(best_mse, 0.17047619047619045)

    # Test 4: Q4
    best_pair, pair_mse = question_4(df)
    assert set(best_pair) == {"Store_1", "Store_4"}, (
        f"Q4 failed: expected pair {{'Store_1', 'Store_4'}}, got {best_pair}"
    )
    _assert_close(pair_mse, 0.14475991090933812)

    # Test 5: Q5
    ans5 = question_5(df)
    _assert_close(ans5, 4.073996757877766)

    # Test 6: Q6
    comment = question_6_comment().lower()
    valid_keywords = [
        "lasso",
        "l1",
        "forward",
        "stepwise",
        "backward",
        "greedy",
        "feature selection",
    ]
    assert any(keyword in comment for keyword in valid_keywords), (
        "Q6 failed: your comment should mention a sensible approximation strategy."
    )

    # Extra test 7: Q2 on a modified dataset with a different filtered median
    df2 = df.copy()
    df2.loc[:, "Store_3"] = [89, 91, 95, 100, 101, 88, 93, 94, 86, 85, 84, 83]
    # Filtered rows are indices 1,2,3,6,7 with NYC temps [75,78,80,88,84] => median 80
    ans2b = question_2(df2)
    _assert_close(ans2b, 80.0)

    print("All tests passed.")
    print()
    print("Q1:", ans1)
    print("Q2:", ans2)
    print("Q3:", (best_store, best_mse))
    print("Q4:", (best_pair, pair_mse))
    print("Q5:", ans5)
    print("Q6:", question_6_comment())


if __name__ == "__main__":
    run_tests()
