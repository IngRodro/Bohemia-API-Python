import bcrypt

def encrypt_pass(password: str):
  salt = bcrypt.gensalt()
  hash = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
  return hash

def comparePass(password: str, hash: str):
  result = bcrypt.checkpw(password.encode('utf-8'), hash.encode('utf-8'))
  return result
