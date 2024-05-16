import os
import config
from bs4 import BeautifulSoup
from googlesearch import search
import urllib.request as urequest
import urllib.parse as parse
import ssl

context = ssl._create_unverified_context()

SYSTEM_ROLE = "You are a polite and helpful assistant. You are persuasive but not pushy."

PROMPT = "Here is information about a clinical trial: {}. This is the sentiment of this user named {} about the clinical trial: {}. Generate a personalized message for the user encouraging them to participate in the clinical trial. Add relevant supporting information as required. Always use {} for details on interventions, outcomes, and eligibility. Always discuss pros and cons. If user is neutral, be more informative and persuasive. If user is negative, give them information but do not push them."


from openai import OpenAI

client = OpenAI(api_key=config.OPENAI_API_KEY)

def info_search(keyword):
    info_string = ""
    urls = []
    for url in search(keyword +" clinicaltrials.gov", num_results = 1):
        urls.append(url)
        page=urequest.urlopen(url, context = context)
        # print(url)
        html_doc=BeautifulSoup(page,'html.parser')

        study_info = html_doc.findAll('div', {'class':'ct-body3 tr-indent2'})
        for element in study_info:
            if study_info:
                info_string += "\n" + element.text
    return (info_string, urls[0])



def generate_message(INFORMATION, USER, SENTIMENT, URL):
    #print(PROMPT.format(INFORMATION, USER, SENTIMENT, URL))
    response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": SYSTEM_ROLE},
    {"role": "user", "content": PROMPT.format(INFORMATION, USER, SENTIMENT, URL)}
  ]
)
    return response.choices[0].message.content


# generate_message(info_search("women heart attack")[0], "xyz", "Neutral", info_search("women heart attack")[1])
