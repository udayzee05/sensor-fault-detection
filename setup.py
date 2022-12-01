from setuptools import find_packages,setup
from typing import List

def get_requirement()->List[str]:
    '''
    This function will return list of requirement
    '''
    requirement_list:List[str] = []
    with open('requirement.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            requirement_list.append(line) 
    #Assignment : write code to read requirement .text file and append each requirement in requirement list variable
        return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="uday",
    author_email="udayzee05@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement(),

)