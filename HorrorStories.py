from cProfile import label
import sys
import openai
import os
print("Amy's' AI horror story generator")
print("################################################################################")
print(" ")
topic = input("Give topic: ")
print("sending...")
openai.api_key = "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"

response = openai.Completion.create(
    model="text-davinci-002",
    prompt="Topic: Breakfast\nTwo-Sentence Horror Story: He always stops crying when I pour the milk on his cereal. I just have to remember not to let him see his face on the carton.\n    \nTopic: " + topic+"\nTwo-Sentence Horror Story:",
    temperature=0.8,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
)
print(response.choices[0].text)

print("Want to do another? (y/n)")

#if input() == "n":
#    sys.exit()
#    if input() == "y":
#        os.execv(sys.executable, ['python'] + sys.argv)`