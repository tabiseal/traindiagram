from trainschedule import TrainSchedule

train_lines = ["Train A", "Train B", "Train C"]
stations = ["Utsumomiya", "Koganei", "Omiya", "Ueno", "Tokyo","Shinagawa"]

schedule = TrainSchedule(train_lines, stations)
schedule.add_station_time("Train A", "Utsumomiya", 5, 7)
schedule.add_station_time("Train A", "Koganei", 10, 12)
schedule.add_station_time("Train A", "Omiya", 15, 17)
schedule.add_station_time("Train A", "Ueno", 20)  # 无出发时间

schedule.add_station_time("Train B", "Utsumomiya", 15, 17)
schedule.add_station_time("Train B", "Omiya", 25,27)
schedule.add_station_time("Train B", "Tokyo", 35,37)
schedule.add_station_time("Train B", "Shinagawa", 45)

# schedule.add_station_time("Train C", "Koganei", 5, 7)
# schedule.add_station_time("Train C", "Omiya", 15,17)
# schedule.add_station_time("Train C", "Tokyo", 20)  # 无出发时间

schedule.show()
