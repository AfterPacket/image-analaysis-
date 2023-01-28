import cv2
import exifread
from geopy.geocoders import Nominatim
from PIL import Image

# Open the image
img = cv2.imread('image.jpg')

# Extract EXIF data
with open('image.jpg', 'rb') as f:
    tags = exifread.process_file(f)

# Get GPS coordinates from EXIF data
lat = tags['GPS GPSLatitude'].values
lon = tags['GPS GPSLongitude'].values

# Convert coordinates to decimal format
lat_dec = convert_to_degrees(lat)
lon_dec = convert_to_degrees(lon)

# Use Geopy to reverse geocode the coordinates
geolocator = Nominatim(user_agent="image_locator")
location = geolocator.reverse(f'{lat_dec}, {lon_dec}')

# Print location
print(location.address)
