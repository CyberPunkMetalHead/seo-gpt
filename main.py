import numpy as np

from services.chat_gpt_service import ChatGpt
from services.scraper_service import ContentScraper
from utils.util import Utils
from utils.logger import *
from utils.load_config import *


def main():
    scraper = ContentScraper()
    chatgpt = ChatGpt()
    util = Utils()

    saved_articles = util.get_filenames_in_folder()

    if len(saved_articles) == 0:
        # Generates a list of all the pages that contain articles
        logging.info(f"Scraping {blog_url} ")
        pages = scraper.generate_list_of_pages(blog_url, num_pages, page_param)

        # Generates a list of article URLS and flattens the array
        article_urls = np.hstack(
            [
                scraper.search_for_pages_in_parent_page(
                    page,
                    path_to_search_for=path_to_search_for,
                    root_url=root_url,
                    paths_to_exclude=paths_to_exclude,
                )
                for page in pages
            ]
        )

        # Scrapes and saves each article as an HTML file.

        articles = [
            util.save_file(
                f"{content['title']}.txt",
                content["body"],
            )
            for content in [
                scraper.scrape_all_content_under_tag(url, article_tag, title_tag)
                for url in article_urls
            ]
        ]
    else:
        logging.info(
            f"Skipping scraping as the output folder contains {len(saved_articles)} articles. If you want to re-scrape. delete everything from the output/scraped_articles folder."
        )

    logging.info("Starting ChatGPT service")
    saved_articles = util.get_filenames_in_folder()
    for article in saved_articles:
        try:
            article_body = util.load_file(article)
            response = chatgpt.generate_single_input_text(
                f"{gpt_prompt}: {article_body}"
            )

            util.save_file(
                article.replace(".txt", ".md"),
                response["choices"][0]["message"]["content"],
                path="output/gpt_articles",
            )
            logging.info(f"Successfully generated Article for {article}")

        except Exception as e:
            logging.error(f"ERROR encountered at {article}: {e}")
            continue


if __name__ == "__main__":
    main()
