RESULT_NAME = "hfble.py"
PLATFORM_DEP_CODE = {
	"l":"import os\ndef clear():\n\tos.system(\"clear\")\n\n",
	"w":"import os\ndef clear():\n\tos.system(\"cls\")\n\n",
	"r":"import replit\nclear = replit.clear\n\n"
}
initialName = input("Enter the name of the initial file (enter nothing for the default, 'main.py'): ")
initialName = "main.py" if initialName.lower().strip() == "" else initialName
platform = "a"
try:
	while platform.strip().lower()[0] not in "mlwr":
		platform = input("What OS is this to be installed on? MacOS/(L)inux (default), (W)indows, or non-explorer (R)eplit? ")
except IndexError:
	platform = "l"
platform = "l" if platform.strip().lower()[0] in "ml" else platform.strip().lower()[0]
try:
	f = open(initialName, "r")
	original = f.read()
	f.close()
	f = open(RESULT_NAME, "w+")
	f.write(PLATFORM_DEP_CODE[platform] + original)
	f.close()
	del original
	print("Setup complete.")
except FileNotFoundError:
	input("The initial file you submitted does not exist.\nPress enter to continue. ")
finally:
	f.close()
