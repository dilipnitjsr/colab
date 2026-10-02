from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def run_demo(seed: int = 42) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    x = rng.uniform(0, 10, 300)
    noise = rng.normal(0, 1.5, 300)
    y = 3.2 * x + 7.5 + noise

    frame = pd.DataFrame({"x": x, "y": y})
    X_train, X_test, y_train, y_test = train_test_split(
        frame[["x"]],
        frame["y"],
        test_size=0.2,
        random_state=seed,
    )

    model = LinearRegression().fit(X_train, y_train)
    predictions = model.predict(X_test)

    return {
        "mae": float(mean_absolute_error(y_test, predictions)),
        "r2": float(r2_score(y_test, predictions)),
        "coefficient": float(model.coef_[0]),
        "intercept": float(model.intercept_),
    }


if __name__ == "__main__":
    metrics = run_demo()
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")
