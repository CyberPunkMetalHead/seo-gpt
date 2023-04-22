# GPTSEO - Re-write hundreds of articles a day

GPTSEO is a Python tool that scrapes entire blogs or knowledgebases and automatically generates hundreds of new, and SEO unique articles by using the power of ChatGPT. You can edit the prompt to get it to focus on a certain nuance or re-write existing articles from a certain perspective. YOu can also optimise for SEO by telling chatGPT to focus on certain keywords.

## How to use GPTSEO

1. Clone the Repo to your local environment
2. Make sure you're running Python 3.10+
3. Initialise a new python environment `python -m venv env`
4. Start the env `env/scripts/activate`
5. Install the requirements `pip install -r requirements.txt`
6. Rename `.env.example` to `.env` and add your OpenAI API key
7. Rename `config.example.yml` to `config.yml` and configure SEOGPT to your requirements.
8. Start main.py. (starting it outside of VS Code might cause issues)

## Using the Output
Check the `output` folder once SEOGPT has finished running. Note: If the blog contains hundreds of articles, it will take several hours or up to a day for all the articles to be generated using chatGPT. You will be able to see an output of each re-written article in the console. By default, all gpt-artcles will be saved in markdown format. 

## Limiations of SEOGPT
It most likely won't work out of the box with blogs as subdomains as it was only tested on blogs as subdirectories.

