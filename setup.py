from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            for line in requirements:
                requirment=line.strip()
                if requirment and requirment!='-e .':
                    requirement_lst.append(requirment)

    except Exception as e:
        raise e

    return requirement_lst

setup(
    name='Networkingproject',
    version='0.0.1',
    author='vishruth',
    author_email='vishu.valandas@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)

