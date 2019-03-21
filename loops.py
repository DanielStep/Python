emails = ['me@gmail.com','you@hotmail.com','they@gmail.com']

for item in emails:
    if 'gmail' in item:
        print(item)


names=['james','john','jack']
email_domains=['gmail','hotmail','yahoo']

for i,j in zip(names, email_domains):
    print(i,j)