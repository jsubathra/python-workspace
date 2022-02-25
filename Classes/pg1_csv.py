import csv

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # csv_reader shd be iterated

#     # # next(csv_reader) # to skip the header
#     # for line in csv_reader:
#     #     print(line)  # including the header all the lines are printed as lists
#     #     # print(line[2])  # only email

#     with open('new_names.csv', 'w') as new_csv_file:
#         # to write the new file with - delimter or '\t' tab delimter
#         csv_writer = csv.writer(new_csv_file, delimiter='\t')

#         for line in csv_reader:
#             csv_writer.writerow(line)  # writes all the lines

# with open('new_names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file,delimiter = '\t') # by defalult will except , if otherwise we need to specify

#     for line in csv_reader:
#         print(line)

# Dictionary Reader is better as each line is a dictionary with key as the first row
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['email'])  # can give the key to retrive values

        with open('new_names1.csv', 'w') as new_csv_file:
            # field names must be specifield in tthe dic writer
            fieldnames = ['first_name', 'last_name', 'email']
            csv_writer = csv.DictWriter(
                new_csv_file, delimiter='\t', fieldnames=fieldnames)

            csv_writer.writeheader()  # to write the header also

            for line in csv_reader:
                del line['email']  # the email column will be removed
                csv_writer.writerow(line)
