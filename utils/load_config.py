from utils.util import Utils

utils = Utils()
config = utils.load_config()

scraping_options = config["scraping_options"]
blog_url = scraping_options["blog_url"]
num_pages = scraping_options["num_pages"]
page_param = scraping_options["page_param"]
path_to_search_for = scraping_options["path_to_search_for"]
root_url = scraping_options["root_url"]
paths_to_exclude = scraping_options["paths_to_exclude"]

article_options = config["article_options"]
article_tag = article_options["article_tag"]
title_tag = article_options["title_tag"]
gpt_prompt = article_options["gpt_prompt"]
