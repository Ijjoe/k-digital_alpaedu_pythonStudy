from setuptools import setup, find_packages

setup(
    name='example_package_cij',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'numpy',  # 예시 종속성
        'bs4',
        'requests'
    ],
    # 추가 메타데이터
)
