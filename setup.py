{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bdc54867-9958-479d-9284-84a3a2cf0930",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'tuple' object has no attribute 'tb_frame'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mGetoptError\u001b[0m                               Traceback (most recent call last)",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\setuptools\\_distutils\\fancy_getopt.py:246\u001b[0m, in \u001b[0;36mFancyGetopt.getopt\u001b[1;34m(self, args, object)\u001b[0m\n\u001b[0;32m    245\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 246\u001b[0m     opts, args \u001b[38;5;241m=\u001b[39m getopt\u001b[38;5;241m.\u001b[39mgetopt(args, short_opts, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlong_opts)\n\u001b[0;32m    247\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m getopt\u001b[38;5;241m.\u001b[39merror \u001b[38;5;28;01mas\u001b[39;00m msg:\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\getopt.py:95\u001b[0m, in \u001b[0;36mgetopt\u001b[1;34m(args, shortopts, longopts)\u001b[0m\n\u001b[0;32m     94\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m---> 95\u001b[0m         opts, args \u001b[38;5;241m=\u001b[39m do_shorts(opts, args[\u001b[38;5;241m0\u001b[39m][\u001b[38;5;241m1\u001b[39m:], shortopts, args[\u001b[38;5;241m1\u001b[39m:])\n\u001b[0;32m     97\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m opts, args\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\getopt.py:195\u001b[0m, in \u001b[0;36mdo_shorts\u001b[1;34m(opts, optstring, shortopts, args)\u001b[0m\n\u001b[0;32m    194\u001b[0m opt, optstring \u001b[38;5;241m=\u001b[39m optstring[\u001b[38;5;241m0\u001b[39m], optstring[\u001b[38;5;241m1\u001b[39m:]\n\u001b[1;32m--> 195\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m short_has_arg(opt, shortopts):\n\u001b[0;32m    196\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m optstring \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m:\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\getopt.py:211\u001b[0m, in \u001b[0;36mshort_has_arg\u001b[1;34m(opt, shortopts)\u001b[0m\n\u001b[0;32m    210\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m shortopts\u001b[38;5;241m.\u001b[39mstartswith(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m:\u001b[39m\u001b[38;5;124m'\u001b[39m, i\u001b[38;5;241m+\u001b[39m\u001b[38;5;241m1\u001b[39m)\n\u001b[1;32m--> 211\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m GetoptError(_(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124moption -\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m not recognized\u001b[39m\u001b[38;5;124m'\u001b[39m) \u001b[38;5;241m%\u001b[39m opt, opt)\n",
      "\u001b[1;31mGetoptError\u001b[0m: option -f not recognized",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mDistutilsArgError\u001b[0m                         Traceback (most recent call last)",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\setuptools\\_distutils\\core.py:172\u001b[0m, in \u001b[0;36msetup\u001b[1;34m(**attrs)\u001b[0m\n\u001b[0;32m    171\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 172\u001b[0m     ok \u001b[38;5;241m=\u001b[39m dist\u001b[38;5;241m.\u001b[39mparse_command_line()\n\u001b[0;32m    173\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m DistutilsArgError \u001b[38;5;28;01mas\u001b[39;00m msg:\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\setuptools\\_distutils\\dist.py:467\u001b[0m, in \u001b[0;36mDistribution.parse_command_line\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    466\u001b[0m parser\u001b[38;5;241m.\u001b[39mset_aliases({\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mlicence\u001b[39m\u001b[38;5;124m'\u001b[39m: \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mlicense\u001b[39m\u001b[38;5;124m'\u001b[39m})\n\u001b[1;32m--> 467\u001b[0m args \u001b[38;5;241m=\u001b[39m parser\u001b[38;5;241m.\u001b[39mgetopt(args\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mscript_args, \u001b[38;5;28mobject\u001b[39m\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m)\n\u001b[0;32m    468\u001b[0m option_order \u001b[38;5;241m=\u001b[39m parser\u001b[38;5;241m.\u001b[39mget_option_order()\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\setuptools\\_distutils\\fancy_getopt.py:248\u001b[0m, in \u001b[0;36mFancyGetopt.getopt\u001b[1;34m(self, args, object)\u001b[0m\n\u001b[0;32m    247\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m getopt\u001b[38;5;241m.\u001b[39merror \u001b[38;5;28;01mas\u001b[39;00m msg:\n\u001b[1;32m--> 248\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m DistutilsArgError(msg)\n\u001b[0;32m    250\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m opt, val \u001b[38;5;129;01min\u001b[39;00m opts:\n",
      "\u001b[1;31mDistutilsArgError\u001b[0m: option -f not recognized",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mSystemExit\u001b[0m                                Traceback (most recent call last)",
      "    \u001b[1;31m[... skipping hidden 1 frame]\u001b[0m\n",
      "Cell \u001b[1;32mIn[1], line 5\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msetuptools\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m setup, find_packages\n\u001b[1;32m----> 5\u001b[0m setup(\n\u001b[0;32m      6\u001b[0m     name\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mmy_scraper\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m      7\u001b[0m     version\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m0.1.0\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m      8\u001b[0m     packages\u001b[38;5;241m=\u001b[39mfind_packages(),\n\u001b[0;32m      9\u001b[0m     install_requires\u001b[38;5;241m=\u001b[39m[\n\u001b[0;32m     10\u001b[0m         \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mrequests\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m     11\u001b[0m         \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mbeautifulsoup4\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m     12\u001b[0m     ],\n\u001b[0;32m     13\u001b[0m     description\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mA simple web scraping library.\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m     14\u001b[0m     author\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mYour Name\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m     15\u001b[0m     author_email\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124myour.email@example.com\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m     16\u001b[0m     url\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mhttps://github.com/yourusername/my_scraper\u001b[39m\u001b[38;5;124m'\u001b[39m,  \u001b[38;5;66;03m# Update with your GitHub URL\u001b[39;00m\n\u001b[0;32m     17\u001b[0m     classifiers\u001b[38;5;241m=\u001b[39m[\n\u001b[0;32m     18\u001b[0m         \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mProgramming Language :: Python :: 3\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m     19\u001b[0m         \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mLicense :: OSI Approved :: MIT License\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m     20\u001b[0m         \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mOperating System :: OS Independent\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m     21\u001b[0m     ],\n\u001b[0;32m     22\u001b[0m     python_requires\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m>=3.6\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m     23\u001b[0m )\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\setuptools\\__init__.py:103\u001b[0m, in \u001b[0;36msetup\u001b[1;34m(**attrs)\u001b[0m\n\u001b[0;32m    102\u001b[0m _install_setup_requires(attrs)\n\u001b[1;32m--> 103\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m distutils\u001b[38;5;241m.\u001b[39mcore\u001b[38;5;241m.\u001b[39msetup(\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mattrs)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\setuptools\\_distutils\\core.py:174\u001b[0m, in \u001b[0;36msetup\u001b[1;34m(**attrs)\u001b[0m\n\u001b[0;32m    173\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m DistutilsArgError \u001b[38;5;28;01mas\u001b[39;00m msg:\n\u001b[1;32m--> 174\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mSystemExit\u001b[39;00m(gen_usage(dist\u001b[38;5;241m.\u001b[39mscript_name) \u001b[38;5;241m+\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124merror: \u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m%\u001b[39m msg)\n\u001b[0;32m    176\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m DEBUG:\n",
      "\u001b[1;31mSystemExit\u001b[0m: usage: ipykernel_launcher.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]\n   or: ipykernel_launcher.py --help [cmd1 cmd2 ...]\n   or: ipykernel_launcher.py --help-commands\n   or: ipykernel_launcher.py cmd --help\n\nerror: option -f not recognized",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "    \u001b[1;31m[... skipping hidden 1 frame]\u001b[0m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:2121\u001b[0m, in \u001b[0;36mInteractiveShell.showtraceback\u001b[1;34m(self, exc_tuple, filename, tb_offset, exception_only, running_compiled_code)\u001b[0m\n\u001b[0;32m   2118\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m exception_only:\n\u001b[0;32m   2119\u001b[0m     stb \u001b[38;5;241m=\u001b[39m [\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAn exception has occurred, use \u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124mtb to see \u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m   2120\u001b[0m            \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mthe full traceback.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m'\u001b[39m]\n\u001b[1;32m-> 2121\u001b[0m     stb\u001b[38;5;241m.\u001b[39mextend(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mInteractiveTB\u001b[38;5;241m.\u001b[39mget_exception_only(etype,\n\u001b[0;32m   2122\u001b[0m                                                      value))\n\u001b[0;32m   2123\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m   2125\u001b[0m     \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mcontains_exceptiongroup\u001b[39m(val):\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\ultratb.py:710\u001b[0m, in \u001b[0;36mListTB.get_exception_only\u001b[1;34m(self, etype, value)\u001b[0m\n\u001b[0;32m    702\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mget_exception_only\u001b[39m(\u001b[38;5;28mself\u001b[39m, etype, value):\n\u001b[0;32m    703\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Only print the exception type and message, without a traceback.\u001b[39;00m\n\u001b[0;32m    704\u001b[0m \n\u001b[0;32m    705\u001b[0m \u001b[38;5;124;03m    Parameters\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    708\u001b[0m \u001b[38;5;124;03m    value : exception value\u001b[39;00m\n\u001b[0;32m    709\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m--> 710\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m ListTB\u001b[38;5;241m.\u001b[39mstructured_traceback(\u001b[38;5;28mself\u001b[39m, etype, value)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\ultratb.py:568\u001b[0m, in \u001b[0;36mListTB.structured_traceback\u001b[1;34m(self, etype, evalue, etb, tb_offset, context)\u001b[0m\n\u001b[0;32m    565\u001b[0m     chained_exc_ids\u001b[38;5;241m.\u001b[39madd(\u001b[38;5;28mid\u001b[39m(exception[\u001b[38;5;241m1\u001b[39m]))\n\u001b[0;32m    566\u001b[0m     chained_exceptions_tb_offset \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0\u001b[39m\n\u001b[0;32m    567\u001b[0m     out_list \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m--> 568\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mstructured_traceback(\n\u001b[0;32m    569\u001b[0m             etype,\n\u001b[0;32m    570\u001b[0m             evalue,\n\u001b[0;32m    571\u001b[0m             (etb, chained_exc_ids),  \u001b[38;5;66;03m# type: ignore\u001b[39;00m\n\u001b[0;32m    572\u001b[0m             chained_exceptions_tb_offset,\n\u001b[0;32m    573\u001b[0m             context,\n\u001b[0;32m    574\u001b[0m         )\n\u001b[0;32m    575\u001b[0m         \u001b[38;5;241m+\u001b[39m chained_exception_message\n\u001b[0;32m    576\u001b[0m         \u001b[38;5;241m+\u001b[39m out_list)\n\u001b[0;32m    578\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m out_list\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\ultratb.py:1435\u001b[0m, in \u001b[0;36mAutoFormattedTB.structured_traceback\u001b[1;34m(self, etype, evalue, etb, tb_offset, number_of_lines_of_context)\u001b[0m\n\u001b[0;32m   1433\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m   1434\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mtb \u001b[38;5;241m=\u001b[39m etb\n\u001b[1;32m-> 1435\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m FormattedTB\u001b[38;5;241m.\u001b[39mstructured_traceback(\n\u001b[0;32m   1436\u001b[0m     \u001b[38;5;28mself\u001b[39m, etype, evalue, etb, tb_offset, number_of_lines_of_context\n\u001b[0;32m   1437\u001b[0m )\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\ultratb.py:1326\u001b[0m, in \u001b[0;36mFormattedTB.structured_traceback\u001b[1;34m(self, etype, value, tb, tb_offset, number_of_lines_of_context)\u001b[0m\n\u001b[0;32m   1323\u001b[0m mode \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mmode\n\u001b[0;32m   1324\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m mode \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mverbose_modes:\n\u001b[0;32m   1325\u001b[0m     \u001b[38;5;66;03m# Verbose modes need a full traceback\u001b[39;00m\n\u001b[1;32m-> 1326\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m VerboseTB\u001b[38;5;241m.\u001b[39mstructured_traceback(\n\u001b[0;32m   1327\u001b[0m         \u001b[38;5;28mself\u001b[39m, etype, value, tb, tb_offset, number_of_lines_of_context\n\u001b[0;32m   1328\u001b[0m     )\n\u001b[0;32m   1329\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m mode \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mMinimal\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[0;32m   1330\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m ListTB\u001b[38;5;241m.\u001b[39mget_exception_only(\u001b[38;5;28mself\u001b[39m, etype, value)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\ultratb.py:1173\u001b[0m, in \u001b[0;36mVerboseTB.structured_traceback\u001b[1;34m(self, etype, evalue, etb, tb_offset, number_of_lines_of_context)\u001b[0m\n\u001b[0;32m   1164\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mstructured_traceback\u001b[39m(\n\u001b[0;32m   1165\u001b[0m     \u001b[38;5;28mself\u001b[39m,\n\u001b[0;32m   1166\u001b[0m     etype: \u001b[38;5;28mtype\u001b[39m,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   1170\u001b[0m     number_of_lines_of_context: \u001b[38;5;28mint\u001b[39m \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m5\u001b[39m,\n\u001b[0;32m   1171\u001b[0m ):\n\u001b[0;32m   1172\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Return a nice text document describing the traceback.\"\"\"\u001b[39;00m\n\u001b[1;32m-> 1173\u001b[0m     formatted_exception \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mformat_exception_as_a_whole(etype, evalue, etb, number_of_lines_of_context,\n\u001b[0;32m   1174\u001b[0m                                                            tb_offset)\n\u001b[0;32m   1176\u001b[0m     colors \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mColors  \u001b[38;5;66;03m# just a shorthand + quicker name lookup\u001b[39;00m\n\u001b[0;32m   1177\u001b[0m     colorsnormal \u001b[38;5;241m=\u001b[39m colors\u001b[38;5;241m.\u001b[39mNormal  \u001b[38;5;66;03m# used a lot\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\ultratb.py:1063\u001b[0m, in \u001b[0;36mVerboseTB.format_exception_as_a_whole\u001b[1;34m(self, etype, evalue, etb, number_of_lines_of_context, tb_offset)\u001b[0m\n\u001b[0;32m   1060\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(tb_offset, \u001b[38;5;28mint\u001b[39m)\n\u001b[0;32m   1061\u001b[0m head \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprepare_header(\u001b[38;5;28mstr\u001b[39m(etype), \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlong_header)\n\u001b[0;32m   1062\u001b[0m records \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m-> 1063\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mget_records(etb, number_of_lines_of_context, tb_offset) \u001b[38;5;28;01mif\u001b[39;00m etb \u001b[38;5;28;01melse\u001b[39;00m []\n\u001b[0;32m   1064\u001b[0m )\n\u001b[0;32m   1066\u001b[0m frames \u001b[38;5;241m=\u001b[39m []\n\u001b[0;32m   1067\u001b[0m skipped \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0\u001b[39m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\ultratb.py:1131\u001b[0m, in \u001b[0;36mVerboseTB.get_records\u001b[1;34m(self, etb, number_of_lines_of_context, tb_offset)\u001b[0m\n\u001b[0;32m   1129\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m cf \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m   1130\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m-> 1131\u001b[0m         mod \u001b[38;5;241m=\u001b[39m inspect\u001b[38;5;241m.\u001b[39mgetmodule(cf\u001b[38;5;241m.\u001b[39mtb_frame)\n\u001b[0;32m   1132\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m mod \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m   1133\u001b[0m             mod_name \u001b[38;5;241m=\u001b[39m mod\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__name__\u001b[39m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'tuple' object has no attribute 'tb_frame'"
     ]
    }
   ],
   "source": [
    "# setup.py\n",
    "\n",
    "from setuptools import setup, find_packages\n",
    "\n",
    "setup(\n",
    "    name='my_scraper',\n",
    "    version='0.1.0',\n",
    "    packages=find_packages(),\n",
    "    install_requires=[\n",
    "        'requests',\n",
    "        'beautifulsoup4',\n",
    "    ],\n",
    "    description='A simple web scraping library.',\n",
    "    author='Your Name',\n",
    "    author_email='your.email@example.com',\n",
    "    url='https://github.com/yourusername/my_scraper',  # Update with your GitHub URL\n",
    "    classifiers=[\n",
    "        'Programming Language :: Python :: 3',\n",
    "        'License :: OSI Approved :: MIT License',\n",
    "        'Operating System :: OS Independent',\n",
    "    ],\n",
    "    python_requires='>=3.6',\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "566d7b9e-1444-4fe9-a2fe-504ca22cbab9",
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
