# hfble

# A login engine

# Classes:


## `LoginEngine(object)`
The objects have an attribute `db` which is intended to store a list of dicts, in which each dict has items with keys of "username" (storing a string - the username), "salt" (storing a string - the salt), "hashedPassword" (storing a string - the password, salted and hashed), and "extra" (storing a tuple - user's data).

### `NoneType __init__()`
Basic constructor, initializing some variables.

### `str SaltGen()`
Generates a salt suitable for the hashing algorithm.

### `str Encrypt(str content)`
Runs the SHA512 hashing algorithm using `content`.

### `int AccountFind(str username)`
Searches through the loaded database for account data with a username equal to `username`. Returns the index of it if it is found; if it is not found, it returns -1.

### `str Login(str username, str password)`
Attempts to log in using the loaded database - returns a status string according to what happened with that - out of the self-explanatory set of "SuccessfulLogin", "IncorrectPassword", and "UserDoesNotExists".

### `str Register(str username, str password, str|list UNprohibited, tuple extra)`
Attempts to register an account into the database with the data as given in the arguments - `UNprohibited` defines what characters are not allowed in usernames, `extra` contains the user data to store with the account. It returns a status string according to what happened out of the self-explanatory set of "SuccessfulRegister", "UsernameTaken", "EmptyUsername", and "InvalidCharInUsername".

### `str ChangePassword(str username, str oldPassword, str newPassword)`
Attempts to change the password associated with the account specified by `username` to `newPassword`, but will only work if `oldPassword` is the correct current password. It returns a self-explanatory status string out of "InvalidLogin", "SuccessfulPasswordChange". It also generates a new salt when changing the password.


## `LoginConsoleInteractivity(LoginEngine)`
The objects have an attribute `account` which is intended to store either a `NoneType` meaning that they are not logged in or a `str` representing the name of the account that they are logged into. In all of the UI functions, after the user finishes, it calls into `UIMain`.

### `NoneType __init__(str|list UNrestrict)`
Basic constructor, calling the parent constructor and initializing some variables.

### `NoneType UILogin(bool v=False)`
Gives a console-based interface allowing a user to attempt to login, setting the attribute `account` in the process. `v` controls whether or not to output some extra \[debugging\] information that should not be shown in a production system.

### `NoneType UIRegister(bool v=False)`
Gives a console-based interface allowing a user to attempt to register an account, editing the attribute `db` in the process. `v` controls whether or not to output some extra \[debugging\] information that should not be shown in a production system.

### `NoneType UIReadData(bool v=False)`
Gives a console-based interface allowing a user to read the data associated with the account that they are logged in as. `v` controls whether or not to output some extra \[debugging\] information that should not be shown in a production system.

### `NoneType UIWriteData(bool v=False)`
Gives a console-based interface allowing a user to attempt to edit an item in the data associated with the account that they are logged in as. `v` controls whether or not to output some extra \[debugging\] information that should not be shown in a production system.

### `NoneType UIAppendData(bool v=False)`
Gives a console-based interface allowing a user to attempt to append an item to the list of data items associated with the account that they are logged in as. `v` controls whether or not to output some extra \[debugging\] information that should not be shown in a production system.

### `NoneType UIChangePassword(bool v=False)`
Gives a console-based interface allowing a user to attempt to change the password stored (in salted+hashed form, of course) in the database associated with their account (but only if they correctly enter the old password). `v` controls whether or not to output some extra \[debugging\] information that should not be shown in a production system.

### `NoneType UIMain(bool v=False)`
Gives a console-based interface allowing a user to access the other `UI...` functions, or to exit the function. When other `UI...` functions are exited, it returns to this one. `v` controls whether or not to output some extra \[debugging\] information that should not be shown in a production system.


## `SaveManagerText()`
The RW format of this Save Manager is equivalent to the recommended format for `LoginEngine.db`.

### `NoneType __init__(str filename)`
Basic constructor, initializing some variables. `filename` is the name of the file it manages (should have a suffix of .txt, .dat, or, most preferably, .login). During the contsructor, it tests if the file with the name `filename` exists with try/finally.

### `list Read()`
Reads from the object-associated file, returning the contents as a list in the format as is intended for `LoginEngine.db`.

### `NoneType Write(list db)`
Writes the database \[assuming it is in the format appropriate for `LoginEngine.db`\] to the object-associated file, in a way that is compatible with `SaveManagerText.Read`.
