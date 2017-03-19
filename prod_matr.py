def get_val_col_line_for_A(line, val_col_A):
	for i in range(0, len(val_col)):
		if val_col[i] == -line:
			first_index = i
		if val_col[i] == -line-1:
			second_index = i 
			return val_col[first_index+1:second_index-1]

def check_line_B_is_column_A(line_B, val_col_line_for_A):
	for x in val_col_line_for_A:
		if line_B == val_col_line_for_A[1]
			return true
	return false

def get_val_col_column_for_B(coloana_j, val_col_B ):
	tuplu_linie_valoare
	for i in range(0, len(val_col_B)):
		if val_col_B[i][0] < 0:
			last_line = -val_col_B[i]
		elif val_col_B[i][1] == coloana_j:
			val_col_column_for_B.append(x)
			tuplu_linie_valoare.append(last_line, val_col_B[i][0])
	return tupl_linie_valoare	
		

def prod_matr(d_A, val_col_A, d_B, val_col_B, nr_lines_A, nr_columns_A, nr_columns_B):
	d_prod = []
	val_col_prod = []
	for i in range(0, nr_lines_A):
		val_col.append(0, -(i+1))
		val_col_line_for_A = get_val_col_line_for_A(i, val_col_A)
		print(val_col_line_for_A)
		for j in range(0, nr_columns_B):
			tuplu_linie_valoare = get_val_column_for_B(j, val_col_B)
			print(tuplu_linie_valoare)			
	
