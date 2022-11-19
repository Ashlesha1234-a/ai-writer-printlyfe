import os
import openai
import config
openai.api_key = config.OPENAI_API_key

def productDescription(query):
response = openai.Completion.create(
  model="davinci-instruct-beta",
  prompt="Generate a detailed product description for:{}".format(query),
  temperature=0.6,
  max_tokens=200,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0)
  
  print(response)
  query = 'Apple iPhone'
  productDescription(query)
  
  







