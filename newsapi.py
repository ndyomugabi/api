import click
import requests
API_KEY = '1d49361e4e44431db776c0bc3c811615'

@click.group()
def main():
        """
        NewsAPI is a newsapp that offers the user 4 sources where she is required to choose you choose one.
        your choice will returns a list of the top 10 headlines,
        The news headline has a title, description and a url in case the user needs to follow up
        The user also needs to have a valid news api created from http://www.newsapi.org
        """
        pass

@main.command()

def listsources():
	""" Lists 4 sources from the API """
	main_url = " https://newsapi.org/v2/sources?apiKey=1d49361e4e44431db776c0bc3c811615"

	# fetching data in json format 
	open_source = requests.get(main_url).json() 

	# getting all articles in a string sources
	source = open_source["sources"] 

	# empty list which will 
	# contain all trending newssources 
	results = [] 
	
	for news in source: 
                results.append(news["id"])
            
   	
	for current_new in results[0:4]:
            print(current_new)	


@main.command()
def topheadlines():
          """ enter your choice from the listsources """
          newsSource = click.prompt("Enter your choice from listsources")
    
          main_url = "https://newsapi.org/v2/top-headlines?apiKey=1d49361e4e44431db776c0bc3c811615&sources="+newsSource

	# fetching data in json format 
          open_headline = requests.get(main_url).json() 

	# getting all headlines in a string articles 
          headline = open_headline["articles"] 

	# empty list which will contain all trending newssources
	 
          output = [] 
	
          for top_news in headline: 
                click.echo('\n')
                click.secho(click.style('TITLE: ' + top_news['title'], fg='green'))
                click.secho(click.wrap_text(top_news['description']))
                click.secho(click.style('DOMAIN: ' + top_news['url'], fg='blue'))
           
           	
          for choice in output[:11]:
                print(choice)


if __name__ == '__main__':
	main()
