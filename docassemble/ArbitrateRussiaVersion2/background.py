def gpt_revise(question, response):
  import json
  import openai
  from docassemble.base.util import get_config

  openai.api_key = get_config('openai secret key')

  bg="You are an experienced attorney at the best law firm practicing investment treaty arbitration. You are drafting a section in a notice of arbitration against the Russian Federation."
  
  para=" "

  q=''.join(["Investor was asked: ",question])
             
  r=f"Investor responded: '{response}'"
  task="Rephrase Investor's response . Use gender neutral terms and refer to Client as 'Investor'. Do not refer to Client's hopes or desiers, if provided. Please only provide the proposed text. Do not include any text addressed to me. Do not add any fact you are not provided with. Particularly, do not assume anything about the way the asset was used or about it's location unless unless specifically provided with that information by Investor. Any reference to amounts should be as $ with no decimals and with commas. Do not say things like 'Investor informed us' - instead say 'Investor submits that'"
  
  prompt='\n'.join([bg,q,r,task])
  
  response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  temperature=0.5,
  messages=[
        {"role": "system", "content": "You are a lawyer drafting a section of a written pleading in an investment treaty arbitration."},
        {"role": "user", "content":  prompt}
    ]
)
  
  return response["choices"][0]["message"]["content"]

def use_gpt(use):
  question = "What was the asset used for?"
  return gpt_revise(question, use)

def control_gpt(control):
  question="Please desribe any event that may estanish an argument that Russia or Russian forces had effective control over the territory where the asset was locatedbefore or at the time the asset was damaged. If you cannot think of any, please leave this question blank."  
  return gpt_revise(question, control)

def events_gpt(events):
  question="Please describe the sequence of events that led to the damages you suffered as a result of the Russian forces' actions."  
  return gpt_revise(question, events)

def ownership_gpt(ownership, bg):
  question=f"Thank you for letting us know you {ownerhsip} the asset. Please provide additional background."  
  return gpt_revise(question, bg)

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

def investment_gpt(use):
  import json
  import openai
  from docassemble.base.util import get_config
  prompt = f"You are an experienced attorney at the best law firm practicing investment treaty arbitration. You are drafting a section in a notice of arbitration against the Russian Federation.\n Investor's description of asset: {use}. \n Argue that the asset is an investment according to Article 1(1) of the Treaty without quoting from it.  Use gender-neutral terms and refer to the Client as 'Investor'. Do not refer to Client's hopes or desiers, if provided. Please only provide the proposed text. Do not include any text addressed to me. Do not add any fact you are not provided with. Particularly, do not assume anything about the way the asset was used or about its location unless specifically provided with that information by Investor. Any reference to amounts should be $ with no decimals and commas. Do not say things like 'Investor informed us' - instead say 'Investor submits that'.\n Continue the argument after the following paragraph:\n The term 'Investment' is defined broadly in Article 1(1) of the Treaty as “all kinds of property and intellectual values, which are put in by the investor of one Contracting Party on the territory of the other Contracting Party in conformity with the latter’s legislation.' Such type of investments include, but not limited to: 'a) movable and immovable property and any other rights of property therein; b) monetary funds and also securities, liabilities, deposits and other forms of participation; c) rights to objects of intellectual property, including authors' copyrights and related rights, trade marks, the rights to inventions, industrial samples, models and also technological processes and know-how; d) rights to perform commercial activity, including rights to prospecting, development and exploitation of natural resources.' "
  
  openai.api_key = get_config('openai secret key')

  response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  temperature=0.4,
  messages=[
        {"role": "system", "content": "You are an experienced attorney at the best law firm practicing investment treaty arbitration"},
        {"role": "user", "content":  prompt}
    ]
)
    
  return response["choices"][0]["message"]["content"]

