TEMPLATE_FILE = "./Input/Letters/starting_letter.txt"
NAMES_FILE = "./Input/Names/invited_names.txt"
OUTPUT_FOLDER = "./Output/ReadyToSend/"

with open(NAMES_FILE, mode="r") as file:
  names = file.read()

with open(TEMPLATE_FILE, mode="r") as file:
  template = file.read()

names = names.split() 

for name in names:
  filename = OUTPUT_FOLDER + "letter_for_"+ name + ".txt"
  text = template.replace('[name]',name)
  with open(filename, mode="w") as file:
    file.write(text)
