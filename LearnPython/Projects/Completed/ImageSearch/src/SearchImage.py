import pandas as pd
import matplotlib.pyplot as plt 
import os
import matplotlib.image as mpimg


def load_pokemon_images():	
	dict = {}
	path = "../InputData/"

	for root, _, files in os.walk(path):		
		current_directory_path = os.path.abspath(root)
		for f in files:
			name, ext = os.path.splitext(f)
			if ext == ".png" or ext == ".jpg":
				current_image_path = os.path.join(current_directory_path, f)
				current_image = mpimg.imread(current_image_path)				
				dict[name] = current_image

	return dict

def create_and_disply_plot(img,spfs):
	plt.imshow(img)
	plt.text(83.4091,86.486,'Name: '+ str(spfs['Name'].iloc[0]))
	plt.text(83.4091,92.486,'Type1: '+ str(spfs['Type1'].iloc[0]))
	plt.text(83.4091,98.486,'Type2: '+ str(spfs['Type2'].iloc[0]))
	plt.title('Pokemon')	
	plt.show()


def display_pokemon():	
	images = load_pokemon_images()
	details =  pd.read_csv('..\\InputData\\pokemon.csv')
	pok_name = input("Enter Pokemon name\t")	
	spfs =details[details['Name']==pok_name]	
	try:		
		img = images[pok_name]		
	except:	
		print('Image Not found')
		exit(1)
	create_and_disply_plot(img,spfs)

if __name__ == '__main__':
	display_pokemon()

