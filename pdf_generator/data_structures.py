from dataclasses import dataclass


@dataclass
class PersonalInformation:
    professional_title: str
    linkedin_profile_url: str
    github_profile_url: str
    country_of_residence: str


@dataclass
class Skill:
    name: str
    level: str


@dataclass
class MainPageContext:
    personal_information: PersonalInformation
    professional_summary: str
    skills: list[str]
    total_experience: int
