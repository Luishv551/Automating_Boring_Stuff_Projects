#! python3

# Multi Clipboard Program

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

#sys.argv = ['mclip.py', 'agree']

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - compy phrase text')
    sys.exit()

keyphrase = sys.argv[1] #First argument is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print ('Text for' + keyphrase + 'copied to clipboard.')
else:
    print ('There is no text for' + keyphrase)