def expropriation_gpt(use, events, damages):
  import json
  import openai
  from docassemble.base.util import get_config
  prompt = f"You are an experienced attorney at the best law firm practicing investment treaty arbitration. You are drafting a section in a notice of arbitration against the Russian Federation.\n Investor's description of asset: {use} \n Investor's description of events: {events}. \n Investor's description of damages: {damages}\n Argue that the asset was expropriated in violation of Article 5(1) of the Treaty without quoting from it.  Use gender-neutral terms and refer to the Client as 'Investor'. Do not refer to Client's hopes or desiers, if provided. Please only provide the proposed text. Do not include any text addressed to me. Do not add any fact you are not provided with. Particularly, do not assume anything about the way the asset was used or about its location unless specifically provided with that information by Investor. Any reference to amounts should be $ with no decimals and commas. Do not say things like 'Investor informed us' - instead say 'Investor submits that'.\n Continue the argument after the following paragraphs:\n Article 5(1) of the Treaty provides that an investment “shall not be subject to expropriation, nationalization or other measures equivalent in effect to expropriation ... except in cases where such measures are taken in the public interest according to the procedures established by law, are not of a discriminatory nature and are accompanied by prompt, adequate and effective compensation.” Such expropriation, nationalization, or equivalent measures can only be legally taken in cases where they are in the public interest, are non-discriminatory, are conducted through due process of law, and are accompanied by prompt, adequate, and effective compensation. All four of these requirements must be met in order for an expropriation to be considered lawful. Arbitral tribunals have consistently held that failure to meet any one of these conditions renders the expropriation wrongful. \n Notably, the Special Rapporteur on International Responsibility highlighted the importance of the public purpose requirement for the legality of an expropriation: \n '[T]he least that can be required of the State is that it should exercise [its] power only when the measure is clearly justified by the public interest. Any other view would condone and even facilitate the abusive exercise of the power to expropriate and give legal sanction to manifestly arbitrary acts of expropriation. […] It is accordingly sufficient to require that all States should comply with the condition or requirement which is common to all; namely, that the power to expropriate should be exercised only when expropriation is necessary and is justified by a genuinely public purpose or reason. If this raison d’etre is plainly absent, the measure of expropriation is ‘arbitrary.’'\n The Treaty prohibits not only direct expropriation, but also indirect expropriation through measures that are “equivalent in effect to expropriation”. The Treaty's protection covers not only physical takings of property or legal title transfers, but also actions that deprive an investor of the use and enjoyment of their investment without affecting possession or formal title. In cases of direct expropriation, there is typically an open and clear intent to deprive the owner of their property through physical means or legal decrees. However, in cases of indirect expropriation, it is the measure's economic impact on the investment that determines whether it constitutes an unlawful expropriation, regardless of whether there is a clear intent to expropriate. \n Here, "
  
  openai.api_key = get_config('openai secret key')

  response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  temperature=0.4,
  messages=[
        {"role": "system", "content": "You are an experienced attorney at the best law firm practicing investment treaty arbitration"},
        {"role": "user", "content":  prompt}
    ]
)
    
  return response["choices"][0]["message"]["content"]


def protection_gpt(use, events, damages):
  import json
  import openai
  from docassemble.base.util import get_config
  prompt = f"You are an experienced attorney at the best law firm practicing investment treaty arbitration. You are drafting a section in a notice of arbitration against the Russian Federation.\n Investor's description of asset: {use} \n Investor's description of events: {events}. \n Investor's description of damages: {damages}\n Argue that the asset was not provided complete and unconditional protection in violation of Article 2(1) of the Treaty without quoting from it.  Use gender-neutral terms and refer to the Client as 'Investor'. Do not refer to Client's hopes or desiers, if provided. Please only provide the proposed text. Do not include any text addressed to me. Do not add any fact you are not provided with. Particularly, do not assume anything about the way the asset was used or about its location unless specifically provided with that information by Investor. Any reference to amounts should be $ with no decimals and commas. Do not say things like 'Investor informed us' - instead say 'Investor submits that'.\n Continue the argument after the following paragraphs:\n Pursuant to Article 2(1) of the Treaty, the Russian Federation 'shall encourage the investors of [Ukraine] to make investments on its territory and shall allow such investments in conformity with its respective laws.' Article 2(2) further provides that the Russian Federation 'shall guarantee, in conformity with its own laws, the complete and unconditional legal protection of investments by [Ukrainian investors].' As discussed above, the Russian Federation enacted the Integration Law, which provided for the continuous business activity in the territory of Investor's asset."
  
  openai.api_key = get_config('openai secret key')

  response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  temperature=0.4,
  messages=[
        {"role": "system", "content": "You are an experienced attorney at the best law firm practicing investment treaty arbitration"},
        {"role": "user", "content":  prompt}
    ]
)
    
  return response["choices"][0]["message"]["content"]