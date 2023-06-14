
import openai
import random


prompts = ["Tell me a very interesting and suspenseful story about a time when the unexpected happened",
"Give me a very interesting and suspenseful story about an unusual coincidence",
"Tell me a very interesting and suspenseful story about a time when someone's kindness made a difference",
"Give me a very interesting and suspenseful story about an unexpected plot twist",
"Tell me a very interesting and suspenseful story about an amazing accomplishment",
"Give me a very interesting and suspenseful story about a scary or creepy experience",
"Tell me a very interesting and suspenseful story about a time when someone overcame adversity",
"Give me a very interesting and suspenseful story about a miraculous event",
"Tell me a very interesting and suspenseful story about a near-death experience",
"Give me a very interesting and suspenseful story about a surprising encounter with a stranger",
"Tell me a very interesting and suspenseful story about an act of bravery or heroism",
"Give me a very interesting and suspenseful story about a life-changing moment",
"Tell me a very interesting and suspenseful story about a shocking revelation or secret",
"Give me a very interesting and suspenseful story about an unexpected success or failure",
"Tell me a very interesting and suspenseful story about a time when something inexplicable happened",
"Give me a very interesting and suspenseful story about a humorous or embarrassing moment",
"Tell me a very interesting and suspenseful story about a time when someone faced a difficult decision",
"Give me a very interesting and suspenseful story about a moment of serendipity or luck",
"Tell me a very interesting and suspenseful story about a time when someone went above and beyond to help another person"
]


def getStory(title, postNum):
    
    
    prompt = random.choice(prompts)
  

    openai.api_key = "" # Replace with your api Key!

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"The following is a conversation with an Amazing storytelling AI. The AI is creative and excellent at creating suspenseful, mysterious,  and jaw-dropping stories. His stories always have an amazing twist. The stories are also always long, but intriguing. \n\nHuman: Hello, who are you?\nAI: I tell the most amazing and mysterious stories, what amazing thing would you like to hear about today?\nHuman: {prompt} Make sure it is in the first person and sounds very real and like you just happened to be typing the story. Also make sure it is about and you keep this prompt in mind: \" {title} \".\nAI:",
    temperature=0.9,
    max_tokens=3863,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    
    story = response.choices[0].text
    
    story.replace("\nHuman:", "")
    story.replace("\nAI:", "")
    
    open(f"assets/post{postNum}/story.txt", "w").write(story)
    
    
    
    
