import matplotlib.pyplot as plt

class TrainSchedule:
    def __init__(self, train_lines, stations):
        self.train_lines = {line: {} for line in train_lines}
        self.stations = stations
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 60)
        plt.xticks(range(0, 61, 5))
        plt.yticks(range(1, len(stations) + 1), stations)
        plt.grid(True)
        self.ax.invert_yaxis()

    def add_station_time(self, line_name, station_name, arrival_time, departure_time=None):
        line = self.train_lines.get(line_name)
        if line is not None:
            station_index = self.stations.index(station_name) + 1
            line[station_name] = (arrival_time, departure_time)
            if departure_time:
                self.ax.plot([arrival_time, departure_time], [station_index, station_index], 'r-')
            self.connect_stations(line_name)

    def connect_stations(self, line_name):
        line = self.train_lines[line_name]
        # Sort stations by arrival time
        sorted_stations = sorted(line.items(), key=lambda x: x[1][0])
        last_time = None
        last_position = None
        for station, times in sorted_stations:
            arrival_time, departure_time = times
            current_time = departure_time if departure_time else arrival_time
            current_position = self.stations.index(station) + 1
            if last_time is not None and last_position is not None:
                # Draw travel line with blue line
                self.ax.plot([last_time, arrival_time], [last_position, current_position], 'b-')
            last_time = current_time
            last_position = current_position

    def show(self):
        plt.show()
