from datetime import datetime
import os

from enum import Enum
from functools import partial
from gtts import gTTS
from pathlib import Path
from playsound import playsound
import speech_recognition as sr

from generate_audio_file import generate_audio_file_from_text


class QueryOptions(Enum):
  today = "today"
  different_day = "different day"
  current_time = "current"
  different_time = "different time"
  query_again = "yes"
  do_not_query_again = "no"



def play_common_response_and_get_input(response_type, audio_source, recognizer):
  play_common_response(response_type)
  return listen_and_transcribe(audio_source, recognizer)


def play_common_response_and_get_expected_input(
  response_type, expected_inputs, audio_source, recognizer
):
  play_common_response(response_type)
  return get_expected_input(expected_inputs, audio_source, recognizer)


def ask_name(audio_source, recognizer):
  return play_common_response_and_get_input(
    ResponseTypes.ask_name, audio_source, recognizer
  )


def ask_today_or_not(audio_source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_today_or_not,
    [QueryOptions.today.value, QueryOptions.different_day.value],
    audio_source,
    recognizer,
  )


def ask_current_or_not(audio_source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_current_or_not,
    [QueryOptions.current_time.value, QueryOptions.different_time.value],
    audio_source,
    recognizer,
  )


def ask_how_many_hours(audio_source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_how_many_hours,
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
    audio_source,
    recognizer,
  )


def ask_how_many_days(audio_source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_how_many_days,
    ["1", "2", "3", "4", "5", "6", "7"],
    audio_source,
    recognizer,
  )


def ask_if_query_again(audio_source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_if_query_again,
    [QueryOptions.query_again.value, QueryOptions.do_not_query_again.value],
    audio_source,
    recognizer,
  )


def respond_dynamically(text):
  # TODO: Make this work using tempfile instead.

  file_name = f"temp_audio_file_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"
  file_path = generate_audio_file_from_text(text, file_name, common=False)
  playsound(file_path)
  os.remove(file_path)


def greet(name):
  respond_dynamically(f"Nice to meet you {name}!")


def report_current_weather(temp, feels_like):
  respond_dynamically(
    f"The current temperature is {temp} degrees celcius and feels like "
    f"{feels_like} degrees celcius."
  )


def report_weather_for_later_time(temp, feels_like):
  respond_dynamically(
    f"The temperature at the time that you requested will be {temp} degrees "
    f"celcius, and it will feel like {feels_like} degrees celcius."
  )


def report_weather_for_later_day(
  temp_day, temp_eve, feels_like_day, feels_like_eve
):
  respond_dynamically(
    f"The temperature on the day that you requested will be {temp_day} "
    f"degrees celcius in the day time and {temp_eve} in the evening. It will "
    f"feel like {feels_like_day} degrees celcius in the day time and "
    f"{feels_like_eve} in the evening."
  )
