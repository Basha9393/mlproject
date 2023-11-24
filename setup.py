from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function wil return the list of requirements
    '''
    requirements=[]
    with open(file_path) as fiel_obj:
        requirements=fiel_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='basha9393',
author_email='sadiqbasha9393',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)