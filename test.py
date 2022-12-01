
from typing import List


def get_requirement()->List[str]:
    '''
    This function will return list of requirement
    '''
    requirement_list=[]
    with open('requirement.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            requirement_list:List[str].append(line)  
    #Assignment : write code to read requirement .text file and append each requirement in requirement list variable
        return requirement_list

print(get_requirement())