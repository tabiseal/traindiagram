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
                # Draw stop duration with red line
                self.ax.plot([arrival_time, departure_time], [station_index, station_index], 'r-')
            self.connect_stations(line_name)

    def connect_stations(self, line_name):
        line = self.train_lines.get(line_name)
        sorted_stations = sorted((station, times) for station, times in line.items() if times)
        last_time = None  # To store the last time we need to connect from
        for station, times in sorted_stations:
            arrival_time, departure_time = times
            current_time = departure_time if departure_time else arrival_time
            if last_time is not None:
                # Draw travel line with blue line
                self.ax.plot([last_time, arrival_time], 
                             [self.stations.index(previous_station) + 1, self.stations.index(station) + 1], 'b-')
            last_time = current_time
            previous_station = station

    def show(self):
        plt.show()


