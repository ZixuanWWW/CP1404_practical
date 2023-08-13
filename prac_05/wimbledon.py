import csv
def main():
    filename = "wimbledon.csv"
    data = read_data(filename)
    champions = get_champions(data)
    show_champions(champions)
    countries, number_of_countries = get_countries(data)
    show_countries(countries, number_of_countries)

def read_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        rows = csv.reader(in_file)
        next(rows)
        data = [row for row in rows]
    return data

def get_champions(data):
    champions = {}
    for row in data:
        winner = row[2]
        if winner in champions:
            champions[winner] += 1
        else:
            champions[winner] = 1
    return champions

def show_champions(champions):
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")
    print()

def get_countries(data):
    countries = {}
    for row in data:
        country = row[1]
        if country in countries:
            countries[country] += 1
        else:
            countries[country] = 1
    sorted_countries = sorted(countries.keys())
    return sorted_countries, len(countries)

def show_countries(countries, number_of_countries):
    print(f"These {number_of_countries} countries have won Wimbledon: ")
    country_list = ", ".join(countries)
    print(country_list)


main()
