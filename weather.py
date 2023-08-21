# Made By Ali Hany 8/21/2023 
# Import Needed Libary's
import python_weather as pyw ,asyncio,requests,os,time
from ip2geotools.databases.noncommercial import DbIpCity
# Variables
os.system("color 5") # Console Color
os.system("cls") # Clear Console
# Get Local Area
ip = requests.get("https://api.ipify.org").content.decode("utf8")
city = DbIpCity.get(ip,api_key="free").country
# Functions
async def weather_info():
    async with pyw.Client() as client:
        weather = await client.get(city)
        info = f"""
{"-"*10}{city.upper()}{"-"*10} 
 Temperature: {weather.current.temperature}-C
 Wind Speed: {weather.current.wind_speed}
 Wind Direction: {weather.current.wind_direction}
{"-"*(20+len(city))}
"""
        print(info,end="\r",flush = True)
        time.sleep(60) # Refreshing Every Mintue
        os.system("cls")
while True:
    asyncio.run(weather_info())
