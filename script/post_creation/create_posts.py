import os
from pathlib import Path
import json
import datetime
import random

# See '/mnt/data01/thisdayinhistory' on NBER for the scripts that create the inputs for this code
#   and where the inputs are stored

def convert_json_to_md(todaysdate, source_folder=Path(os.getcwd(), '_json'), destination_folder=Path(os.getcwd(),'_posts')):
    # Construct the full path of the source and destination files
    if os.path.isfile(Path(source_folder, f'{todaysdate}.json')):
        source_path = Path(source_folder, f'{todaysdate}.json')
        destination_path = Path(destination_folder, f'{todaysdate}-This-Day-in-History.md')

        # Read the .json file
        with open(source_path, 'r') as file:
            og_data = json.load(file)

        # Extract content from JSON
        # print(og_data)

        randint1 = 0
        data = {}

        if len(og_data) > 0:
            randint1 = random.randint(0, len(og_data)-1)
            data = og_data[randint1]
        else:
            print('og_data has length zero')
        
        original_url = data.get('url', '')
        original_source = data.get('source', {})
        original_source_name = original_source.get('name', '').title().replace('|', ' ').replace('\n', ' ')
        original_title = data.get('title', '').title().replace('|', ' ').replace('\n', ' ')
        
        original_article = data.get('clean_text', '')[:1_000] # want only the first 1500 characters
        original_article = original_article.replace('|', ' ').replace('\n\n', '<br>&nbsp;&nbsp;&nbsp;&nbsp;').replace('\n', ' ')
        original_article = original_article + f' ...<br><br>Read the full article at<br>[{original_url}]({original_url})'
        if original_article[:len('&nbsp;&nbsp;&nbsp;&nbsp;')] != '&nbsp;&nbsp;&nbsp;&nbsp;':
            original_article = '&nbsp;&nbsp;&nbsp;&nbsp;' + original_article
        original_author = data.get('author', '').title().replace('|', ' ').replace('\n', ' ')

        original_byline = ""
        if original_author and original_source_name:
            original_byline = f"{original_author} for {original_source_name}"
        elif source_name:
            original_byline = f"{original_source_name}" 
        elif temp_byline:
            original_byline = f"{original_author}" 

        nearest_hist_news = data.get('nearest_hist_news', {})

        randint2 = 0
        news = {}
        date =  ""
        post_title = 'Today\'s News'

        if len(nearest_hist_news) > 0:

            randint2 = random.randint(0, len(nearest_hist_news)-1)
            news = nearest_hist_news[randint2]
            date = '{dt:%B} {dt.day}, {dt.year}'.format(dt=datetime.datetime.strptime(todaysdate, '%Y-%m-%d'))
            post_title = f'Today\'s News {date}'
        else:
            print('news has length zero')

        image_file_name = news.get('image_file_name', '')
        image_file_name_split = ""
        source_name = ""
        source_date = ""
        if image_file_name:
            image_file_name_split = image_file_name.split("-")
            source_date = '{dt:%B} {dt.day}, {dt.year}'.format(dt=datetime.datetime.strptime("-".join(image_file_name_split[-5:-2]), '%b-%d-%Y'))
            source_name = " ".join(image_file_name_split[1:-5]).title().replace('|', ' ').replace('\n', ' ')
        else:
            print('image_file_name is an empty string')

        headline = news.get('headline', '').title().replace('|', ' ').replace('\n', ' ')
        article =  news.get('article', '').replace('|', ' ').replace('\n\n', '<br>&nbsp;&nbsp;&nbsp;&nbsp;').replace('\n', ' ')
        if article[:len('&nbsp;&nbsp;&nbsp;&nbsp;')] != '&nbsp;&nbsp;&nbsp;&nbsp;':
            article = '&nbsp;&nbsp;&nbsp;&nbsp;' + article
        temp_byline = news.get('byline', '').title().replace('|', ' ').replace('\n', ' ')

        byline = ""
        if temp_byline and source_name:
            byline = f"{temp_byline} published in {source_name}"
        elif temp_byline:
            byline = f"{temp_byline}" 
        elif source_name:
            if source_name[0:3].lower() != "the":
                byline = f"News Wire Article published in the {source_name}" 
            else:
                 byline = f"News Wire Article published in {source_name}" 

        
        # Format the content in Markdown
        md_content = (
            "---\n",
            "layout: post\n",
            f"title: \"{post_title}\"\n",
            # "categories:\n",
            # f"    - {''}\n",
            # "tags:\n", 
            # f'    - {''}\n',
            f'date: {todaysdate}\n',
            "---\n\n",
            f'| {original_title} | {headline} |\n',
            f'| {''} | {''} |\n',
            f'| {original_byline} | {byline} |\n',
            f"| {date} | {source_date} |\n",
            f"| {original_article} | {article} |"
        )
        # print(md_content)

        # Write the content to a .md file
        with open(destination_path, 'w', encoding='utf-8') as file:
            file.writelines(md_content)

        print(f"Converted {todaysdate}.json' to Markdown and saved in {destination_folder}")
    
    elif not os.path.isfile(Path(source_folder, f'{todaysdate}.json')):
        print("Today's file was not found")
    
    return None

if __name__ == '__main__':
  convert_json_to_md(todaysdate="2023-11-30")
#   convert_json_to_md(todaysdate=datetime.datetime.today().strftime('%Y-%m-%d'))

