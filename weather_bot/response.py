from enum import Enum


class ResponseTypes(Enum):
  ask_how_many_days = "ask_how_many_days"
  ask_how_many_hours = "ask_how_many_hours"
  ask_if_current_time = "ask_if_current_time"
  ask_if_query_again = "ask_if_query_again"
  ask_if_today = "ask_if_today"
  ask_name = "ask_name"
  goodbye = "goodbye"
  hello = "hello"
  invalid_input = "invalid_input"
  pardon = "pardon"


RESPONSE_FILES = {
  ResponseTypes.ask_how_many_days: "ask_how_many_days.mp3",
  ResponseTypes.ask_how_many_hours: "ask_how_many_hours.mp3",
  ResponseTypes.ask_if_current_time: "ask_if_current_time.mp3",
  ResponseTypes.ask_if_query_again: "ask_if_query_again.mp3",
  ResponseTypes.ask_if_today: "ask_if_today.mp3",
  ResponseTypes.ask_name: "ask_name.mp3",
  ResponseTypes.goodbye: "goodbye.mp3",
  ResponseTypes.hello: "hello.mp3",
  ResponseTypes.invalid_input: "invalid_input.mp3",
  ResponseTypes.pardon: "pardon.mp3",
}


def play_common_response(response_type):
  file_path = os.path.join(
    Path().absolute(),
    "weather_bot",
    "media",
    "common_responses",
    RESPONSE_FILES[response_type],
  )
  playsound(file_path)


beg_pardon = partial(play_common_response, response_type=ResponseTypes.pardon)
flag_invalid_input = partial(
  play_common_response, response_type=ResponseTypes.invalid_input
)
say_goodbye = partial(play_common_response, response_type=ResponseTypes.goodbye)
say_hello = partial(play_common_response, response_type=ResponseTypes.hello)
