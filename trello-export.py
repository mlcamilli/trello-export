import os, sys, argparse, json, csv



def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("inputfile", help="the json file containing trello board data")
	parser.add_argument("--outputfile", help="the json file containing trello board data")
	args = parser.parse_args()
	f = open(args.inputfile)
	json_object = json.load(f)
	print_cards(json_object, args.outputfile)
	


def print_cards(json_object, outputfile):
	
	def checklist_data(card):
		if len(card['idChecklists']) > 0:
			checklist_id = card['idChecklists'][0]
		else:
			return ''
		checklists = sorted(json_object['checklists'], key=lambda k: k['id'])
		checklist = {}
		for check in checklists:
			if check['id'] == checklist_id:
				checklist = check
				break
		string = ''
		for item in checklist['checkItems']:
			string += item['name'] + '\n'
		return string[:-1] 

	def labels(card):
		label = ''
		for lbl in card['labels']:
			label += lbl['name'] + '\n'
		return label[:-1] 
	def members(card):
		member_string = ''
		for member in card['idMembers']:
			for member_obj in json_object['members']:
				if member_obj['id'] == member:
					member_string += member_obj['fullName'] + '\n'
					break
		return member_string[:-1]



	cards = sorted(json_object['cards'], key=lambda k: k['idShort'])
	if outputfile != None:
		filename = outputfile
	else:
		filename = 'output.csv'
	with open(filename, 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['ID', 'Story', 'Description', 'Checklist', 'Labels', 'Due Date', 'Members'])
		for card in cards:
			writer.writerow([card['idShort'], card['name'],
				card['desc'], checklist_data(card), labels(card), card['due'], members(card)]) 

	



if __name__ == "__main__":
	main()