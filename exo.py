def lister_todos():
print('Fonctionnalité "lister les todos" à venir')
# Fonction pour créer un todo - à réaliser
def creer_todo():
print('Fonctionnalité "créer un todo" à venir')
# Menu principal
choix = ''
while choix != 'q':
	# Affichage des choix
	print('\n==== Menu principal ====')
	print('1: Lister les todos')
	print('2: Créer un todo')	
	# Actions suivant le choix
	choix = input('=> Choix : ')
	match choix:
		case '1': lister_todos()
		case '2': creer_todo()
