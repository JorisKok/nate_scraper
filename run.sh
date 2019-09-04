# We always need to rebuild to use the latest scraper.py
docker build -t nate_scraper .
docker run -it --rm --name nate_scraper nate_scraper

