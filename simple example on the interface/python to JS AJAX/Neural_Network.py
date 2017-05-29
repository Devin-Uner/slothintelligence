# for random intializatin of weights
# also for randomly zeroing weights during runtime
import random, math
# random.seed(1)






class Neural_Network(object):
	"""docstring for Neural_Network"""
	def __init__(self, num_neurons_per_layer_):

		# the length of the neural network
		self.layer_count = len(num_neurons_per_layer_)

		# the layers
		self.layers = [[0]*layer_len for layer_len in num_neurons_per_layer_]

		# initialize the weights of the neural network
		self.weights = []
		try:
			self.read_data()
		except:
			print "failed"
			for i in range(0, len(num_neurons_per_layer_)-1):
				self.weights += [[     [random.uniform(-1,1) for x in range(num_neurons_per_layer_[i+1])]     for j in range(0,num_neurons_per_layer_[i])]]


	def sigmasoid(self, x, deriv=False):
		if(deriv):
			return x*(1-x)
		return 1/(1+ (2.7182818284590451**-x))


	def dot_sigma(self, x, y, sigma_val):
		new = []
		for c in range(0,len(y[0])):
			new += [self.sigmasoid(sum([x[r]*y[r][c] for r in range(0, len(y))]), sigma_val)]
		return new

	def dot(self, x, y):
		new = []
		for c in range(0,len(y[0])):
			new += [sum([x[r]*y[r][c] for r in range(0, len(y))])]
		return new


	def get_output(self, data):
		if(len(data) != len(self.layers[0])):
			raise ValueError("invalid length of input :)")
		# set the initial input
		self.layers[0] = data
		for i in range(1, self.layer_count-1):
			# calculate the next line of output
			self.layers[i] = self.dot_sigma(self.layers[i-1], self.weights[i-1], False)

			# bias values
			self.layers[i][0] = 1
		self.layers[-1] = self.dot_sigma(self.layers[-2], self.weights[-1], False)
		return self.layers[-1]



	def train(self, input_data, output_data):
		# calculate the output given the input
		y = self.get_output(input_data)
		error = [output_data[i] - y[i] for i in range(len(y))]
		self.backpropigate(error)
		return error



	def backpropigate(self, final_error):
		# initialize the change and error
		error = [  [] for i in range(0, len(self.layers)) ]
		change = [  [] for i in range(0, len(self.layers)) ]

		

		# calculate the final error and final change
		error[-1] = final_error
		change[-1] = [error[-1][i]*self.sigmasoid(self.layers[-1][i],True) for i in range(len(error[-1]))]

		# print the error
		# print "error is: " "{0:.5f}".format(abs(sum(error[-1])))

		# backpropigate
		for n in range(len(self.layers)-2, -1, -1):
			# transform weights[n]
			new = [[0]*len(self.weights[n]) for j in range(len(self.weights[n][0]))]
			for r in range(len(self.weights[n])):
				for c in range(len(self.weights[n][0])):
					new[c][r] = self.weights[n][r][c]
			# calculate the error and change
			error[n] = self.dot(change[n+1], (new))
			change[n] = [error[n][i] * self.sigmasoid(self.layers[n][i], True) for i in range(len(error[n]))]

		# add the change to the weights
		for i in range(0, len(self.weights)):
			for r in range(len(self.weights[i])):
				for c in range(len(self.weights[i][0])):
					self.weights[i][r][c] += self.layers[i][r]*change[i+1][c]
					# if(random.random() < 0.000001):
					# 	self.weights[i][r][c] = 0

		# for errornum in error:
		# 	print errornum,"\n"


		return error

	def save_data(self):
		num = 0
		for weight_layer in self.weights:
			num+=1
			with open("weight" + str(num) + ".txt", "w") as output_file:
				for weight in weight_layer:
					output_file.write(str(weight).replace("[","").replace("]","").replace(",","")+"\n")

	def read_data(self):
		# try:
		for weight_layer in range(1, self.layer_count):
			with open("weight" + str(weight_layer) + ".txt", "r") as output_file:
				self.weights += [[]]
				for line in output_file:
					self.weights[weight_layer-1] += [[float(x) for x in line.split(" ")]]
		# except:
		# 	print "couldnt load in file"



class NN_translator(object):
	"""docstring for NN_translator"""
	def __init__(self, num_neurons_per_layer_, inputs_, outputs_):
		super(NN_translator, self).__init__()
		self.neural_net = Neural_Network(num_neurons_per_layer_)
		self.inputs = inputs_
		self.outputs = outputs_

	def train(self, input_data, output_data):
		input_bin = [1 if x in input_data else 0 for x in self.inputs]
		output_bin = [1 if x in output_data else 0 for x in self.outputs]
		network_error = self.neural_net.train(input_bin, output_bin)
		return [(self.outputs[i], network_error[i]) for i in range(len(self.outputs))]
	
	def get_output(self, input_data):
		input_bin = [1 if x in input_data else 0 for x in self.inputs]
		network_output =  self.neural_net.get_output(input_bin)
		return [(self.outputs[i], network_output[i]) for i in range(len(self.outputs))]

	def get_best_three(self, input_data):
		input_bin = [1 if x in input_data else 0 for x in self.inputs]
		network_output =  self.neural_net.get_output(input_bin)
		network_labeled_output = [(self.outputs[i], network_output[i]) for i in range(len(self.outputs))]
		bestscores = [-1,-1,-1]
		bestlabels = ['','','']
		for output in network_labeled_output:
			if(output[1] > bestscores[0]):
				bestscores = [output[1],bestscores[0],bestscores[1]]
				bestlabels = [output[0],bestlabels[0],bestlabels[1]]
			elif(output[1] > bestscores[1]):
				bestscores = [bestscores[0],output[1],bestscores[1]]
				bestlabels = [bestlabels[0],output[0],bestlabels[1]]
			elif(output[1] > bestscores[2]):
				bestscores = [bestscores[0],bestscores[1],output[1]]
				bestlabels = [bestlabels[0],bestlabels[1],output[0]]
		return bestlabels











