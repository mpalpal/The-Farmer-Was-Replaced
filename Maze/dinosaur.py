set_world_size(3)

clock_dir_list = [North, East, South, West]
co_clock_dir_list = [North, West, South, East]

clock_dir_dict = {
	North: 0, 
	East: 1, 
	South: 2, 
	West: 3
}
co_clock_dir_dict = {
	North: 0,
	West: 1,
	South: 2,
	East: 3
}

def dinosaur(dict, list):
	global last_dir
	global order
	global no_move

	x = get_pos_x()
	y = get_pos_y()

	first_time = True
	move_times = n - 1
	move_counts = 0
	move_once = 0
	finish_loop = False
	
	if first_time == True:
		order = [0, 1, 2, 3]
	else:
		index = (dict[last_dir]+3) % 4
		for i in range(4):
			order.append((index + i)% 4)

	while finish_loop == False:
		for ind in order:
			dir = list[ind]
			for i in range(move_times):
				move(dir)
			move_counts += 1
			k = (move_counts+1) // 2
			move_times = n - 2*k
			if move_times == 1:
				move_once += 1
			if move_once == 2:
				last_dir = dir
				order = []
				first_time = False
				finish_loop = True
				break

	if dict == clock_dir_dict:
		dict = co_clock_dir_dict
	else:
		dict = clock_dir_dict
	if list == clock_dir_list:
		list = co_clock_dir_list
	else:
		list = clock_dir_list

	move_times += 1
	move_counts = 0
	move_once = 0
	finish_loop = False
	add_times = 0

	index = (dict[last_dir]+3) % 4
	for i in range(4):
		order.append((index+ i)% 4)

	while finish_loop == False:
		for ind in order:
			dir = list[ind]
			for i in range(move_times):
				move(dir)
			move_counts += 1
			if move_counts == 1:
				move_times -= 1
			else:
				if move_times < n-2:
					if move_counts < n-1:
						if add_times % 2 == 0:
							move_times += 2
						add_times += 1
					if move_counts == n-1:
						move_times = n - 1
			if move_counts == n:
				last_dir = dir
				order = []
				finish_loop = True
				break
	
	if get_pos_x() == x and get_pos_y() == y:
		no_move = True

while True:

	# 初期位置移動
	clear()
	while get_pos_x() != 0:
		move(West)
	while get_pos_y() != 0:
		move(South)

	change_hat(Hats.Dinosaur_Hat)

	n = get_world_size()
	last_dir = None
	order = []

	no_move = False

	while no_move == False:

		x = get_pos_x()
		y = get_pos_y()
		dinosaur(clock_dir_dict, clock_dir_list)
		dinosaur(co_clock_dir_dict, co_clock_dir_list)

	change_hat(Hats.Dinosaur_Hat)


