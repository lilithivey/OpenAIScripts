from cProfile import label
import sys
import openai
import os
print("The Allenator")
print("################################################################################")
print(" ")
print("sending...")
openai.api_key = "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"

response = openai.Completion.create(
    model="text-davinci-002",
    prompt="we have a mutual coworker named Allen, and we make jokes about him.  /n/n/n you will Create a list that contains five jokes (one per line) in the style of a Comedy Central Roasting, predominately about his weight. old age, or inability to stay married. jokes must be sarcastic but not hurtful./n/n/nExamples:/nAllen might be late coming in. They're still greasing him up so he can fit through the doorway./n/n'I hope Allen never passes out upstairs. We can't fit a forklift up there to get him.'",
    temperature=1,
    max_tokens=512,
    top_p=.05,
    frequency_penalty=0.9,
    presence_penalty=0
)
print(response.choices[0].text)

print("end")

#if input() == "n":
#    sys.exit()
#    if input() == "y":
#        os.execv(sys.executable, ['python'] + sys.argv)`