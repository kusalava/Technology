import pandas as pd 
import numpy as np 

def read_data():	
	dataset = pd.read_csv("../InputData/height_weight_data.csv")
	#pd.set_option('display.expand_frame_repr', False)
	return dataset

def get_gender(x):
	if x=='F':
		return 'Female'
	if x=='M':
		return 'Male'


def validate_input(x,height):
	while x != 'M' and x!='F' or height > 90:
		if x != 'M' and x!='F':			
			print('Wrong Gender\nPlease enter correcet Gender')
			x = input()
		if height > 90:
			print('Wrong Height\nPlease enter correcet Height (in Inches)')
			height = float(input())
	return get_gender(x),np.ceil(height)


def convert_string_to_values(dataset):
	dataset.Height = dataset.Height.astype(float).fillna(0.0)
	dataset.Weight = dataset.Weight.astype(float).fillna(0.0)
	dataset.Height = np.ceil(dataset.Height)
	dataset.Weight = np.ceil(dataset.Weight)	

def process_data(dataset,gender,height):
	data = dataset[dataset['Gender']== gender]		
	selected_data = data[data['Height'] == height]
	if not selected_data.empty:
			return selected_data
	j=0
	while j<6:
		j+=1
		selected_data = fetch_data(data,selected_data,height,0,j)
		selected_data = fetch_data(data,selected_data,height,1,j)
		if not selected_data.empty:
			return selected_data
	print('Not able to predict, More data is required')
	print('## Program terminating abnormally')
	exit(1)

def fetch_data(data,selected_data,height,val,index):
	num = height	
	j = 0
	if not selected_data.empty and index!=6:		
		if val == 0:
			num -= index
		else:
			num += index		
		selected_data = data[data['Height'] == num]		
	return selected_data


def get_result(selected_data):
	mean = np.mean(selected_data['Weight'])		
	print('Your predicted ' + selected_data['Gender'].iloc[0] + ' Weight is %.2f  (in Pounds)' %mean)


if __name__ == '__main__':
	print("Enter Gender 'F' for Female\nEnetr Gender 'M' for Male\nEnter Height (in Inches)",sep='')
	try:
		x,height = input(),float(input())
	except:
		print('Wrong Details Try Again')
		print('####### Program Terminating #######')
		exit(1)
	gender,height = validate_input(x,height)
	dataset = read_data()
	#print(dataset)
	convert_string_to_values(dataset)
	#print(dataset)
	selected_data = process_data(dataset,gender,height)
	#print(selected_data)
	get_result(selected_data)