def clear_till():
	clear()
	for i in range(get_world_size()):
		while get_ground_type()==Grounds.Grassland:
			till()
			move(North)
		move(East)

def water():
	if get_water()<=1 and num_items(Items.water)>=1:
			use_item(Items.water)
	