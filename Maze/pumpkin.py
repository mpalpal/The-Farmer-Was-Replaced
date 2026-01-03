import bf
bf.clear_till()

while True:

	first_time = True
	completed_row = []

	while len(completed_row) < get_world_size():
		if first_time == True:
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					plant(Entities.Pumpkin)
					move(East)
				move(North)
			first_time = False

		for i in range(get_world_size()):
			y = get_pos_y()
			replant_counts = 0
			if y in completed_row:
				move(North)
				continue
			for j in range(get_world_size()):
				if can_harvest() == True:
					move(East)
					continue
				else:
					plant(Entities.Pumpkin)
					replant_counts += 1
					move(East)
			if replant_counts == 0 and y not in completed_row:
					completed_row.append(y)
			move(North)

	if can_harvest() == True:
		harvest()