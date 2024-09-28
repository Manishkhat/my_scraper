{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "abb7ae21-e7b8-40c5-bee8-923dfac1a398",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'my_scraper'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# tests/test_scraper.py\u001b[39;00m\n\u001b[1;32m----> 3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mmy_scraper\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m scrape_website\n\u001b[0;32m      5\u001b[0m \u001b[38;5;66;03m# Replace 'http://example.com' with the URL you want to test\u001b[39;00m\n\u001b[0;32m      6\u001b[0m url \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mhttp://example.com\u001b[39m\u001b[38;5;124m'\u001b[39m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'my_scraper'"
     ]
    }
   ],
   "source": [
    "# tests/test_scraper.py\n",
    "\n",
    "from my_scraper import scrape_website\n",
    "\n",
    "# Replace 'http://example.com' with the URL you want to test\n",
    "url = 'http://example.com'\n",
    "\n",
    "# Call the scrape function and print the result\n",
    "title = scrape_website(url)\n",
    "print(f\"The title of the page is: {title}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "615f7df4-9a01-4caa-ad21-909e9064670e",
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
