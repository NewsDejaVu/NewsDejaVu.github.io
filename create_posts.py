import os
import json
import datetime

def convert_json_to_md(json_file, source_folder='_json', destination_folder='_posts'):
    # Construct the full path of the source and destination files
    source_path = os.path.join(source_folder, json_file)
    destination_path = os.path.join(destination_folder, json_file.replace('.json', '.md'))

    # Read the .json file
    with open(source_path, 'r') as file:
        data = json.load(file)

    # Extract content from JSON
    nearest_hist_news = data.get('nearest_hist_news', {})
    print(nearest_hist_news)
    for i, news in enumerate(nearest_hist_news):
      destination_path = os.path.join(destination_folder, json_file.replace('.json', f'-{i}.md'))
      headline = news.get('headline', 'No Headline')
      article = news.get('article', 'No Article Content')
      byline = news.get('byline', 'No Byline')

      # Format the content in Markdown
      md_content = f"# {headline}\n\n*{byline}*\n\n{article}\n"

      # Write the content to a .md file
      with open(destination_path, 'w') as file:
          file.write(md_content)

      print(f"Converted {json_file} to Markdown and saved in {destination_folder}")

if __name__ == '__main__':
  todaysdate = datetime.datetime.today().strftime('%Y-%m-%d')
  convert_json_to_md(f'{todaysdate}.json')
