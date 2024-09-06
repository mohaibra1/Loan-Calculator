import math
import argparse
import sys
parser = argparse.ArgumentParser()

#add the arguments to the parser
parser.add_argument('--type')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

args = parser.parse_args()

#intialise variables using args.argument
type = args.type
payment = args.payment
principal = args.principal
periods = args.periods
interest = args.interest
#put the variables in a list
lis2 = [payment, principal, periods, interest]
#----------------------------------------------------------------------------------
#check the if requirements are met
def check_requirements(type):
    #check if its differentiated 
    if type == None or interest == None:
        return 'Incorrect parameters'
    #check if type is not annuity or diff
    if type not in ['annuity', 'diff']:
        return 'Incorrect parameters'
    #check if numbers are postive
    for j in range(0,4):
        if lis2[j] != None:
            digit = float(lis2[j])
            if round(digit) < 0:
                print('Incorrect parameters')
                return 'Incorrect parameters'
    #check if its differentiated
    if type == 'diff':
        if payment != None:
            return 'Incorrect parameters'
        if periods == None or principal == None:
            return 'Incorrect parameters'
    #check if its annuity 
    if type == 'annuity':
        #check if 2 out of payment, principal, or periods are given
        #put the variables in a lis and check if two are given
        lis = [principal, payment, periods]
        if len(lis) != 2:
            return 'Incorrect parameters'
#--------------------------------------------------------------------------------------
#function that calculates diff
def calculator_diff():
    #calculate interest, this will be global variable being used by diff and annuity
    if interest == None:
        print('Incorrect parameters')
        return 'Incorrect parameters'
    i = float(interest)/1200
    #store the total in a varable
    total = 0
    total_with_interest = 0
    #calculate for all the months
    for j in range(1, int(periods) + 1):
        total = int(principal)/int(periods) + i * (int(principal) - (int(principal) * (j - 1)/int(periods)))
        total_with_interest += math.ceil(total)
        print(f'Month {j}: payment is {math.ceil(total)}')
    print(f'Overpayment = {(total_with_interest - int(principal))}')
#------------------------------------------------------------------------------------------
#function that calls either annuity function or diff
def calculator_annuity():
    #calculate interest, this will be global variable being used by diff and annuity
    if interest == None:
        print('Incorrect parameters')
        return 'Incorrect parameters'
    i = float(interest)/1200
    #total variable
    print('fuck this shiiit')
    total = 0
    if periods == None:
        #calculate the periods
        total =  math.log((float(payment) / (float(payment) - i * float(principal))), 1 + i)
        #round it 
        total = math.ceil(total)
        outputY = ''
        outputM = ''
        years = math.trunc(total/12)
        months = math.ceil(total%12)
        if math.trunc(total/12) > 1:
            outputY = 's'
        if total%12 > 1:
            outputM = 's'
        print(f'It will take {years} year{outputY} and {months} month{outputM} to repay this loan!')
        overpayment = int(payment) * total
        overpayment = overpayment - int(principal)
        print(f'Overpayment = {overpayment}')
        #print(f'(Overpayment = {}))
    if principal == None:
        #calculate the principal
        holder = (1 + i) ** int(periods)
        total = float(payment)/((i * holder) /(holder - 1))
        #print(math.trunc(total))
        print(f'Your loan principal = {math.trunc(total)}!.')
        overpayment = (int(payment) * int(periods)) - math.trunc(total)
        print(f'Overpayment = {overpayment}')
        
    if payment == None:
        #calculate payment
        holder = (1 + i) ** int(periods)
        total = int(principal) * (i * holder) / (holder - 1)
        print(f'Your monthly payment = {math.ceil(total)}!')
    return 'None printed'
#-------------------------------------------------------------------------------------------------
#function that calculates based on type diff or annuity
def calculator(type):
    #check the specified type given and check the rules for diff and annuity
    check_requirements(type)
    if type == 'diff':
        calculator_diff()
    elif type == 'annuity':
        calculator_annuity()
    else:
        return 'Incorrect parameters'

print(calculator(type))
