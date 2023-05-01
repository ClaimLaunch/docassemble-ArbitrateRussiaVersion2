def gpt_revise(question, response, context):
  import json
  import openai
  from docassemble.base.util import get_config

  openai.api_key = get_config('openai secret key')

  bg="The following is for your knowledge only: You are an experienced attorney at the best law firm practicing investment treaty arbitration. You are drafting a section in a ntoice of arbitration against the Russian Federtion. The investor lacks legal knowledge, and so Investor's response to questions asking about the asset and events related to the claim must be rephrased."
  
  para=" "

  q=''.join(["Investor was asked: ",question])
             
  r=f"Investor responded: '{response}'"
  task="Rephrase Investor's response accordingly. Use gender neutral terms and refer to Client as 'Investor'. Do not refer to Client's hopes or desiers, if provided. Remember, you are expected to meet high standards. Please only provide the proposed text. Do not include any text addressed to me. Do not add any fact you are not provided with, and avoid any issue you have no information about, or information that the Investor does not know. Particularly, do not assume anything about the way the asset was used or about it's location unless unless specifically provided with that information by Investor. Any reference to amounts should be as $ with no decimals and with commas. Do not say things like 'Investor informed us' - instead say 'Investor submits that'"
  
  prompt='\n'.join([bg,para,q,r,task])
  
  response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  temperature=0.2,
  messages=[
        {"role": "system", "content": "You are a lawyer drafting a written notice of intent to submit an investment treaty arbitration."},
        {"role": "user", "content":  prompt}
    ]
)
  
  return response["choices"][0]["message"]["content"]

def use_gpt(use):
  question = "What was the asset used for? Was the asset used for housing (who lived there? for how long?), business (please describe main uses, annual income and any other relevant information) or other use? Please elaborate."
  para = f"In accordance with Article 9(1) of the Agreement between the Government of the Russian Federation and the Cabinet of Ministers of the Ukraine on the Encouragement and Mutual Protection of Investments of November 27, 1998 (the “Treaty”), disputing investor hereby provides the Russian Federation with this written notice of intention to submit a claim to arbitration under Article 9(2) of the Treaty. This letter is being sent with copy to the President of the Russian Federation, the Minister of Justice of the Russian Federation, the Minister of Foreign Affairs of the Russian Federation, and Minister of Finance of the Russian Federation."

  return gpt_revise(question, use, para)

def events_gpt(events):
  question="Please describe the sequence of events that led to the damages you suffered as a result of the Russian forces' actions. Please include any specific details you remember, such as the date and time of the events, the location where they occurred, and any individuals or groups involved."
  
  para = "On the morning of February 24, 2022, Russian President Vladimir Putin announced a special military operation, and Russian forces launched strikes and a large-scale ground invasion along multiple fronts, including a northern front from Belarus towards Kyiv, a northeastern front towards Kharkiv, a southern front from Crimea, and a southeastern front from Luhansk and Donetsk. Russian troops withdrew from the northern front by April. On the southern and southeastern fronts, the Russian Federation captured Kherson in March and Mariupol in May after a siege. In April, the Russian Federation launched a renewed attack on the Donbas region, and Russian forces continued to bomb both military and civilian targets, including infrastructure such as electrical and water systems, far from the front lines. In September 2022, the Russian Federation announced the purported annexation of four partially occupied oblasts: Luhansk, Donetsk, Kherson, and Zaporizhzhia' (do not repeat this paragraph). Use gender neutral terms and refer to Client as 'Investor'. Do not refer to Client's hopes or desiers, if provided."
  
  return gpt_revise(question, events, para)

def damages_gpt(initial_value, improved, additional_investment, development, assessment, value, value_explanation):
  import json
  import openai
  from docassemble.base.util import get_config

  openai.api_key = get_config('openai secret key')

  bg = "The following is for your knowledge only: You are an experienced attorney at the best law firm practicing investment treaty arbitration. You are drafting a section in a ntoice of arbitration against the Russian Federtion describing how the Investor used an asset before it was damaged by Russian forces. The investor lacks legal knowledge, and so Investor's response to questions asking about the asset and events related to the claim must be rephrased. You are drafting a pargraph in a notice of arbitration against the Russian Federation describing the damages incurred by your client. Draft that paragraph only - not the entire notice. Use gender neutral terms and refer to Client as 'Investor'. Do not refer to Client's hopes or desiers, if provided. Remember, you are expected to meet high standards. Please only provide the proposed text. Do not add any fact you are not provided with, and avoid any issue you have no information about, or information that the Investor does not know. Particularly, do not assume anything about the way the asset was used or about it's location unless unless specifically provided with that information by Investor. Any reference to amounts should be as $ with no decimals and with commas. Do not say things like 'Investor informed us' - instead say 'Investor submits that'. The damages are calculated as follows: "

  iv = f"The Initial value of of the asset when first obtained was {initial_value}."
  if improved:
    inv = f"I then invested {additional_investment} to improve and develop the asset. {development}"
  else:
    inv = " "
  if assessment:
    va = f"The value of the asset prior to Russia's actions was {value}, This valuation is based on the following: {value_explanation}"
  else:
    va = " "  
  prompt = '\n'.join([bg, iv, inv, va])
    
  response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  temperature=0.4,
  messages=[
        {"role": "system", "content": "You are a lawyer drafting a written notice of intent to submit an investment treaty arbitration for a ukrainian citzen claiming damages from war."},
        {"role": "user", "content":  prompt}
    ]
)
    
  return response["choices"][0]["message"]["content"]

def total_damages_gpt(text):
  import json
  import openai
  from docassemble.base.util import get_config
  prompt = f"Read the following and write only the total amount of damages as $ with no decimals and with commas: '{text}'. Write the amount only and no text."
  
  openai.api_key = get_config('openai secret key')

  response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  temperature=0.4,
  messages=[
        {"role": "system", "content": "You are a handy assistant"},
        {"role": "user", "content":  prompt}
    ]
)
    
  return response["choices"][0]["message"]["content"]


