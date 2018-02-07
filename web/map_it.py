import sys
import webbrowser


def arr_to_str(arr):
    return ' '.join(arr)


if len(sys.argv) > 1:
    input_arr = sys.argv[1:]
    query = arr_to_str(input_arr)
    webbrowser.open('https://www.google.com/maps/place/' + query)
