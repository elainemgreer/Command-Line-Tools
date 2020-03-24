import click
import requests

api_key = 'b9469532f9cc5a05bd1611cd5aba402a'


def current_weather(location, api_key=api_key):

    request_string = (f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}')

    # payload = {'appid': api_key,
    #         'q': location}

    response = requests.get(request_string)
    response = response.json()
    

    weather = response['weather'][0]['description']

    return weather



@click.command()
@click.argument('location')
def main(location):
    weather = current_weather(location)
    print(f'The weather in {location} right now is {weather}!')

    if 'rain' in weather:
        print(f'Wear a raincoat!')


if __name__ == "__main__":
    main()