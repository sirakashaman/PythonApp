# arr1=[1,2,4,5,10]
# arr2=[5,6,-1,4,8]
# x=9
# # print([i for i in arr1 if i!=0] + [j for j in arr2 if j==0])
# print([(i,j) for i in arr1 for j in arr2 if i+j ==x])
# print([(x-i,i) for i in arr1 if x-i in arr2])
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    result = [0,0,0]
    i = 1 
    while(i< len(patient_medical_speciality_list)):
        if patient_medical_speciality_list[i] == 'P': result[0] = result[0] + 1
        elif patient_medical_speciality_list[i] == 'O' : result[1] = result[1] + 1
        elif patient_medical_speciality_list[i] == 'E' : result[2] = result[2] + 1
        i = i + 1
    a = max(result)
    a = result.index(a)
    if a == 0: speciality = 'Pediatrics'
    elif a == 1: speciality ='Orthopedics'
    else : speciality = 'ENT'
    return speciality
patient_medical_speciality_list=input()
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)



[101,'P',102,'O',302,'P',305,'P']	Pediatrics
[101,'O',102,'O',302,'P',305,'E',401,'O',656,'O']	Orthopedics
[101,'O',102,'E',302,'P',305,'P',401,'E',656,'O',987,'E']	ENT