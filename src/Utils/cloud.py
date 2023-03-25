import cloudinary
import cloudinary.uploader
from Config.config import cloud_config

cloudinary.config(
  cloud_name = cloud_config["cloud_name"],
  api_key = cloud_config["api_key"],
  api_secret = cloud_config["api_secret"]
)

def upload_image(image_route: str):
    return cloudinary.uploader.upload(image_route)

def delete_image(public_id: str):
    return cloudinary.uploader.destroy(public_id)