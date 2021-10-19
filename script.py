from playsound import playsound
import os
import pandas as pd

path = "audio/" # path to the dataset
files = os.listdir(path)

df = pd.DataFrame([], columns = ['file_name', 'label'])

for file, i in zip(files, range(len(files))):
	print("Currently playing " + file)
	playsound(path + file)
	label = input("Please, provide the label(n for noisy and c for clean audio files): ")
	while(label != 'c' and label != "n"):
		label = input("Provided label is neither n nor c. Try again... ")
	df.loc[i] = [file, label]

df.to_json("data.json", orient = 'records')
