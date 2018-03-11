import praw, re, os, time, webbrowser, pyautogui

r = praw.Reddit(client_id='',client_secret='',user_agent='',username='',password='') #fill this up according to your api access tokens

for submission in r.subreddit('all').stream.comments(): #add subreddits in this line separated by + symbol or just make it 'all'
 
    # Print the name of the OP, if you want to.
    #print(submission.author)
 
    # Find all things that look like Steam keys.  
    m = re.findall('[a-zA-Z0-9]{4,6}\-[a-zA-Z0-9]{4,6}\-[a-zA-Z0-9]{4,6}', submission.body)
 
    # Print out the matches, if you want to.
    #print (m)

    # Activate key
    try:
        n='https://store.steampowered.com/account/registerkey?key='+m[0]
        print(n)
        webbrowser.open_new_tab(n)
        time.sleep(3)
        x=pyautogui.locateCenterOnScreen('butt.png',grayscale=False)
        pyautogui.click(x)
        time.sleep(1)
        y=pyautogui.locateCenterOnScreen('continue.png',grayscale=False)
        time.sleep(1)
        pyautogui.click(y)
    except:
        pass
