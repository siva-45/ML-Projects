#this for building our application as package 
from setuptools import find_packages,setup
from typing import List

hypen_e_dot = "-e ."
def get_requirements(file_path:str)->List(str):
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements

serup(
name= "mlproject",
version = '0.0.1',
author = "Siva",
packages = find_packages(),
install_requores = get_requirements('requirements.txt')

)