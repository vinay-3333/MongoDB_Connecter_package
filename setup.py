from setuptools import find_packages,setup
from typing import List

"""HYPEN_E_DOT='-e .'

def get_requirement(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requiremets]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements"""



setup(
    name='DimondPricePrediction',
    version='1.0.0',
    author='Vinay Agrawal',
    author_email='vagrawal@gmail.com',
    install_requires=['scikit-learn','numpy','pandas'],
    packages=find_packages()
)