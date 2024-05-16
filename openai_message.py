import os
import config
from bs4 import BeautifulSoup
from googlesearch import search
import urllib.request as urequest
import urllib.parse as parse
import ssl

context = ssl._create_unverified_context()

SYSTEM_ROLE = "You are a polite assistant. You are persuasive but not pushy."

PROMPT = "Here is information about a clinical trial: {}. This is what this user {} thinks about the clinical trial: {}. Generate a message targeting this user. Encourage them to participate in this clinical trial."


from openai import OpenAI

client = OpenAI(api_key=config.OPENAI_API_KEY)

def info_search(keyword):
    info_string = ""
    for url in search(keyword +" clinicaltrials.gov", num_results = 1):
        page=urequest.urlopen(url, context = context)
        print(url)
        html_doc=BeautifulSoup(page,'html.parser')

        study_info = html_doc.findAll('div', {'class':'ct-body3 tr-indent2'})
        for element in study_info:
            if study_info:
                info_string += "\n" + element.text
    return info_string



def generate_message(INFORMATION, USER, SENTIMENT):
    response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": SYSTEM_ROLE},
    {"role": "user", "content": PROMPT.format(INFORMATION, USER, SENTIMENT)}
  ]
)
    print(response.choices[0].message.content)


# generate_message("Women's HARP is a multi-center, observational study which enrolls women with MI who are referred for cardiac catheterization. During the MI hospitalization, questionnaires will be administered to assess psychosocial stress leading up to the event (MI). Participants will also have the option to enroll in the HARP-Stress Ancillary Study and HARP-Platelet Sub-Study. Two months following MI, participants may be screened for the Stress Ancillary Study. Women with elevated perceived stress at screening will be enrolled. Patients will complete baseline assessments (self-report questionnaires and 7 days of wrist actigraphy) and then will be randomized to group-based stress management or to enhanced usual care (EUC). Both study arms involve 8 weekly phone sessions delivered by trained facilitators. Following intervention, participants in both study arms will repeat self-report questionnaires and 7 days of wrist actigraphy. Anticipate enrollment of approximately 200 women to meet target of 144 qualified women.", "xyz", "Positive")
info_search("women heart attack")