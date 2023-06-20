from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import sys

session = Session(profile_name="default")
polly = session.client("polly")


def getTTS(text, outputDir, voice="Matthew"):

    try:
        response = polly.synthesize_speech(Text=text, OutputFormat="mp3",
                                           VoiceId=voice)

    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)

    if "AudioStream" in response:

        body = response['AudioStream'].read()

        try:
            with open(outputDir + '/speech.mp3', "wb") as file:
                file.write(body)

        except IOError as error:
            print(error)
            sys.exit(-1)
    else:
        print("Could not stream audio")
        sys.exit(-1)
