from fastapi import APIRouter, Body, Response
from Server.db import conn
from Utils.auth import gen_token
from App.v1.user.user_model import User
from Utils.crypt import comparePass, encrypt_pass

base = '/users'

user = APIRouter()

@user.post(base + '/signin')
async def signin(user: dict = Body(...)):
  try:
    user_find = conn.BohemiaDatabase.users.find_one({"username": user['username']})
    if user_find is not None:
      isMatch = comparePass(user['password'], user_find['password'])
      token = gen_token({'id': str(user_find['_id'])})
      if isMatch:
       return Response(status_code=200, content="User logged in", headers={"Authorization": token})
    return Response(status_code=404, content="Las credenciales ingresadas no son validas")
  except:
    return Response(status_code=500, content="Internal server error")


@user.post(base + '/signup')
async def signup(user: User = Body(...)):
  user.password = encrypt_pass(user.password)
  user.status = 'active'
  try:
    conn.BohemiaDatabase.users.insert_one(dict(user))
    return Response(status_code=200, content="User created")
  except:
    return Response(status_code=500, content="Internal server error")