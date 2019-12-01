from employees import Employee
import random


def employeesCreate():
    revisor = Employee(0,'revisor')

    specialists = []
    for i in range (0,2):
        specialists.append(Employee(i,'specialist','revisor'))

    attendants = []
    for i in range (0,6):
        superior_id = i%2
        attendants.append(Employee(i,'attendant','specialist'))
    
    return revisor,specialists,attendants



def flukeMethod():
    
    revisor,specialists,attendants = employeesCreate()
    unavailableWorkers = []

    def renewAvailability():
        if len(unavailableWorkers) > 0 and random.randint(0,2) == 1:
            i = random.randint(0, len(unavailableWorkers)-1)
            employee = unavailableWorkers.pop(i)
            if employee.jobRole == 'attendant':
                attendants.append(employee)
            else: specialists.append(employee)
            isNewAvailable = True
        else: isNewAvailable = False
        return isNewAvailable

    numberOfCalls = 15
    callNumber = 0
    while callNumber < numberOfCalls:

        # selecting call receiver
        if len(attendants) > 0:
            receiver = attendants.pop()
            print(receiver.jobRole+' '+str(receiver.id)+' got call '+str(callNumber))
            callNumber += 1 
            unavailableWorkers.append(receiver)
        elif len(specialists) > 0:
            receiver = specialists.pop()
            print(receiver.jobRole+' '+str(receiver.id)+' got call '+str(callNumber))
            callNumber += 1 
            unavailableWorkers.append(receiver)
        else:
            receiver = revisor
            print(receiver.jobRole+' '+str(receiver.id)+' got call '+str(callNumber))
            # checking for returning workers
            isNewAvailable = False
            while not isNewAvailable:
                isNewAvailable = renewAvailability()

        
        



    return None

def main():
    flukeMethod()

if __name__ == "__main__":
    main()


