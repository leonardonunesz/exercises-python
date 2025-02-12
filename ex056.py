#Read a name, a age and a gender of 4 people. Show: average age of the group, what is the name of the oldest man and how many women have less than 20 years old
age = 0
sumage = 0
average = 0
oldestage = 0
name = ''
oldestname = ''
sex = ''
womenC = 0
for person in range(1, 5):
  name = input('Name: ').strip()
  age = int(input('Age: '))
  sex = input('Sex [M/F]: ').upper().strip()
  #Average of the group
  sumage += age
  average = sumage / 4
  #name of the oldest man
  if sex == 'M':
    if person == 1:
      oldestage = age
      oldestname = name
    else:
      if age > oldestage:
        oldestage = age
        oldestname = name
  #women less than 20 years old
  elif sex == 'F' and age < 20:
    womenC += 1
if womenC == 4:
  oldestname = 'none'
print('The group average is: {}'.format(average))
print('The oldest man is {} with {} years old'.format(oldestname, oldestage))
print('Have {} women less than 20 years old'.format(womenC))