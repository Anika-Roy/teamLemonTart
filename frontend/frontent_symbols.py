# List of cities supported by OpenWeatherAPI and their names
CITY_LIST = [
    "London",
    "Paris",
    "New York",
    "Tokyo",
    "Berlin",
    "Sydney",
    "Rome",
    "Moscow",
    "Cairo",
    "Toronto",
    "Rio de Janeiro",
    "Mumbai",
    "Beijing",
    "Dubai",
    "Amsterdam",
    "Barcelona",
    "Bangkok",
    "Los Angeles",
    "Istanbul",
    "Singapore",
    "Vienna",
    "Athens",
    "Prague",
    "Stockholm",
    "Cape Town",
    "Havana",
    "Buenos Aires",
    "Zurich",
    "Seoul",
    "Mexico City",
    "Helsinki",
    "Dublin",
    "San Francisco",
    "Madrid",
    "Florence",
    "Lisbon",
    "Copenhagen",
    "Osaka",
    "Vancouver",
    "Edinburgh",
    "Kuala Lumpur",
    "Warsaw",
    "Budapest",
    "Marrakech",
    "Johannesburg",
    "Vienna",
    "Prague",
    "Toronto",
    "Zurich",
    "Stockholm",
    "Seoul",
    "São Paulo",
    "Shanghai"
]
WIND_DIRECTION = [
    "↓", "↙", "←", "↖", "↑", "↗", "→", "↘",
]

# # List of cities supported by OpenWeatherAPI and their names
# CITY_LIST = [
#     "London",
#     "Paris",
#     "New York"
# ]

# List of symbols to pretty print for weather conditions
# Credits to : https://github.com/chubin/wttr.in
WEATHER_SYMBOL = {
    "Unknown": [
        "    .-.      ",
        "     __)     ",
        "    (        ",
        "     `-’     ",
        "      •      "],
    "clear sky": [
        "\033[38;5;226m    \\   /    \033[0m",
        "\033[38;5;226m     .-.     \033[0m",
        "\033[38;5;226m  ― (   ) ―  \033[0m",
        "\033[38;5;226m     `-’     \033[0m",
        "\033[38;5;226m    /   \\    \033[0m"],
    "few clouds": [
        "\033[38;5;226m   \\  /\033[0m      ",
        "\033[38;5;226m _ /\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m   \\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "             "],
    "scattered clouds": [
        "             ",
        "\033[38;5;250m     .--.    \033[0m",
        "\033[38;5;250m  .-(    ).  \033[0m",
        "\033[38;5;250m (___.__)__) \033[0m",
        "             "],
    "broken clouds": [
        "             ",
        "\033[38;5;240;1m     .--.    \033[0m",
        "\033[38;5;240;1m  .-(    ).  \033[0m",
        "\033[38;5;240;1m (___.__)__) \033[0m",
        "             "],
    "shower rain": [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;111m     ‘ ‘ ‘ ‘ \033[0m",
        "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m"],
    "rain": [
        "\033[38;5;240;1m     .-.     \033[0m",
        "\033[38;5;240;1m    (   ).   \033[0m",
        "\033[38;5;240;1m   (___(__)  \033[0m",
        "\033[38;5;21;1m  ‚‘‚‘‚‘‚‘   \033[0m",
        "\033[38;5;21;1m  ‚’‚’‚’‚’   \033[0m"],
    "thunderstorm": [
        "\033[38;5;240;1m     .-.     \033[0m",
        "\033[38;5;240;1m    (   ).   \033[0m",
        "\033[38;5;240;1m   (___(__)  \033[0m",
        "\033[38;5;21;1m  ‚‘\033[38;5;228;5m⚡\033[38;5;21;25m‘‚\033[38;5;228;5m⚡\033[38;5;21;25m‚‘ \033[0m",
        "\033[38;5;21;1m  ‚’‚’\033[38;5;228;5m⚡\033[38;5;21;25m’‚’  \033[0m"],
    "snow": [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;255m     *  *  * \033[0m",
        "\033[38;5;255m    *  *  *  \033[0m"],
    "mist": [
        "             ",
        "\033[38;5;251m _ - _ - _ - \033[0m",
        "\033[38;5;251m  _ - _ - _  \033[0m",
        "\033[38;5;251m _ - _ - _ - \033[0m",
        "             "],
}

ICON_CODE_MAPPING={
    "01d":"clear sky",
    "01n":"clear sky",
    "02d":"few clouds",
    "02n":"few clouds",
    "03d":"scattered clouds",
    "03n":"scattered clouds",
    "04d": "broken clouds",
    "04n":"broken clouds",
    "09d": "shower rain",
    "09n": "shower rain",
    "10d":"rain",
    "10n": "rain",
    "11d": "thunderstorm",
    "11n":" thunderstorm",
    "13d":"snow",
    "13n":  "snow",
    "50d":  "mist",
    "50n":  "mist"
}
