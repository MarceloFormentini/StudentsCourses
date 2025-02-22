class MinhaClasse:
	def __enter__(self):
		print('Entrando')

	def __exit__(self, exc_type, exc_value, traceback):
		print('Saindo')

with MinhaClasse() as mc:
	print('Dentro do bloco with')