from setuptools import find_packages,setup
from typing import List

HYPHEN_E_dot= "-e ."

def get_req(file_path_name:str)->List[str]:
    '''
    This funciton will return the list of requirements
    '''
    req=[]
    with open(file_path_name) as file_obj:
        req = file_obj.readlines()
        [r.replace("\n","") for r in req]

        if HYPHEN_E_dot in req:
            req.remove(HYPHEN_E_dot)
    return req


setup(
name='mlproject',
version='0.0.1',
author='Pranav Sharma',
author_email='pshar416@gmail.com',
packages= find_packages(),
install_requires = get_req('requirements.txt')
)