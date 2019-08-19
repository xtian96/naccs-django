import requests

SCHOOLS_ENDPOINT = 'http://universities.hipolabs.com/search'

# Returns a mapping of school names to school domains
def get_schools():
    ca = requests.get(SCHOOLS_ENDPOINT, params={'country':'Canada'})
    ca = ca.json()
    us = requests.get(SCHOOLS_ENDPOINT, params={'country':'United States'})
    us = us.json()

    mapping = {}

    for school in ca:
        mapping[school.get('name')] = school.get('domains')
    
    for school in us:
        mapping[school.get('name')] = school.get('domains')

    return mapping
