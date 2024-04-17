import markdown
import weasyprint

from pdf_generator.data_structures import PersonalInformation, Skill, MainPageContext


# Read the md file for the context
def read_md_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

# Convert the md file to html
def convert_md_to_html(md_content: str) -> str:
    return markdown.markdown(md_content)


# Convert the html file to pdf
def convert_html_to_pdf(html_content: str, pdf_file_path: str) -> None:
    weasyprint.HTML(string=html_content).write_pdf(pdf_file_path)

# Read the context from the md file
def read_context_from_md_file(file_path: str) -> MainPageContext:
    md_content = read_md_file(file_path)
    html_content = convert_md_to_html(md_content)
    pdf_file_path = 'resume.pdf'
    convert_html_to_pdf(html_content, pdf_file_path)
    return MainPageContext(
        personal_information=PersonalInformation(
            professional_title='Software Engineer',
            linkedin_profile_url='https://www.linkedin.com/in/example/',
            github_profile_url='https://github.com/example',
            country_of_residence='United States'
        ),
        professional_summary='My professional summary',
        skills=[
            Skill(name='Python', level='Expert'),
            Skill(name='Java', level='Intermediate'),
            Skill(name='C++', level='Beginner')
        ],
        total_experience=10
    )

# Read the context from the md file
def main():
    context = read_context_from_md_file('../docs/index.md')
    print(context)
    print(type(context))
    print(context.skills)
    print(type(context.skills))
    print(context.skills[0])
    print(type(context.skills[0]))
    print(context.skills[0].name)
    print(type(context.skills[0].name))
    print(context.skills[0].level)
    print(type(context.skills[0].level))
    print(context.personal_information)
    print(type(context.personal_information))
    print(context.personal_information.professional_title)
    print(type(context.personal_information.professional_title))
    print(context.personal_information.linkedin_profile_url)
    print(type(context.personal_information.linkedin_profile_url))


if __name__ == '__main__':
    main()
