# https://dev.to/thepracticaldev/daily-challenge-224-password-validator-7if

'''
Write a quick password validator to make sure that the people that visit your site use appropriate passwords.
Respond with "VALID" if the string meets the requirements or "INVALID" if it does not.

Requirements:
More than 3 characters but less than 20.
Must contain only alphanumeric characters.
Must contain letters and numbers.

Examples
'Username123!' => INVALID
'123' => INVALID
'Username123' => VALID
'''

var = input("Enter the password: ")
aflag = 0
nflag = 0
sflag = 0

if len(var) < 4 or len(var) > 19:
	print("INNVALID")
else:
	for i in var:
		if i.isalpha():
			aflag += 1
		elif i.isnumeric():
			nflag += 1
		else:
			sflag += 1
			break

	if aflag == 0 or nflag == 0 or sflag != 0:
		print("INVALID")
	else:
		print("VALID")
