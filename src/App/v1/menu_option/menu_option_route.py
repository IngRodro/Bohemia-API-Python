from fastapi import APIRouter, Response
from Server.db import conn
from App.v1.menu_option.menu_option_model import MenuOption
from App.v1.menu_option.menu_option_schema import menu_option_entity, menu_options_entity, menu_option_pipeline

menu_option = APIRouter()
base = '/menu_option'

@menu_option.get(base + '/{id_restaurant}')
async def get_menu_option(id_restaurant: str):
  try:
    menu_options = conn.BohemiaDatabase.menus.find()
    results = menu_options_entity(menu_options)
    return Response(status_code=200, content=results)
  except Exception as e:
    return Response(status_code=500, content=str(e))

