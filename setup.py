from setuptools import setup, find_packages

setup(
    name="today_checklist",                # 패키지 이름
    version="0.1.0",                       # 프로젝트 버전
    packages=find_packages(),              # 자동으로 패키지 폴더(today_checklist) 탐색
    install_requires=[                     # 의존성 패키지 (필요 시 추가)
        "pytest",
    ],
    author="김효은",                       # 작성자 이름
    description="하루 일과 및 체크리스트 관리 패키지",
    python_requires='>=3.7',               # 파이썬 버전 요구사항
)