from src import client

class ClientInterface:
	def __init__(self):
		self.active = True

		self.commands = {}
		self.commands["help"] = self.help
		self.commands["exit"] = self.exit
		self.commands["register"] = self.register

	def exit(self):
		self.active = False
	def help(self):
		print("help: Display this")
		print("exit: Exit")
		print("register: Register new client")
	def register(self):
		print("Registering new client...")
		first_name = input("First name: ")
		last_name = input("Last name: ")
		email = input("Email: ")
		city = input("City: ")
		street = input("Street: ")
		house_number = input("House number: ")
		additional = input("Additional address info (can be blank): ")
		if additional == "":
			additional = None
		c = client.Client.register(first_name, last_name, email, city, street, house_number, additional)
		print("Registered new client with number", c.client_number)

	def start(self):
		self.active = True
		print("Client manager")
		print("Enter \"help\" to get started ;)")
		while self.active:
			try:
				cmd = input("client: ")
				if cmd in self.commands:
					self.commands[cmd]()
				else:
					print("Unknown command")
			except EOFError:
				self.active = False
			except Exception as error:
				print("Error:", error)
		print()