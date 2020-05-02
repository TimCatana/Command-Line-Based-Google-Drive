from pydrive.auth import GoogleAuth

# Authenticates the account you want to work with
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

from pydrive.drive import GoogleDrive
drive = GoogleDrive(gauth)

# Print file names with ID's
def list(ID):
	file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(ID)}).GetList() # Query the given location
	
	print('\nQUERY RESULTS\n--------------------')
	print('querying file ID: {}\n'.format(ID))
	for file in file_list:
	    print('title: %s || extension: %s || id: %s' % (file['title'], file['mimeType'].rsplit('.', 1)[-1], file['id']))
	print('--------------------------------------------------------\n')
	
# Create a File	
def createFile():
	fName = input('Insert file name: ')
	print('file types: "folder", "document", "presentation", "drawing", "spreadsheet", "form", "map", "site", "script", "jam"')
	fType = input('Insert file type): ')
	
	while checkfType(fType) == False:
		fType = input('Insert a valid file type(see "file types" document for examples): ')
	file = drive.CreateFile({'title': fName, "mimeType": "application/vnd.google-apps.{}".format(fType)})
	file.Upload()
	
	print('\nCREATED FILE\n--------------------')
	print('title: %s || extension: %s || id: %s' % (file['title'], file['mimeType'].rsplit('.', 1)[-1], file['id']))
	print('--------------------------------------------------------\n')

# Checks if the user inputted a valid file type to create
def checkfType(fType):
	if fType == 'folder' or fType == 'document' or fType == 'presentation' or fType == 'drawing' or  fType == 'spreadsheet':
	    return True
	elif fType == 'form' or fType == 'map' or  fType == 'site' or fType == 'script'  or fType == 'jam': 
		return True
	else: 
		return False
		
# Removes a file given an ID
def removeFile(ID):
	file = drive.CreateFile({'id': '{}'.format(ID)})
	file.Trash()
	
# Print the command list to the terminal
def printCommands():
	print('\nCOMMANDS\n--------------------')
	print('list : Query a folder (will list nothing if file is not a folder)')
	print('query type : List all files of a given file type (folder, map, etc...)')
	print('create : Create a file')
	print('remove : Remove a file')
	print('exit : Terminate the program')
	print('--------------------------------------------------------\n')
	
# List all files with a specific file type
def listSpecFile():
	print('file types: "folder", "document", "presentation", "drawing", "spreadsheet", "form", "map", "site", "script", "jam"')
	fType = input('Insert file type (see "file types" document for examples): ')
	while checkfType(fType) == False:
		fType = input('Insert a valid file type: ')
	
	print('This may take a while...')
	print('\n listing all "{}" file types\n--------------------'.format(fType))
	queryFileType('root', fType)
	print('--------------------------------------------------------\n')
	
# Initialize a csv file at the beginning of the program
def queryFileType(ID, fType): # ID = 'root' when ralled 
	folderNames = []
	folderIDs = []
	
	file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(ID)}).GetList()
	for file in file_list:
		if file['mimeType'] == 'application/vnd.google-apps.{}'.format(fType):
			print('title: %s || extension: %s || id: %s' % (file['title'], file['mimeType'].rsplit('.', 1)[-1], file['id']))
			
	for file in file_list:
		queryFileType(file['id'], fType)

		

run = True
ID = 'root'
print('Initializing Program...')
list(ID) # query root at the beginning

# Continue until user wants to exit
while run:
	comm = input('what do you want to do? Insert "help" for list of commands: ')
	
	if comm == 'list':
		ID = input('Insert File ID to query (insert "root" to query home: ')
		list(ID)
	elif comm == 'create':
		createFile()
	elif comm == 'remove':
		ID = input('Insert File ID to remove: ')
		removeFile(ID)
	elif comm == 'query type':
		listSpecFile()
	elif comm == 'help':
		printCommands()
	elif comm == 'exit':
		run = False
	else:
		print('Invalid Command')
		
		
		
		







### Etra experamental stuff ###

#import os
#import csv


# Initialize a csv file at the beginning of the program
#def initializeCSV(ID): # ID = 'root' when ralled 
#	folderNames = []
#	folderIDs = []
	
#	file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(ID)}).GetList()
#	for file in file_list:
#		if file['mimeType'] == 'application/vnd.google-apps.folder':
#			folderIDs.append(file['id'])
#			folderNames.append(file['title'])
	
#	with open('Folders.csv', 'a+', newline='') as file:
#		writer = csv.writer(file)
#		for i in range(len(folderNames)):
#			writer.writerow([folderNames[i], folderIDs[i]])
			
	#for file in file_list:
	#	initializeCSV(file['id'])
		
			
#with open("Folders.csv", "w") as file:
	#writer = csv.writer(file)
	#writer.writerow(["Title", "ID"])
	
# initializeCSV(ID)

#os.remove('Folders.csv')