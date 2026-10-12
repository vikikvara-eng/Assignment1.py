name=input('enter yor name').strip().lower()
surname=input('enter your surname').strip().lower()
domain=input('enter your platphorm').strip().lower()
name_prefix =name [:2]
email =f"{name_prefix}{surname}@{domain}"
print (email)
print('\n\n your email has been successfully created')