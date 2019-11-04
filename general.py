# parse a string to float
def parse_number(num_str):
    try:
        num_str = num_str.replace(',', '')
        return float(num_str)
    except Exception as exception:
        print(exception)
        return num_str


# Create a new file
def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()


# Month dictionary
month_dict = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12'
}


# Parse date from investing
def parse_date_from_investing(date_str):
    parts = date_str.split()
    month = month_dict[parts[0]]
    return parts[1] + '/' + month


# Parse date from trading chart
def parse_date_from_trading_chart(date_str):
    parts = date_str.split("'")
    month = month_dict[parts[0]]
    return parts[1] + '/' + month