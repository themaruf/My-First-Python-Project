patientName = "Jhon Smith"
patientAge = 32
isNewPatient = False

patientName = input("Enter your name: ")
patientAge = input("Enter your age: ")
isNewPatientInput = input("Have you visited us before?(Y for Yes, Anything for No) ")

if(isNewPatientInput == "Y" or isNewPatientInput == "y"):
    isNewPatient = True
    print(patientName + " is " + str(patientAge) + " years old and a new patient")
else:
    print(patientName + " is " + str(patientAge) + " years old and is not a new patient")