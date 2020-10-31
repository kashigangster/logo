C = "\033[94;m"
G = "\033[92;m"
r = "\033[0;m"
P = "\033[93;m"
M = "\033[91;m"
def banner():
    print(f"""
{C}___  _______________ 
{C}|  \/  || ___ \  ___| {r}[ {G}MULTI BRUTE FORCE {r}]
{C}| .  . || |_/ / |_  {r}AUTHOR   {r}: KASHI ARAIN
{C}| |\/| || ___ \  _| {Whtsapp Num   {r}:+923062045786
{C}| |  | || |_/ / |   {C}GIFT FOR{r}:PUBG and FREE FIRE 
{C}\_|  |_/\____/\_|   {M}YOUTUBE  {r}:KASHI-TEACH
            """
CorrectUsername = "Speedi"
CorrectPassword = "Kashi"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;97mUSER NAME \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;97mPASWORD \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCUJSOqxjU4f9npLso-10Fuw')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCUJSOqxjU4f9npLso-10Fuw')
def menu():
    print(f"{G}1{r} Crack From Friendlist")
    print(f"{G}2{r} Crack From Likes On Post,PUBG")
    print(f"{G}3{r} Crack By Search Name")
    print(f"{G}4{r} Crack From Group (Only Takes 100 User)")
    print(f"{G}5{r} Crack From Friend Friendlist")
    print(f"{G}6{r} Crack From Hashtag")
    print(f"{G}7{r} Crack Re-check Result")
