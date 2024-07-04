# 示例
train_lines = ["Train A", "Train B", "Train C", "Train C", "Train D"]
stations = ["Station 1", "Station 2", "Station 3", "Station 4", "Station 5", "Station 6", "Station 7", "Station 8", "Station 9"]

schedule = TrainSchedule(train_lines, stations)
schedule.add_station_time("Train A", "Station 1", 5, 7)
schedule.add_station_time("Train A", "Station 2", 10, 12)
schedule.add_station_time("Train A", "Station 3", 15,17) 
schedule.add_station_time("Train A", "Station 4", 20)  # 无出发时间


schedule.add_station_time("Train B", "Station 1", 15, 17)
schedule.add_station_time("Train B", "Station 4", 25,27)
schedule.add_station_time("Train B", "Station 7", 35,37)
schedule.add_station_time("Train B", "Station 9", 45)

schedule.add_station_time("Train C", "Station 4", 5, 7)
schedule.add_station_time("Train C", "Station 5", 15,17)
schedule.add_station_time("Train C", "Station 6", 20)  # 无出发时间

schedule.show()
