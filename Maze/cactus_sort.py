# サボテンをソートする関数
def sort(r_or_c, index):

	global sorted_row
	global sorted_column

	# ソート方向によって変数を設定
	if r_or_c == 'row':
		target = '行'
		sorted_list = sorted_row
		dir1 = East
		dir2 = West
		next_row = North
		ind = get_pos_y()
	elif r_or_c == 'column':
		target = '列'
		sorted_list = sorted_column
		dir1 = North
		dir2 = South
		next_column = East
		ind = get_pos_x()
	else:
		print('Error: r_or_c must be "row" or "column".')
		return

	# 現在の位置が対象の行/列でない場合、エラーを表示して終了
	if ind != index:
		print('Error: Current index does not match target index.')
		return  

	# 初期化
	swap_counts = 0
	first_time_sort = True

	# スワップループ
	while swap_counts > 0 or first_time_sort == True:
		swap_counts = 0
		for i in range(get_world_size()-1):
			compare_right = measure(dir1)
			move(dir1)
			compare_left = measure(dir2)
			if compare_right < compare_left:
				swap(dir2)
				swap_counts += 1
		move(dir1)
		first_time_sort = False

	sorted_list.append((ind, target))
	if r_or_c == 'row':
		move(next_row)
	if r_or_c == 'column': 
		move(next_column)

while True:

	# 初期位置に移動
	while get_pos_x() != 0:
		move(West)
	while get_pos_y() != 0:
		move(South)

	# 全マスにサボテンを植える
	if get_entity_type() != Entities.Cactus:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				plant(Entities.Cactus)
				move(East)
			move(North)

	# 履歴記録用リスト
	sorted_row = []
	sorted_column = []

	# 行方向でソートを実行
	for y in range(get_world_size()):
		sort('row', y)

	# 列方向でソートを実行
	for x in range(get_world_size()):
		sort('column', x)

	# すべての行と列がソートされたか確認し、収穫
	if len(sorted_row) == get_world_size() and len(sorted_column) == get_world_size():
		if can_harvest():
			harvest()
	else:
		print('Error: Not all rows and columns were sorted successfully.')


