{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d62e65ec-9f5f-4207-8f29-2e785f0f395c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Shashi Kamal Mishra\\AppData\\Local\\Temp\\ipykernel_20700\\601045175.py:1: FutureWarning: \n",
      "\n",
      "All support for the `google.generativeai` package has ended. It will no longer be receiving \n",
      "updates or bug fixes. Please switch to the `google.genai` package as soon as possible.\n",
      "See README for more details:\n",
      "\n",
      "https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md\n",
      "\n",
      "  import google.generativeai as genai\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello! How can I help you today?\n"
     ]
    }
   ],
   "source": [
    "import google.generativeai as genai\n",
    "\n",
    "genai.configure(api_key=\"A**********************\")\n",
    "\n",
    "model = genai.GenerativeModel(\"gemini-2.5-flash\")\n",
    "\n",
    "response = model.generate_content(\"Hello\")\n",
    "print(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2733d691-ea66-4bc9-9b32-7472f056504f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "IPv4: 216.239.34.223\n"
     ]
    }
   ],
   "source": [
    "import socket\n",
    "\n",
    "print(\"IPv4:\", socket.gethostbyname(\"generativelanguage.googleapis.com\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ef33731-d0fe-4c62-8ed7-ff19b1b996b1",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
