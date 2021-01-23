
import math as m

class ExpressionCalculator:
	def __init__(self, data, status):
		self.data = data
		self.status = status
		self.math_signs = ['+', '-', '×', '÷', '^', '√', 'sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'Log', 'Exp']
		self.math_sign_count = 0
		self.operator = None
		self.precedence = None
		self.sub_data = None
		self.position = None
		self.sum = 0
		self.sub_sum = 0
	
	def Operator(self, operator):
		levels = {'+': 1, '-': 1, '×': 2,'÷': 2, '^': 3, '√': 3, 'sin': 3, 'cos': 3, 'tan': 3, 'arcsin': 3, 'arccos': 3, 'arctan': 3, 'Log': 3, 'Exp': 3}
		return levels[operator]
	
	def getting_position_and_precedence(self, _data):
		max_pre = None
		current_pre = None
		sign = None
		position = 0
		position_1 = None
		position_2 = None
		close_counter = 0
		count = 0
		if ('(' or ')') not in _data:
			for char in _data:
				count += 1
				if char in self.math_signs:
					current_pre = self.Operator(char)
					if (max_pre == None) or (max_pre < current_pre):
						max_pre = current_pre
						sign = char
						position = count
					else:
						pass
			print(max_pre, sign, position)
			return (max_pre, sign, position)
		else:
			for char in _data:
				count += 1
				if char == '(':
					if close_counter != 1:
						position_1 = count
				elif char == ')':
					close_counter += 1
					if close_counter == 1:
						position_2 = count
						return position_1, position_2
						break
	
	def data_update(self, _data):
		if (self.precedence == 1) or (self.precedence == 2) or (self.precedence == 3 and self.operator == '^'):
			del _data[self.position - 2:self.position + 1]
			_data.insert(self.position - 2, self.sub_sum)
		elif (self.precedence == 3) and (self.operator == 'Log'):
			del _data[self.position - 1:self.position + 2]
			_data.insert(self.position - 1, self.sub_sum)
		else:
			del _data[self.position - 1:self.position + 1]
			_data.insert(self.position - 1, self.sub_sum)
		print(_data)
		self.position = None
		self.operator = None
		self.precedence = None
		self.sub_sum = 0
	
	def degree_to_radian_converter(self, value, status):
		# This function can only return values in radians.
		argv = 0
		if status == 'degree':
			argv = value * m.pi / 180
		elif status == 'radian':
			argv = value
		return argv
	
	def radian_to_degree_converter(self, value, status):
		# This function can return both radian and degree values depernding on the status.
		argv = 0
		if status == 'degree':
			argv = value * 180 / m.pi
		elif status == 'radian':
			argv = value
		return argv
	
	def expression_evaluator(self, _data):
		values = self.getting_position_and_precedence(_data)
		self.precedence, self.operator, self.position = values[0], values[1], values[2]
		if (self.precedence == 1) and (self.operator == '+'):
			sum_expression = lambda num_1, num_2: num_1 + num_2
			x, y = _data[self.position - 2], _data[self.position]
			self.sub_sum = sum_expression(x, y)
			self.data_update(_data)
		elif (self.precedence == 1) and (self.operator == '-'):
			sum_expression = lambda num_1, num_2: num_1 - num_2
			x, y = _data[self.position - 2], _data[self.position]
			self.sub_sum = sum_expression(x, y)
			self.data_update(_data)
		elif (self.precedence == 2) and (self.operator == '×'):
			sum_expression = lambda num_1, num_2: num_1 * num_2
			x, y = _data[self.position - 2], _data[self.position]
			self.sub_sum = sum_expression(x, y)
			self.data_update(_data)
		elif (self.precedence == 2) and (self.operator == '÷'):
			sum_expression = lambda num_1, num_2: num_1 / num_2
			x, y = _data[self.position - 2], _data[self.position]
			self.sub_sum = sum_expression(x, y)
			self.data_update(_data)
		elif (self.precedence == 3) and (self.operator == '^'):
			sum_expression = lambda num_1, num_2: num_1 ** num_2
			x, y = _data[self.position - 2], _data[self.position]
			self.sub_sum = sum_expression(x, y)
			self.data_update(_data)
		elif (self.precedence == 3) and (self.operator == '√'):
			sum_expression = lambda num_2: m.sqrt(num_2)
			y = _data[self.position]
			self.sub_sum = sum_expression(y)
			self.data_update(_data)
		elif (self.precedence == 3) and (self.operator == 'Exp'):
			sum_expression = lambda num_2: m.exp(num_2)
			y = _data[self.position]
			self.sub_sum = sum_expression(y)
			self.data_update(_data)
		elif (self.precedence == 3) and (self.operator == 'Log'):
			sum_expression = lambda num_1, num_2: m.log(num_2, num_1)
			x, y = _data[self.position], _data[self.position + 1]
			self.sub_sum = sum_expression(x, y)
			self.data_update(_data)
		elif (self.precedence == 3) and (self.operator == 'sin'):
			sum_expression = lambda num_2: m.sin(num_2)
			y = _data[self.position]
			self.sub_sum = sum_expression(self.degree_to_radian_converter(y, self.status))
			self.data_update(_data)
		elif (self.precedence == 3) and (self.operator == 'cos'):
			sum_expression = lambda num_2: m.cos(num_2)
			y = _data[self.position]
			self.sub_sum = sum_expression(self.degree_to_radian_converter(y, self.status))
			self.data_update(_data)
		elif (self.precedence == 3) and (self.operator == 'tan'):
			sum_expression = lambda num_2: m.tan(num_2)
			y = _data[self.position]
			self.sub_sum = sum_expression(self.degree_to_radian_converter(y, self.status))
			self.data_update(_data)
		elif (self.precedence == 3) and (self.operator == 'arcsin'):
			sum_expression = lambda num_2: m.asin(num_2)
			y = _data[self.position]
			self.sub_sum = self.radian_to_degree_converter(sum_expression(y), self.status)
			self.data_update(_data)
		elif (self.precedence == 3) and (self.operator == 'arccos'):
			sum_expression = lambda num_2: m.acos(num_2)
			y = _data[self.position]
			self.sub_sum = self.radian_to_degree_converter(sum_expression(y), self.status)
			self.data_update(_data)
		elif (self.precedence == 3) and (self.operator == 'arctan'):
			sum_expression = lambda num_2: m.atan(num_2)
			y = _data[self.position]
			self.sub_sum = self.radian_to_degree_converter(sum_expression(y), self.status)
			self.data_update(_data)
		return _data
	
	def math_sign_counter(self, _data):
		self.math_sign_count = 0
		for item in _data:
			if item in self.math_signs:
				self.math_sign_count += 1
		return self.math_sign_count
	
	def sub_data_manipulator(self):
		position_1, position_2 = self.getting_position_and_precedence(self.data)
		self.sub_data = self.data[position_1:position_2 - 1]
		del self.data[position_1 - 1:position_2]
		self.math_sign_counter(self.sub_data)
		while self.math_sign_count != 0:
			self.expression_evaluator(self.sub_data)
			self.math_sign_count -= 1
		if len(self.sub_data) == 1:
			self.data.insert(position_1 - 1, self.sub_data[0])
			self.sub_data = None
			self.math_sign_counter(self.data)
		return self.data
	
	def main(self):
		self.math_sign_counter(self.data)
		while self.math_sign_count != 0:
			self.math_sign_counter(self.data)
			if ('(' or ')') in self.data:
				self.sub_data_manipulator()
			else:
				self.expression_evaluator(self.data)
				self.math_sign_count -= 1
		else:
			self.sum = self.data[0]
		return self.sum