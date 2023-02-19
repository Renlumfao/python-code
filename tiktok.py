import requests

url = "https://scraptik.p.rapidapi.com/list-followers"

querystring = {"user_id":"7072823865591759878","count":"10","max_time":"0"}

headers = {
	"X-RapidAPI-Key": "API-KEY",
	"X-RapidAPI-Host": "scraptik.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)