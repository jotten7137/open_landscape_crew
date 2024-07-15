import os
import datetime as dt
from exa_py import Exa
from langchain.agents import Tool
from typing import List, Union

today = dt.date.today()
week_ago = today - dt.timedelta(days=7)

class FieldSearchToolset:
    def __init__(self, field):
        self.field = field

    def search_trends(self, *args, **kwargs):
        """Search for the latest trends in the specified field based on the query."""
        query = args[0] if args else kwargs.get('query', '')
        return self._exa().search(
            f"latest {self.field} trends {query}",
            use_autoprompt=True,
            num_results=5,
            start_published_date= str(week_ago),
            end_published_date = str(today)
        )

    def search_research(self, *args, **kwargs):
        """Search for recent research papers in the specified field based on the query."""
        query = args[0] if args else kwargs.get('query', '')
        return self._exa().search(
            f"{self.field} research paper {query}",
            use_autoprompt=True,
            num_results=5,
            start_published_date= str(week_ago),
            end_published_date = str(today)
        )

    def search_news(self, *args, **kwargs):
        """Search for recent news articles in the specified field based on the query."""
        query = args[0] if args else kwargs.get('query', '')
        return self._exa().search(
            f"{self.field} news {query}",
            use_autoprompt=True,
            num_results=5,
            start_published_date= str(week_ago),
            end_published_date = str(today)
        )

    def find_similar(self, *args, **kwargs):
        """Search for webpages similar to a given URL."""
        url = args[0] if args else kwargs.get('url', '')
        return self._exa().find_similar(url, num_results=5)

    def get_contents(self, *args, **kwargs):
        """Get the contents of webpages."""
        urls = args[0] if args else kwargs.get('urls', [])
        if isinstance(urls, str):
            urls = [urls]
        
        exa = self._exa()
        processed_contents = []
        
        for url in urls:
            try:
                response = exa.search(url, num_results=1)
                results = response.results
                if results:
                    content = results[0]
                    processed_content = f"Title: {getattr(content, 'title', 'No title')}\n"
                    processed_content += f"URL: {getattr(content, 'url', 'No URL')}\n"
                    processed_content += f"Content: {getattr(content, 'text', 'No content')[:1000]}..."
                    processed_contents.append(processed_content)
                else:
                    processed_contents.append(f"No content found for URL: {url}")
            except Exception as e:
                processed_contents.append(f"Error retrieving content for URL {url}: {str(e)}")
        
        return "\n\n".join(processed_contents)

    def search_companies(self, *args, **kwargs):
        """Search for information about companies in the specified field based on the query."""
        query = args[0] if args else kwargs.get('query', '')
        return self._exa().search(
            f"{self.field} company {query}",
            use_autoprompt=True,
            num_results=5,
            start_published_date= str(week_ago),
            end_published_date = str(today)
        )

    def get_tools(self):
        return [
            Tool(name="search_trends", func=self.search_trends, description="Search for the latest trends in the specified field based on the query."),
            Tool(name="search_research", func=self.search_research, description="Search for recent research papers in the specified field based on the query."),
            Tool(name="search_news", func=self.search_news, description="Search for recent news articles in the specified field based on the query."),
            Tool(name="find_similar", func=self.find_similar, description="Search for webpages similar to a given URL."),
            Tool(name="get_contents", func=self.get_contents, description="Get the contents of webpages given their URLs."),
            Tool(name="search_companies", func=self.search_companies, description="Search for information about companies in the specified field based on the query.")
        ]

    def _exa(self):
        return Exa(api_key=os.environ.get('EXA_API_KEY'))