import pickle

key = input("Key:")
secret = input("Secret")

mycred = {'key':key, 'secret':secret.encode('UTF-8')}

with open('cred.pkl', 'wb') as file:      
    # A new file will be created
    pickle.dump(mycred, file)

print("cre.pkl created")