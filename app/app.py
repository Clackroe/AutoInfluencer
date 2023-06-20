import argparse
import os
import logging
from utils.GPTUtils import gpt
from utils.GatheringUtils import choosePost, takeScreenshot
from utils.TTSUtils import getTTS
from utils.EditUtils import editDaMovie

logger = logging.getLogger(__name__)


def choose_and_screenshot_post(subreddit, category, time, input_dir):
    try:
        title, post = choosePost(subreddit, category, time)
        takeScreenshot(post, subreddit, category, time, input_dir)
        return title
    except Exception as e:
        logger.error("Error choosing post and taking screenshot: %s", str(e))
        raise


def generate_story(title, input_dir):
    try:
        return gpt(title, input_dir)
    except Exception as e:
        logger.error("Error generating story: %s", str(e))
        raise


def convert_to_audio(story, input_dir):
    try:
        getTTS(story, input_dir)
    except Exception as e:
        logger.error("Error converting to audio: %s", str(e))
        raise


def edit_movie(clip_dir, input_dir, output_dir):
    try:
        editDaMovie(clipDir=clip_dir, inputDir=input_dir, outputDir=output_dir)
    except Exception as e:
        logger.error("Error editing movie: %s", str(e))
        raise


def main():
    # Create argument parser
    # Example: py app.py --subreddit "AskReddit" --category "hot" --time "day" --clip_dir "assets/gameplay-clips" --input_dir "assets" --output_dir "Test"
    parser = argparse.ArgumentParser(
        description="AutoInfluencer | Python Backend")
    parser.add_argument(
        "--subreddit", help="Name of the subreddit", default="AskReddit")
    parser.add_argument(
        "--category", help="Category of the posts", default="top")
    parser.add_argument(
        "--time", help="Time range of the posts", default="day")
    parser.add_argument(
        "--clip_dir", help="Directory for gameplay clips", required=True)
    parser.add_argument(
        "--input_dir", help="Input directory for screenshots", required=True)
    parser.add_argument(
        "--output_dir", help="Output directory for edited files", required=True)

    # Parse command-line arguments
    args = parser.parse_args()

    subreddit = args.subreddit
    category = args.category
    time = args.time
    clip_dir = os.path.abspath(args.clip_dir)
    input_dir = os.path.abspath(args.input_dir)
    output_dir = os.path.abspath(args.output_dir)

    # Set up logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    try:
        title = choose_and_screenshot_post(
            subreddit, category, time, input_dir)
        story = generate_story(title, input_dir)
        convert_to_audio(story, input_dir)
        edit_movie(clip_dir, input_dir, output_dir)
        logging.info("Task completed successfully.")
    except Exception as e:
        logging.error("An error occurred during execution: %s", str(e))


if __name__ == "__main__":
    main()
