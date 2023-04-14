def test_gpt():
  import json
  import openai
  from docassemble.base.util import get_config

  openai.api_key = get_config('openai secret key')

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Be nice: Why should I?",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)

  content = response['choices'][0]['text']  
  return content