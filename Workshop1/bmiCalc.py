__author__ = 'Nicholas Stanton-Cook'
print('Body Mass Calculator')
print()
print('Welcome to Body Mass Calculator Program!\nProgrammed by {}'.format(__author__))
print()

heightValue = float(input('Please enter your Height in cm: '))
weightValue = float(input('Please enter your Weight in Kg: '))
bmiValue = weightValue * (heightValue * heightValue)
print()
print('At your current weight {} and Height {},\n your B.M.I. is {}'.format(weightValue, heightValue, bmiValue)  )

