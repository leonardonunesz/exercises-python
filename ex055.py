#Read a weight of 5 people and show the biggest and the smallest weight
heavier = 0
lighter = 0
for person in range (1, 6):
    weight = float(input('Type your weight: '))
    if person == 1:
        heavier = weight
        lighter = weight
    else:
        if weight > heavier:
            heavier = weight
        if weight < lighter:
            lighter = weight 

print('The heaviest person weights {} pounds'.format(heavier))
print('The lightest person weights {} pounds'.format(lighter))