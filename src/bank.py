import random, csv
from src import addressdao, bankdao

class Bank:
	def __init__(self, bankdao, addressdao):
		self.bank_number = bankdao.bank_number
		self.city = addressdao.city
		self.street = addressdao.street
		self.house_number = addressdao.house_number
		self.additional = addressdao.additional

	def __str__(self):
		return self.bank_number + ": " + self.street + " " + self.house_number + ", " + self.city + (": " + self.additional if self.additional != None else "")

	@classmethod
	def register(cls, city, street, house_number, additional=None):
		if not isinstance(city, str):
			raise TypeError("City must be a string")
		if not isinstance(house_number, str):
			raise TypeError("House number must be a string")
		if not isinstance(additional, str) and additional != None:
			raise TypeError("Additional address info must be a string or empty")
		if len(city) <= 0:
			raise ValueError("City cannot be empty")
		if len(street) <= 0:
			raise ValueError("Street cannot be empty")
		if len(house_number) <= 0:
			raise ValueError("House number cannot be empty")
		address = addressdao.AddressDAO(0, city, street, house_number, additional)
		address = addressdao.AddressDAO.create(address)
		bank = bankdao.BankDAO(0, address.id, str(random.randint(100000000000, 999999999999)))
		bank = bankdao.BankDAO.create(bank)
		return cls(bank, address)
	@classmethod
	def list(cls):
		banks = bankdao.BankDAO.readAll()
		res = []
		for b in banks:
			res.append(cls(b, addressdao.AddressDAO.read(b.address_id)))
		return res
	@classmethod
	def importCSV(cls, filepath):
		counter = 0
		with open(filepath, newline="") as file:
			reader = csv.reader(file, delimiter=",", quotechar="\"")
			for row in reader:
				if len(row) != 4:
					raise ValueError("Malformed CSV; must be like city,street,house_number,additional")
				if row[3] == "":
					row[3] = None
				cls.register(row[0], row[1], row[2], row[3])
				counter += 1
		return counter