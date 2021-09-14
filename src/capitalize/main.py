def capit(target : str) -> str:
	return target.upper()

def cli_main():
	from sys import argv
	if len(argv) > 1:
		print(capit(argv[1]))
	else:
		print("Usage: capitalize ['target']")
