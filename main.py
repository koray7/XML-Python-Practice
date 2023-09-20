import xml.dom.minidom


def remove_last_person(domtree):
    group = domtree.documentElement
    people = group.getElementsByTagName('person')

    if people:
        last_person = people[-1]
        group.removeChild(last_person)


###### Creating a function to check if a person with the same ID already exists #####
def person_exists(domtree, person_id):
    group = domtree.documentElement
    people = group.getElementsByTagName('person')

    for person in people:
        if person.getAttribute('id') == person_id:
            return True
    return False


####### Parsing the XML document ############
domtree = xml.dom.minidom.parse('people.xml')

group = domtree.documentElement

people = group.getElementsByTagName('person')

for person in people:
    print(f"--Person {person.getAttribute('id')} --")

    name = person.getElementsByTagName('name')[0].childNodes[0].nodeValue
    age = person.getElementsByTagName('age')[0].childNodes[0].nodeValue
    weight = person.getElementsByTagName('weight')[0].childNodes[0].nodeValue
    height = person.getElementsByTagName('height')[0].childNodes[0].nodeValue

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Weight: {weight}")
    print(f"Height: {height}")

######### Adding new person #######
new_person_id = "77"
new_person_name = "Captain America"
new_person_age = "97"
new_person_weight = "220"
new_person_height = "5'11"

new_person_id = "100"
new_person_name = "Billy Butcher"
new_person_age = "41"
new_person_weight = "220"
new_person_height = "6'1"

new_person_id = "89"
new_person_name = "Frenchy"
new_person_age = "31"
new_person_weight = "167"
new_person_height = "5'8"

###### Checking if a person with the same ID already exists ######
if not person_exists(domtree, new_person_id):
    new_person = domtree.createElement("person")
    new_person.setAttribute("id", new_person_id)

    name = domtree.createElement("name")
    name.appendChild(domtree.createTextNode(new_person_name))

    age = domtree.createElement("age")
    age.appendChild(domtree.createTextNode(new_person_age))

    weight = domtree.createElement("weight")
    weight.appendChild(domtree.createTextNode(new_person_weight))

    height = domtree.createElement("height")
    height.appendChild(domtree.createTextNode(new_person_height))

    new_person.appendChild(name)
    new_person.appendChild(age)
    new_person.appendChild(weight)
    new_person.appendChild(height)

    group.appendChild(new_person)

with open('people.xml', 'w') as f:
    f.write(domtree.toprettyxml())
