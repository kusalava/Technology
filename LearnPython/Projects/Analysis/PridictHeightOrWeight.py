import numpy as np 
import pandas as pd 
import math
import matplotlib.pyplot as plt
import csv

def read_data():	
	dataset = pd.read_csv("..\\DataSets\\height_weight_data.csv")
	pd.set_option('display.expand_frame_repr', False)
	return dataset

def create_plots(dataset):
	x = dataset['Height']
	y = dataset['Weight']
	plt.plot(x,y)
	plt.show()

def write_csv(female,male):
	zip(female,male)
	help(zip)
	myFile = open('data.csv','w',newline='')
	with myFile:
		writer = csv.writer(myFile,delimiter=',')	
		writer.writerows(zip(female))
		writer.writerows(zip(male))

		#writer.writerow(male)

			
				
		
		
if __name__ == '__main__':
	'''dataset = read_data()
	create_plots(dataset)

	#print(dataset)
	#asd = dataset.groupby('Index').aggregate(np.mean)
	print(dataset[['Index','Height']],)'''
	female ,male= [],[]
	for i in range(12500):		
		female.append('Female')
		male.append('Male')	

	write_csv(female,male)