#Given a dictionary, write python expression that gets certain data:
#Ramit's email, Ramit's first interest, Jasmine's email, Jan's second interest

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print("Ramit's email: " + ramit['email'])
print("Ramit's first interest: " + ramit['interests'][0])
print("Jasmine's email: " + ramit['friends'][0]['email'])
print("Jan's second interest: " + ramit['friends'][1]['interests'][1])