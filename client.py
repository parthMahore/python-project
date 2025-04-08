from openai import OpenAI

# pip install openai
#if you saved a key under a differnet environmentvariable name,you can do something like:
client = OpenAI(
    api_key = "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"
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud."},
        { "role": "user", "content": "what is coding."}
    ]
)

print(completion.choices[0].message)

