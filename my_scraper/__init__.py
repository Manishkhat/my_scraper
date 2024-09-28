{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "20054555-2615-47e3-b839-df58ccd11fa0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# my_scraper/__init__.py\n",
    "\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "def scrape_website(url):\n",
    "    \"\"\"Scrapes the title of a website.\"\"\"\n",
    "    response = requests.get(url)\n",
    "    soup = BeautifulSoup(response.content, 'html.parser')\n",
    "    title = soup.title.string if soup.title else 'No title found'\n",
    "    return title\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bad59b8-671a-4475-b956-a978a5608b87",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
