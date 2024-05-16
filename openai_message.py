import config 

SYSTEM_ROLE = "You are a polite assistant. You are persuasive but not pushy."

PROMPT = "Here is information about a clinical trial: {INFORMATION}. This is what this user {USERNAME} thinks about the clinical trial: {USER_OPINION}. Generate a message targeting this user. Encourage them to participate in this clinical trial."

OPEN_AI_KEY = config.OPEN_AI_KEY

from openai import OpenAI

client = OpenAI()

