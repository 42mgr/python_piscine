import time

try:
    epoch_seconds = round(time.time(), 4)
    epoch_seconds_formatted = "{:,}".format(epoch_seconds)
    epoch_seconds_scientific = "{:.2e}".format(epoch_seconds)

    string_time = time.strftime("%b %d %Y", time.localtime())

    print(
        "Seconds since January 1, 1970: "
        + epoch_seconds_formatted
        + " or "
        + epoch_seconds_scientific
        + " in scientific notation"
    )
    print(string_time)

except Exception as e:
    print(f"Error: {e}")

# import datetime

# try:
#     today = datetime.datetime.now()
#     epoch = datetime.datetime.fromtimestamp(0)
#
#     formatted_today = today.strftime("%b %-d %Y")
#     formatted_epoach = epoch.strftime("%B %-d, %Y")
#
#     delta = today - epoch
#     delta_in_seconds = delta.total_seconds()
#
#     seconds_formatted = f"{delta_in_seconds:,.4f}"
#     scientific_notation = "{:.2e}".format(delta_in_seconds)
#
#     print(
#         f"Seconds since {formatted_epoach}:
#         {seconds_formatted} or {scientific_notation}
#         in scientific notation"
#     )
#     print(formatted_today)
#
# except Exception as e:
#     print(f"Error: {e}")
#
