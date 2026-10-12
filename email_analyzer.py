import re
text = ('ouar group members is : saba.ananidze@itstep.com,dima123@gmail.com,test_user@yahoo.com')
email = re.findall (r"\S+@\S+",text)
print(email)
result=email [0]+"+"+ email [1]
print(result)