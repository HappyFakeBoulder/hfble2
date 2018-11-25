f = open("README.txt", "r")
__import__("distutils").core.setup(name="hfble", version="2.0", packages=["hfble"], license="MIT License", long_description=(f.read(), f.close())[0])
