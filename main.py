def make(address, project_name, project_lang):
	import os
	import os.path as pt

	prog_langs = {"c":".c", "c++":"cpp", "python":".py", "lua":".lua", "ruby":".rb", "c#":".cs", "java":".java", "php":".php"}

	if not pt.exists(address):
		os.mkdir(address)

	os.mkdir("/".join([address, project_name]))
	os.chdir("/".join([address, project_name]))

	with open("main"+prog_langs[project_lang], "w") as f:
		f.write("")

if __name__ == '__main__':
	address = input("Enter path for your project:\n")
	project_name = input("Enter name of your project:\n")
	project_lang = input("Enter programming language of your project(c, c++, python, lua, ruby, c#, java, php):\n")
	make(address, project_name, project_lang)