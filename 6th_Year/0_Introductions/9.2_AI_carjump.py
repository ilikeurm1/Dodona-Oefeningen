from math import sin, radians, ceil, sqrt  # noqa: F401

g = 9.81
MIN_SPEED = 10
MAX_SPEED = 240
MIN_ANGLE = 1
MAX_ANGLE = 65


def predict_optimal_speed(target_distance: float, angle: int = 45) -> int:
    """
    Predict optimal speed for a given distance using physics formula.
    Formula: distance = (v^2 * sin(2*theta)) / g
    Solving for v: v = sqrt((distance * g) / sin(2*theta))

    Returns speed in km/h (rounded up to nearest integer)
    """
    angle_rad = radians(angle)
    v_ms = sqrt((target_distance * g) / sin(2 * angle_rad))  # m/s
    v_kmh = v_ms * 3.6  # convert to km/h
    # return ceil(v_kmh)  # round up to ensure we make it
    return round(
        v_kmh  # we dont need to round up since we added 2.5m to target distance
    )


def makes_it(distance: float, target: float, filter: bool) -> bool:
    """Function that returns whether the jump makes it whithin the ramp area.

    Args:
        distance (float): the distance jumped
        target (float): the distance to reach
        filter (bool): Whether to filter the results. If this is false all jumps will return True.

    Returns:
        bool: If the jump should be processed
    """
    if not filter:
        return True

    return distance >= target - 2.5 and distance <= target + 2.5  # On the ramp


# theta: int = 45
def calculate_score(distance: float, speed: int, angle: int, target: float) -> float:
    """
    Calculate score based on:
    - distance from target distance x (the closer the better)
    - speed (the lower the better)
    - angle (the closer to 45 degrees the better (as 45 is optimal for distance))
    """
    return (
        abs(distance - target) * 10  # distance penalty (10 * distance difference)
        + speed // 2  # speed penalty (speed divided by 2)
        + abs(angle - 45) * 3  # angle penalty (3 * angle difference)
    )


def find_optimal_jump(
    target_distance: float,
    /,
    min_speed: int = MIN_SPEED,
    max_speed: int = MAX_SPEED,
    min_angle: int = MIN_ANGLE,
    max_angle: int = MAX_ANGLE,
    filter_jumps: bool = True,
    save_to_file: bool = True,
) -> dict[tuple[float, int, int], float]:
    """
    Find optimal car jump parameters using brute force search.

    Args:
        target_distance (int): Distance to jump in meters (will add 2.5m for ramp).
        min_speed (int, optional): Minimum speed to test in km/h. Defaults to MIN_SPEED.
        max_speed (int, optional): Maximum speed to test in km/h. Defaults to MAX_SPEED.
        min_angle (int, optional): Minimum angle to test in degrees. Defaults to MIN_ANGLE.
        max_angle (int, optional): Maximum angle to test in degrees. Defaults to MAX_ANGLE.
        filter_jumps (bool, optional): If True, include only valid landings; if False, include all attempts. Defaults to True.
        save_to_file (bool, optional): If True, save results to a text file. Defaults to True.

    Returns:
        Dictionary_mapping (distance, speed, angle) tuples to scores, sorted by score
    """

    target_with_ramp = target_distance + 2.5
    scores: dict[tuple[float, int, int], float] = {}

    for v in range(min_speed, max_speed + 1):
        for theta in range(min_angle, max_angle + 1):
            delta_x = round(((v / 3.6) ** 2 * sin(2 * radians(theta))) / g, 2)
            scores[(delta_x, v, theta)] = calculate_score(
                delta_x, v, theta, target_with_ramp
            )

    # Filter once after all calculations
    scores = dict(
        filter(
            lambda item: makes_it(item[0][0], target_with_ramp, filter_jumps),
            scores.items(),
        )
    )

    scores = dict(sorted(scores.items(), key=lambda item: item[1]))

    if save_to_file and scores:
        with open(
            rf"output\python\car_ai_{target_distance:.0f}m.txt",
            "w",
        ) as f:
            f.write("Results sorted from best to worst:\n")
            f.write("((Distance(m), Speed(km/h), Angle(deg)), Score)\n")
            f.write("[\n")
            for params, score in scores.items():
                distance, speed, angle = params
                f.write(f"  (({distance:.2f}, {speed}, {angle}), {score:.2f}),\n")
            f.write("]\n")

    return scores


def run_interactive():
    """Run the car jump optimizer interactively with user input."""
    LOOPED: bool = True

    if not LOOPED:
        target_distance = float(input("Enter the distance to jump (in m): "))
        scores = find_optimal_jump(target_distance)

        if scores:
            best_params = list(scores.keys())[0]
            best_score = scores[best_params]
            print(f"The best score is {best_score:.2f} with: {best_params}")
        else:
            print("No valid solutions found!")
    else:
        MIN_TARGET = 5
        MAX_TARGET = 200

        for target_distance in range(MIN_TARGET, MAX_TARGET + 1):
            scores = find_optimal_jump(target_distance)

            if scores:
                best_params = list(scores.keys())[0]
                best_score = scores[best_params]
                print(
                    f"The best score for {target_distance}m is {best_score:.2f} with: {best_params}"
                )
            else:
                print("No valid solutions found!")


def test_prediction():
    """Test the prediction function against various distances."""
    print("\n--- Testing Prediction Function ---")
    for test_distance in [50, 60, 70, 80, 90]:
        surrounding = []
        predicted_speed = predict_optimal_speed(test_distance + 2.5)
        actual_distance = round(
            ((predicted_speed / 3.6) ** 2 * sin(2 * radians(45))) / g, 2
        )
        surrounding.append(
            (
                predicted_speed - 2,
                round(
                    (((predicted_speed - 2) / 3.6) ** 2 * sin(2 * radians(45))) / g, 2
                ),
            )
        )
        surrounding.append(
            (
                predicted_speed - 1,
                round(
                    (((predicted_speed - 1) / 3.6) ** 2 * sin(2 * radians(45))) / g, 2
                ),
            )
        )
        surrounding.append(
            (
                predicted_speed + 1,
                round(
                    (((predicted_speed + 1) / 3.6) ** 2 * sin(2 * radians(45))) / g, 2
                ),
            )
        )
        surrounding.append(
            (
                predicted_speed + 2,
                round(
                    (((predicted_speed + 2) / 3.6) ** 2 * sin(2 * radians(45))) / g, 2
                ),
            )
        )
        print(
            f"Target: {test_distance}m → Predicted speed: {predicted_speed} km/h at 45° → Actual distance: {actual_distance}m"
        )
        print("  Surrounding speeds and distances:")
        for speed, distance in surrounding:
            print(f"    Speed: {speed} km/h → Distance: {distance} m")


if __name__ == "__main__":
    run_interactive()
    # test_prediction()
