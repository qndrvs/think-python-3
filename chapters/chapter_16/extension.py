## EXTENSIONS
import random

# 1. Extension - Stateful objects and state machines
""""
a. Build a class called TrafficLight with states: 'red', 'yellow', 'green'. __init__(self, initial='red'): initializes the light. Raise ValueError if initial is not a valid state.
b. Implement:
   - next_state(self): transitions to the next state in cycle red->green->yellow->red
   - is_safe_to_go(self): True if state is 'green'
   - __str__: 'TrafficLight(state=green)'
   - cycles_completed(self): counts how many full red-green-yellow-red cycles have completed since initialization (track this internally)
c. Write a function called simulate_traffic(self, n_steps) that calls next_state n_steps times and returns a list of states visited. Verify that the pattern repeats with period 3.
"""

# 1.a
class TrafficLight:
    def __init__(self, state: str = 'red'):
        VALID_STATES: set = {'red', 'yellow', 'green'}
        if state not in VALID_STATES: raise ValueError(f"Invalid state: '{state}'. Allowed states are: {VALID_STATES}")
        self.state = state
        self.cycles_complete = 0
        self.start_red = True if state == 'red' else False

# 1.b
    def next_state(self):
        cycle: list = ['red', 'green', 'yellow']
        index: int = (cycle.index(self.state) + 1) % len(cycle)
        self.state = cycle[index]
        if self.state == 'red':
            if self.start_red: self.cycles_complete += 1
            self.start_red = True

    def is_safe_to_go(self):
        return self.state == 'green'

    def __str__(self):
        return f'TrafficLight(state={self.state})'

    def cycles_completed(self):
        return self.cycles_complete

# 1.c
    def simulate_traffic(self, n_steps: int):
        states_visited: list = [self.state]
        for i in range(n_steps):
            self.next_state()
            states_visited.append(self.state)
        return states_visited
print("done")


# 2. Extension - Object composition and delegation
"""
a. Build a class called Sensor:
   def __init__(self, sensor_id, unit, low_limit, high_limit):
   - sensor_id: string identifier
   - unit: string like 'C', 'Pa', '%'
   - low_limit, high_limit: valid range for readings
   Raise ValueError if low_limit >= high_limit.
b. Add:
   - record(self, value): stores a reading; raise ValueError if outside limits Store readings in a list self.readings.
   - current(self): returns the most recent reading, or None if no readings
   - mean(self): returns mean of all readings, or None if empty
   - is_warning(self, threshold=0.9): True if current reading is within threshold fraction of either limit i.e., abs(current - limit) < (1 - threshold) * (high_limit - low_limit)
   - __str__: 'Sensor(id=TEMP_01, current=36.6C, readings=10)'
c. Build a class called SensorArray:
   __init__(self, name): name of the array, empty list of sensors
   - add_sensor(self, sensor): appends a Sensor to the array
   - get_sensor(self, sensor_id): returns the Sensor with that id, or None
   - record_all(self, readings_dict): takes {sensor_id: value} and calls record() on each matching sensor
   - any_warnings(self): True if any sensor is in warning state
   - summary(self): prints a table of all sensors with current value and status
d. Write a function called simulate_readings(array, n_steps, seed=42) that generates n_steps of random readings for each sensor (within valid range) and feeds them through record_all. After simulation, call summary() and report any warnings.
"""
print("\nEXTENSION 2")

# 2.a
class Sensor:
    def __init__(self, sensor_id: str, unit: str, low_limit: int | float, high_limit: int | float):
        self.sensor_id: str = sensor_id
        self.unit: str = unit

        if low_limit >= high_limit: raise ValueError(f"Invalid limits:\n- {low_limit} >= {high_limit}")
        self.low_l: int | float = low_limit
        self.high_l: int | float = high_limit
        self.readings: list = []

# 2.b
    def record(self, value: int | float) -> None:
        if value < self.low_l or value > self.high_l: raise ValueError(f"Invalid 'value': {value}")
        self.readings.append(value)

    def current(self) -> int | float | None:
        if not self.readings: return None
        return self.readings[-1]

    def mean(self) -> int | float | None:
        total: float = 0.0
        if not self.readings: return None
        for read in self.readings: total += read
        return total / len(self.readings)

    def is_warning(self, threshold: int | float = 0.9) -> bool | None:
        now: float | int | None = self.current()
        if now is None: return None
        extrem: float = (1 - threshold) * (self.high_l - self.low_l)
        return (abs(now - self.low_l) < extrem) or (abs(now - self.high_l) < extrem)

    def __str__(self):
        return f'Sensor(id = {self.sensor_id}, current = {self.current()}{self.unit}, readings = {len(self.readings)})'

# 2.c
class SensorArray:
    def __init__(self, name: str):
        self.name: str = name
        self.sensors: list = []

    def add_sensor(self, sensor: Sensor):
        self.sensors.append(sensor)

    def get_sensor(self, sensor_id: str) -> Sensor | None:
        for sensor in self.sensors:
            if sensor.sensor_id == sensor_id: return sensor
        return None

    def record_all(self, readings_dict: dict):
        for sensor_id, value in readings_dict.items():
            sensor: Sensor = self.get_sensor(sensor_id)
            if sensor is not None:
                sensor.record(value)

    def any_warnings(self) -> bool:
        for sensor in self.sensors:
            if sensor.is_warning(): return True
        return False
    
    def summary(self):
        print(f"{'ID':<10} {'Value':<10} {'Status'}")
        print("-" * 30)
        for sensor in self.sensors:
            current = sensor.current()
            status = "WARNING" if sensor.is_warning() else "OK"
            if current is None:
                print(f"{sensor.sensor_id:<10} {'N/A':<10} {status}")
            else:
                print(f"{sensor.sensor_id:<10} {current:<10.2f} {status}")

# 2.d
def simulate_readings(array: SensorArray, n_steps: int, seed = 42):
    random.seed(seed)
    for _ in range(n_steps):
        readings: dict = {}
        for sensor in array.sensors:
            value = random.uniform(sensor.low_l, sensor.high_l)
            readings[sensor.sensor_id] = value
        array.record_all(readings)
    array.summary()
    print("WARN") if array.any_warnings() else print("OK")