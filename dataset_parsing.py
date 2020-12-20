import csv

def help_create_cities():
    rows = []
    with open('src_files/worldcities.csv', encoding='cp850') as csvfile,open('parsed_csvs/countries.csv',
                                                                               encoding='cp850') as csvfile2:
        reader2=csv.reader(csvfile2, delimiter=',')
        cities_dict={}
        for index,value in enumerate(reader2):
            cities_dict[value[0]]=index+1
        reader = csv.reader(csvfile, delimiter=',')
        cities = []
        for row in reader:
            cities.append(row[1])
        csvfile.seek(0)
        for row in reader:
            if sum(row[1] in s for s in cities) == 1:
                if(row[4] in cities_dict.keys()):
                    rows.append((row[1], cities_dict[row[4]]))

    with open('src_files/worldcities2.csv', 'w', newline='', encoding='cp850') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=1)
        for row in rows:
            writer.writerow(row)

def create_cities():
    rows = []
    with open('src_files/worldcities2.csv', encoding='cp850') as csvfile, open('src_files/wikivoyage-listings-en.csv',
                                                                               encoding='cp850') as csvfile2:
        reader = csv.reader(csvfile, delimiter=',')
        reader2 = csv.reader(csvfile2, delimiter=',')
        locations = []
        cities = []
        for row2 in reader2:
            locations.append(row2[0])
        for row in reader:
            cities.append(row[0])

        csvfile.seek(0)
        for row in reader:
            for i in locations:
                if i.startswith(row[0]) and cities.count(row[0]) == 1:
                    rows.append((row[0], row[1]))
                    break

    with open('parsed_csvs/cities.csv', 'w', newline='', encoding='cp850') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=1)
        for row in rows:
            writer.writerow(row)

    #query = "LOAD DATA INFILE 'cities.csv' INTO TABLE carmen_sandiego.cities"
    #cursor.execute(query)

    # with open('cities.csv', encoding='cp850') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')
    #     sql = "INSERT INTO carmen_sandiego.cities (city, country) VALUES (%s,%s)"
    #     for row in reader:
    #         cursor.execute(sql, row)

def create_locations():
    rows = []
    with open('src_files/wikivoyage-listings-en.csv', encoding='cp850') as csvfile, open('parsed_csvs/cities.csv',encoding='cp850') as csvfile2:
        reader = csv.reader(csvfile, delimiter=',')
        reader2 = csv.reader(csvfile2, delimiter=',')
        cities = []
        indexes = []
        for index,row2 in enumerate(reader2):
            cities.append(row2[0])
            indexes.append(index+1)
        for row in reader:
            for index,city in zip(indexes,cities):
                if (row[0].startswith(city)):
                    rows.append((row[2], row[1], index, row[12], row[23]))
                    break
    with open('parsed_csvs/locations.csv', 'w', newline='', encoding='cp850') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=1)
        for row in rows:
            writer.writerow(row)


def create_questions():
    rows = []
    with open('src_files/carmen_questions.txt', encoding='cp850') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            rows.append((row[0], row[1]))
    with open('parsed_csvs/questions.csv', 'w', newline='', encoding='cp850') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=1)
        for row in rows:
            writer.writerow(row)
    # with open('questions.csv', encoding='cp850') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')
    #     sql = "INSERT INTO carmen_sandiego.questions (question_type, description) VALUES (%s,%s)"
    #     for row in reader:
    #         cursor.execute(sql, row)

def create_comments():
    rows = []
    with open('src_files/gen_comments.txt', encoding='cp850') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            rows.append((row[0], row[1]))
    with open('parsed_csvs/comments.csv', 'w', newline='', encoding='cp850') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=1)
        for row in rows:
            writer.writerow(row)

def create_countries():
    rows = []
    with open('src_files/carmen_countries.txt', encoding='cp850') as csvfile, open('src_files/cotw.csv',
                                                                                   encoding='cp850') as csvfile2:
        reader = csv.reader(csvfile, delimiter='\t')

        reader2 = csv.reader(csvfile2, delimiter=',')
        for row1,row2 in zip(reader,reader2):
            row1.append(str(row2[1]).strip())
            row1.append(row2[3])
            row1.append(row2[8])
            row1.append(row2[14])
            rows.append(row1)

    with open('parsed_csvs/countries.csv', 'w', newline='', encoding='cp850') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=1)
        for row in rows:
            writer.writerow(row)


    #query = "LOAD DATA LOCAL INFILE 'parsed_csvs/countries.csv' INTO TABLE carmen_sandiego.countries"
    #cursor.execute(query)

    # with open('parsed_csvs/countries.csv', encoding='cp850') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')
    #     sql = "INSERT INTO carmen_sandiego.countries (country_name,capital_name,population,currency,languages,flag,region,area,gdp,climate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #     for row in reader:
    #         row[2] = int(row[2].replace(',',''))
    #         row[7] = int(row[7])
    #         try:
    #             row[8] = int(row[8])
    #         except:
    #             row[8] = 0
    #         try:
    #             row[9] = int(row[9])
    #         except:
    #             row[9] = 0
    #         cursor.execute(sql, row)

#help_create_cities()
#create_cities()
#create_locations()
#create_comments()
#create_questions()
#create_countries()

#connection.commit()
