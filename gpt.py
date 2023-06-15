
import openai
import random

import env


prompts = ["The following is a realistic, mysterious, and suspenseful story about a dilapidated bed and breakfast with a twisted secret",
"The following is a realistic, mysterious, and suspenseful story about a possessed childhood toy that brings terror to its owner",
"The following is a realistic, mysterious, and suspenseful story about a remote cabin in the woods that holds a dark and malevolent presence",
"The following is a realistic, mysterious, and suspenseful story about a lost diary filled with sinister secrets that should have remained hidden",
"The following is a realistic, mysterious, and suspenseful story about a cursed painting that brings madness and death to those who possess it",
"The following is a realistic, mysterious, and suspenseful story about a secret underground tunnel inhabited by vengeful spirits with a thirst for souls",
"The following is a realistic, mysterious, and suspenseful story about a haunted antique shop where every object holds a dark history and restless spirits roam",
"The following is a realistic, mysterious, and suspenseful story about a series of unexplained disappearances linked to a sinister force lurking in the shadows",
"The following is a realistic, mysterious, and suspenseful story about a hidden treasure that comes with a deadly curse, driving its seekers to madness and death",
"The following is a realistic, mysterious, and suspenseful story about a long-lost twin who returns from the grave, seeking revenge on those who wronged them"
]


def getStory(title, postNum):
    
    
    prompt = random.choice(prompts)
  
                                        #REMOVE THE REMOVEME and the BRACKETS so that it looks like 'env.py'
    openai.api_key = env.OPENAI_API_KEY # Replace variable in env[REMOVEME].py with your OpenAI API key

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"The following is a realistic, mysterious, and suspenseful story about {title} with a twist at the end.\n\n{prompt}:",
    temperature=1.02,
    max_tokens=3753,
    top_p=1,
    frequency_penalty=0.24,
    presence_penalty=0.6,
    stop=["Story:"]
    )
    
    story = response.choices[0].text
    
    story.replace("\nHuman:", "")
    story.replace("\nAI:", "")
    
    open(f"assets/post{postNum}/story.txt", "w").write(story)
    
    
    
    
