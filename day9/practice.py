# This lesson is for Dictionaries and Nesting

student_scores ={
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = dict()

for student_score in student_scores:
    if 91 <= student_scores[student_score]:
        student_grades[student_score] = 'Outstanding'
    elif 81 <= student_scores[student_score]:
        student_grades[student_score] = 'Exceeds Expectations'
    elif 71 <= student_scores[student_score]:
        student_grades[student_score] = 'Acceptable'
    else:
        student_grades[student_score] = 'Fail'
        
print(student_grades)

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, times_visited, cities_visited):
    
    new_country = dict()
    
    new_country['country'] = country_visited
    new_country['visits'] = times_visited
    new_country['cities'] = cities_visited
    
    travel_log.appned(new_country)
    

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
