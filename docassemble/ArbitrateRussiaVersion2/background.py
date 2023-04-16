def events_gpt(events):
  import json
  import openai
  from docassemble.base.util import get_config

  openai.api_key = get_config('openai secret key')

  q="Client was asked the folowing question: 'Please describe the sequence of events that led to the damages you suffered as a result of the Russian forces' actions. Please include any specific details you remember, such as the date and time of the events, the location where they occurred, and any individuals or groups involved.'"
  
  r=''.join(["Client responded:'",events,"'"])
  
  context="Rephrase and insert Client's response after this paragraph: 'On the morning of February 24, 2022, Russian President Vladimir Putin announced a special military operation, and Russian forces launched strikes and a large-scale ground invasion along multiple fronts, including a northern front from Belarus towards Kyiv, a northeastern front towards Kharkiv, a southern front from Crimea, and a southeastern front from Luhansk and Donetsk. Russian troops withdrew from the northern front by April. On the southern and southeastern fronts, the Russian Federation captured Kherson in March and Mariupol in May after a siege. In April, the Russian Federation launched a renewed attack on the Donbas region, and Russian forces continued to bomb both military and civilian targets, including infrastructure such as electrical and water systems, far from the front lines. In September 2022, the Russian Federation announced the purported annexation of four partially occupied oblasts: Luhansk, Donetsk, Kherson, and Zaporizhzhia.' Use gender neutral terms and refer to Client as 'Investor'. Do not refer to Client's hopes or desiers, if provided."
  
  prompt=''.join([q,r,context])
  
  response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  temperature=0.2,
  messages=[
        {"role": "system", "content": "You are a lawyer rephrasing your client's interview responses and inserting right after a paragraph in a draft of a written notice of investment treaty arbitration."},
        {"role": "user", "content":  prompt}
    ]
)
  
  return response["choices"][0]["message"]["content"]