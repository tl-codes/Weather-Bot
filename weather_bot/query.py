from enum import Enum

from api import (
  extract_weather_data_for_later_day,
  extract_weather_data_for_later_time,
)
from response import (
  report_current_weather,
  report_weather_for_later_day,
  report_weather_for_later_time,
)


class QueryOptions(Enum):
  today = "today"
  different_day = "different day"
  current_time = "current"
  different_time = "different time"
  query_again = "yes"
  do_not_query_again = "no"


def query_current_weather(data):
  report_current_weather(data["current"]["temp"])


def query_weather_for_later_time(call_dt, data, num_of_hours):
  data = extract_weather_data_for_later_time(call_dt, data, num_of_hours)
  report_weather_for_later_time(data["temp"])


def query_weather_for_later_day(call_dt, data, num_of_days):
  temp = extract_weather_data_for_later_day(call_dt, data, num_of_days)["temp"]
  report_weather_for_later_day(temp["day"], temp["eve"])