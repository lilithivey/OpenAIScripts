import openai

topic = "Make up a random quote that will be sarcastic and motivational"
openai.api_key = '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'

response = openai.Completion.create(
    model="text-davinci-002",
    prompt= topic,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
)
print(response.choices[0].text)
print('')
print('-A.I')
