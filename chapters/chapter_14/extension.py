## EXTENSIONS
import math

# 1. Extension 1 - Designing a Point class without __init__
"""
a. Define a class called Point that represents a 2D coordinate. Add a docstring: 'Represents a point in 2D Cartesian space. Attributes: x, y'. No __init__. No methods inside the class.
b. Write a FUNCTION (not a method) called make_point(x, y) that creates a Point instance, assigns its attributes, and returns it.
c. Write a function called print_point(p) that prints '(x, y)' with 2 decimal places.
d. Write these as PURE FUNCTIONS (return a new Point, never modify inputs):
   - add_points(p1, p2): returns p1 + p2 component-wise
   - scale_point(p, scalar): returns scalar * p
   - distance(p1, p2): returns Euclidean distance between two Points.
   - midpoint(p1, p2): returns the midpoint between two Points
   - reflect_origin(p): returns the point reflected through the origin (-x, -y)
e. Write these as MODIFIERS (mutate the object, return None):
   - translate(p, dx, dy): adds dx to p.x and dy to p.y
   - scale_in_place(p, scalar): multiplies both coordinates by scalar
"""
print("\nEXTENSION 1")

# 1.a
class Point:
    """Represents a point in 2D Cartesian space. Attributes: x, y"""

# 1.b
def make_point(x: float | int, y: float | int) -> Point:
    point = Point()
    point.x, point.y = x, y
    return point

# 1.c
def print_point(p: Point) -> None:
    print(f'({p.x:.02f}, {p.y:.02f})')

# 1.d
def add_points(p1: Point, p2: Point) -> Point:
    p = Point()
    p.x, p.y = p1.x + p2.x, p1.y + p2.y
    return p
def scale_point(p: Point, k: float | int) -> Point:
    p_new = Point()
    p_new.x, p_new.y = p.x * k, p.y * k
    return p_new
def distance(p1: Point, p2: Point) -> float:
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    distance: float = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    return distance
def midpoint(p1: Point, p2: Point) -> Point:
    p = Point()
    p.x = (p1.x + p2.x) / 2
    p.y = (p1.y + p2.y) / 2
    return p
def reflect_origin(p: Point) -> Point:
    p_new = Point()
    p_new.x, p_new.y = -1 * p.x, -1 * p.y
    return p_new

# 1.e
def translate(p: Point, dx: float | int, dy: float | int) -> None:
    p.x += dx
    p.y += dy
def scale_in_place(p: Point, k: float | int) -> None:
    p.x *= k
    p.y *= k


# 2. Extension 2 - Object as a data record
"""
a. Define a class called Observation with docstring: 'Represents a single sensor observation. Attributes: sensor_id, value, unit, timestamp'
   Write make_observation(sensor_id, value, unit, timestamp) as a factory function.
   Write print_observation(obs) that prints:
    [timestamp] sensor_id: value unit
b. Write a function called is_valid_observation(obs, low, high) that returns True if obs.value is within [low, high] and obs.sensor_id is a non-empty string. Return False and print a specific error for each failure mode.
c. Write a function called observations_mean(obs_list) that takes a list of Observation objects and returns the mean of their values. Add validation: return None if the list is empty.
d. Write a function called filter_by_sensor(obs_list, sensor_id) that returns a new list containing only observations from the given sensor. The original list must not be modified.
e. Write a function called normalize_observations(obs_list) that returns a NEW list of Observation objects where each value has been scaled to [0, 1] relative to the min and max values in the list. The original obs_list and its objects must remain unchanged. This is a pure function.
"""
print("\nEXTENSION 2")

# 2.a
class Observation:
    """Represents a single sensor observation. Attributes: sensor_id, value, unit, timestamp"""
def make_observation(sensor_id: str, value: float, unit: str, timestamp: str) -> Observation:
    obs: Observation = Observation()
    obs.sensor_id = sensor_id
    obs.value = value
    obs.unit = unit
    obs.timestamp = timestamp
    return obs
