direction_list = [
	North,
	East,
	South,
	West]

opp_dict = {
	North: South,
	East: West,
	South: North,
	West: East
	}

reset_maze = False
	
while True:
	if reset_maze == True:
		clear()
		reset_maze = False

	till()
	plant(Entities.bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

	x = get_pos_x()
	y = get_pos_y()
	goal_pos = measure()
	
	move_hist = {}
	branch2_dict = {}
	branch3_dict = {}
	
	last_time_dir = None
	back_dir = None
	
	while (x, y) != goal_pos:

		moved = False
		bra_che_counts = 0
		if last_time_dir != None:
			back_dir = opp_dict[last_time_dir]
	
		for dir in direction_list:
			if dir == back_dir:
				continue
			if can_move(dir) == True:
				bra_che_counts += 1
	
		if bra_che_counts == 2 and (x, y) not in branch2_dict:
			branch2_dict[(x, y)] = back_dir
		if bra_che_counts == 3 and (x, y) not in branch3_dict:
			branch3_dict[(x, y)] = []
			for dir in direction_list:
				if dir == back_dir:
					continue
				if can_move(dir) == True:
					branch3_dict[(x, y)].append(dir)
		if bra_che_counts >= 4:
			print("4 branches at the start point")
			reset_maze = True
			break

		for dir in direction_list:
			if dir == back_dir:
				continue
			if (x, y) in move_hist and dir == move_hist[(x, y)][0]:
				continue
			if (x, y) in branch2_dict and dir == branch2_dict[(x, y)]:
				continue
			if (x, y) in branch3_dict:
				if dir in branch3_dict[(x, y)]:
					branch3_dict[(x, y)].remove(dir)
				else:
					continue
			if can_move(dir) == True:
				if (x, y) not in move_hist:
					move_hist[(x, y)] = (dir, last_time_dir)
				move(dir)
				last_time_dir = dir
				x = get_pos_x()
				y = get_pos_y()
				moved = True
				break
	
		if not moved:
			if (x, y) in branch2_dict and branch2_dict[(x, y)] != None:
				move(branch2_dict[(x, y)])
				last_time_dir = branch2_dict[(x, y)]
				x = get_pos_x()
				y = get_pos_y()
			elif (x, y) not in move_hist or back_dir != move_hist[(x, y)][0]:
				move(back_dir)
				last_time_dir = back_dir
				x = get_pos_x()
				y = get_pos_y()
				while (x, y) not in branch2_dict and (x, y) not in branch3_dict:
					if move_hist[(x, y)][1] == None or (x, y) not in move_hist:
						break
					move_dir = opp_dict[move_hist[(x, y)][1]]
					move(move_dir)
					last_time_dir = move_dir
					x = get_pos_x()
					y = get_pos_y()
			else:
				print("can't move anywhere")
				reset_maze = True
				break
			
	if (x, y) == goal_pos and get_entity_type() == Entities.Treasure:
		harvest()