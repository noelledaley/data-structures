def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff", 
                    "Slytherin", 
                    "Ravenclaw", 
                    "Gryffindor", 
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])
    
    """

    houses = set()

    cohort_file = open(filename)

    for line in cohort_file:
        line = line.rstrip()
        line = line.split('|')
        houses.add(line[2])

    houses.remove("")

    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]
    
    """

    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []

    cohort_file = open(filename)

    for line in cohort_file:
        line = line.rstrip()
        line = line.split("|")
        full_name = line[0] + " " + line[1]
        if line[4] == "Winter 2015" and line[4] != "":
            winter_15.append(full_name)
        if line[4] == "Spring 2015" and line[4] != "":
            spring_15.append(full_name)
        if line[4] == "Summer 2015" and line[4] != "":
            summer_15.append(full_name)
        if line[3] not in tas and line[3] != "":
            tas.append(line[3])

    all_students.extend([winter_15, spring_15, summer_15, tas])



    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. houses_tas = [ hufflepuff, 
                        gryffindor, 
                        ravenclaw, 
                        slytherin, 
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas 
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []

    cohort_file = open(filename)

    for line in cohort_file:
        line = line.rstrip()
        line = line.split("|")
        
        last_name = line[1]
        house = line[2]

        if line[3] == "" and house != "":
            tas.append(last_name)
        elif house == "Gryffindor":
            gryffindor.append(last_name)
        elif house == "Hufflepuff":
            hufflepuff.append(last_name)
        elif house == "Slytherin":
            slytherin.append(last_name)
        elif house == "Dumbledore's Army":
            dumbledores_army.append(last_name)
        elif house == "Order of the Phoenix":
            order_of_the_phoenix.append(last_name)
        elif house == "Ravenclaw":
            ravenclaw.append(last_name)
        else: 
            pass 

    all_students.extend([gryffindor, hufflepuff, slytherin, dumbledores_army, order_of_the_phoenix, ravenclaw, tas])

    for houses in all_students:
        houses.sort()

    return all_students


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    # Code goes here

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts. 
    Uses set operations (set math) to create a set of these names. 
    NOTE: Do not include staff -- or do, if you want a greater challenge. 

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that, when given a name, returns everyone in
    their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here

    return