def print_observation(obs: Observation) -> None:
    print(f'[{obs.timestamp}] {obs.sensor_id}: {obs.value} {obs.unit}')

# 2.b
def is_valid_observation(obs: Observation, low: int | float, high: int | float) -> bool:
    return obs.sensor_id and (low <= obs.value <= high)

# 2.c
def observations_mean(obs_list: list) -> float | None:
    if not obs_list: return None
    total: float = 0.0
    for obs in obs_list:
        total += obs.value
    return total / len(obs_list)

# 2.d
def filter_by_sensor(obs_list: list, sensor_id: str) -> list:
    return [obs for obs in obs_list if obs.sensor_id == sensor_id]

# 2.e
def normalize_observations(obs_list: list) -> list:
    ordered: list = sorted(obs_list, key = lambda x: x.value)
    high: float = ordered[-1].value
    low : float = ordered[0].value
    if high == low: return [make_observation(obs.sensor_id, 0.0, obs.unit, obs.timestamp) for obs in obs_list]
    return [
        make_observation(
            obs.sensor_id, 
            (obs.value - low) / (high - low),
            obs.unit, 
            obs.timestamp
        ) 
        for obs in obs_list
    ]


# 3. Extension 3 - Prototype-and-patch: time arithmetic
"""
a. Define a class called Time:
    'Represents a time of day. Attributes: hour, minute, second'
   Write make_time(hour, minute, second) that validates:
   - 0 <= hour <= 23
   - 0 <= minute <= 59
   - 0 <= second <= 59
   Raise ValueError with a descriptive message for any violation. Write print_time(t) that prints 'HH:MM:SS' with zero-padding.
b. Write time_to_seconds(t) that converts a Time to total seconds since midnight. Write seconds_to_time(seconds) that converts total seconds back to a Time. Verify the round-trip: seconds_to_time(time_to_seconds(t)) gives the same time.
c. Write add_time(t1, t2) as a PURE FUNCTION that adds two Times.
   Test: add_time(10:30:00, 2:45:30) -> 13:15:30
   Test wrap-around: add_time(23:00:00, 2:00:00) -> 01:00:00 (next day wraps)
d. Write increment(t, seconds) as a MODIFIER that adds seconds to t in place.
   Verify: after increment(t, 3600), t.hour has increased by 1 (if no overflow).
"""
print("\nEXTENSION 3")

# 3.a
class Time:
    """Represents a time of day. Attributes: hour, minute, second"""
def make_time(hour: int, minute: int, second: int) -> Time:
    errors: list = []
    if hour < 0 or hour > 23: errors.append("hour")
    if minute < 0 or minute > 59: errors.append("minute")
    if second < 0 or second > 59: errors.append("second")
    if errors: raise ValueError(f"Invalid value(s) for: {', '.join(errors)}.")
    t: Time = Time()
    t.hour = hour
    t.minute = minute
    t.second = second
    return t
def print_time(t: Time) -> None:
    print(f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}')

# 3.b
def time_to_seconds(t: Time) -> int:
    seconds: int = 0
    seconds += t.hour * 3600
    seconds += t.minute * 60
    seconds += t.second
    return seconds
def seconds_to_time(seconds: int) -> Time:
    t: Time = Time()
    t.hour, temp = divmod(seconds, 3600)
    t.minute, temp = divmod(temp, 60)
    t.second = temp
    return t

# 3.c
def add_time(t1: Time, t2: Time) -> Time:
    t: Time = Time()
    temp, seconds = divmod(t1.second + t2.second, 60)
    temp, minutes = divmod(t1.minute + t2.minute + temp, 60)
    temp, hours = divmod(t1.hour + t2.hour + temp, 24)
    t.hour, t.minute, t.second = hours, minutes, seconds
    return t

# 3.d
def increment(t: Time, secs: int) -> None:
    total_seconds: int = (time_to_seconds(t) + secs) % (24 * 3600)
    new_t: Time = seconds_to_time(total_seconds)
    t.hour, t.minute, t.second = new_t.hour, new_t.minute, new_t.second