
def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 +1

def decade (year):
    return ((year % 100) // 10)*10

def main():
    year = int(input('What year was the book published?'))
    print (century(year), "Century", ",", decade(year),'s')
main()

