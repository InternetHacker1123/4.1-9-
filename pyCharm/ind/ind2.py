class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_string(cls, time_str):
        hour, minute, second = map(int, time_str.split(":"))
        return cls(hour, minute, second)

    @classmethod
    def from_seconds(cls, total_seconds):
        hour = total_seconds // 3600
        minute = (total_seconds % 3600) // 60
        second = total_seconds % 60
        return cls(hour, minute, second)

    @classmethod
    def from_time(cls, other_time):
        return cls(other_time.hour, other_time.minute, other_time.second)

    def to_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def to_minutes(self):
        return (
            (self.hour * 60) + self.minute + 1
            if self.second >= 30
            else self.hour * 60 + self.minute
        )

    def difference_in_seconds(self, other_time):
        return abs(self.to_seconds() - other_time.to_seconds())

    def add_seconds(self, seconds):
        total_seconds = self.to_seconds() + seconds
        return Time.from_seconds(total_seconds)

    def subtract_seconds(self, seconds):
        total_seconds = max(0, self.to_seconds() - seconds)
        return Time.from_seconds(total_seconds)

    def compare(self, other_time):
        if self.to_seconds() > other_time.to_seconds():
            return "First time is greater"
        elif self.to_seconds() < other_time.to_seconds():
            return "Second time is greater"
        else:
            return "Both times are equal"

    def read(self):
        time_str = input("Enter time in format 'hour:minute:second': ")
        self.hour, self.minute, self.second = map(int, time_str.split(":"))

    def display(self):
        print(f"{self.hour}:{self.minute}:{self.second}")


if __name__ == "__main__":
    # Пример использования класса Time
    t1 = Time(2, 30, 45)
    t2 = Time.from_string("5:15:10")

    print("Time 1:")
    t1.display()
    print("Time 2:")
    t2.display()

    print(
        "Difference in seconds between Time 1 and Time 2:", t1.difference_in_seconds(t2)
    )

    t3 = t1.add_seconds(100)
    print("Time 1 + 100 seconds:")
    t3.display()

    t4 = t2.subtract_seconds(30)
    print("Time 2 - 30 seconds:")
    t4.display()

    print("Comparison result:", t1.compare(t2))

    print("Time 1 in minutes:", t1.to_minutes())
