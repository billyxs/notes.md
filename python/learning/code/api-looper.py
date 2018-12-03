import pprint
import requests
from collections import defaultdict


raises={'Part-Time': .1, 'Full-Time': .2, 'On-Leave': .01 }
def getStatusRaise(status):
    return raises[status] 

def getIt(url, retry=3):
    res = (requests.get(url)).json()
    if (type(res).__name__ == 'dict' and res['status'] != 200 and retry > 0):
        return getIt(url, retry-1)
    return res

def getPersonSalaries(): 
    PERSONS_URL = "https://dev-api.hixme.com/code-exercise/persons"
    SALARIES_URL = "https://dev-api.hixme.com/code-exercise/salaries"
    persons = getIt(PERSONS_URL)
    print("GET Persons")
    print(len(persons))
    salaries = getIt(SALARIES_URL)
    print("GET Salaries")
    print(len(salaries))
    d = defaultdict(dict)
    for l in (persons, salaries):
        for elem in l:
            d[elem['PersonId']].update(elem)
    return d.values()

def updateSalary(person, percentage=0):
    print('percentage = ', percentage)
    salary = float(person['Salary'])
    person['NewSalary'] = salary + salary * percentage
    return person

def getTotals(persons):

    
def main():
    persons = getPersonSalaries()
    for p in persons:
        if (p['Status'] == 'Retired'): continue
        updateSalary(p, raises[p['Status']])
    print(persons)


main()
