import csv
import random
import uuid
import datetime
from faker import Faker

fake = Faker()

even_odd_counter = 1

start_date = datetime.date(2003, 1, 1)
end_date = datetime.date(2017, 12, 31)

headers = ['Client #', 'Case #', 'Service Type', 'Date Case Created', 'Resolution Date', 'Birthdate', 'Race',
           'Ethnicity', 'HH Num People', 'HH Annual Income', 'Veteran', 'Disabled', 'Gender', 'Education Level',
           '% AMI', 'age', 'Service Type', 'Resolution', 'Property Street Address', 'Property City', 'Property State',
           'Property Zip Code', 'Price Purchase', 'Closing Date', '1st Time Home Buyer', 'course', 'Client Zip',
           'Head of household']


def main():
    global even_odd_counter
    input_file = input('File Name: ') + '.csv'
    output_file = input('Output File Name: ') + '.csv'

    with open(input_file) as infile:
        data = csv.DictReader(infile)
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = headers
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for line in data:
                # removes a huge set of blanks from the data
                if line['Date Case Created'] == '':
                    continue
                case_created_date = fake_date(start_date, end_date)
                # creates a fake start date for the data
                # TODO: Make all the random dates within 2 years of actual start date to help control for inflation

                line['Service Type'] = remove_blanks(line['Service Type'])
                line['Race'] = remove_blanks(line['Race'])
                line['Ethnicity'] = remove_blanks(line['Ethnicity'])
                line['HH Num People'] = remove_blanks(line['HH Num People'])
                line['Veteran'] = remove_blanks(line['Veteran'])
                line['Disabled'] = remove_blanks(line['Disabled'])
                line['Gender'] = remove_blanks(line['Gender'])
                line['Education Level'] = remove_blanks(line['Education Level'])
                line['Service Type'] = remove_blanks(line['Service Type'])
                line['Resolution'] = remove_blanks(line['Resolution'])
                line['Property Street Address'] = remove_blanks(line['Property Street Address'])
                line['Property City'] = remove_blanks(line['Property City'])
                line['Property State'] = remove_blanks(line['Property State'])
                line['Property Zip Code'] = remove_blanks(line['Property Zip Code'])
                line['Price Purchase'] = remove_blanks(line['Price Purchase'])
                line['Closing Date'] = remove_blanks(line['Closing Date'])
                line['1st Time Home Buyer'] = remove_blanks(line['1st Time Home Buyer'])
                line['course'] = remove_blanks(line['course'])
                line['Client Zip'] = remove_blanks(line['Client Zip'])
                line['Head of household'] = remove_blanks(line['Head of household'])

                # the following all get "randomized"

                line['Client #'] = uuid.uuid4()
                line['Date Case Created'] = check_blank(line['Date Case Created'], case_created_date)
                line['Resolution Date'] = resolution_date(line['Resolution Date'], case_created_date)
                line['age'] = noisy_number(line['age'], 0, 10)
                line['HH Annual Income'] = noisy_number(line['HH Annual Income'], 0, 5000)
                line['Price Purchase'] = noisy_number(line['Price Purchase'], 0, 50000)
                line['% AMI'] = noisy_number(line['% AMI'], 0, 20)
                even_odd_counter = random.randint(1, 2)
                writer.writerow(line)


def get_data(file):
    with open(file) as csvfile:
        data = csv.DictReader(csvfile)
        return data


def fake_date(start, end):
    date = fake.date_between_dates(date_start=start, date_end=end)
    return date


def check_blank(item, output):
    if item == '':
        item = ''
    else:
        item = output
    return item


def noisy_number(item, lowerbound, upperbound):
    # adds an amount of noise to item within user defined bounds
    if item == '':
        item = ''
    elif item == '0':
        item = ''
    elif item == '#N/A':
        item = ''
    else:
        if even_odd_counter % 2 == 1:
            item = int(item) + random.randint(lowerbound, upperbound)
        else:
            item = abs(int(item) - random.randint(lowerbound, upperbound))
    return item


def resolution_date(item, start_date):
    # creates a resolution date within a year of the start date
    if item == '':
        item = ''
    else:
        end = datetime.date(start_date.year + 1, 12, start_date.day)
        item = fake_date(start_date, end)
    return item


def remove_blanks(item):
    if item == '#N/A':
        item = ''
        item = item
    elif item == '0':
        item = ''
    elif item == '':
        item = ''
    else:
        item = item
    return item


if __name__ == '__main__':
    main()
