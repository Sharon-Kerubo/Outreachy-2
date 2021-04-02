import pywikibot

#connect to wikidata
site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()

#Load and print out the page
def get_page(page):
    q_id = page.title()
    print(q_id)
    data = page.get()
    print(data)
    

#Add Hello to the end of the page
def add_hello(page):
    data = page.get()
    data = data + "\nHello"
    page.data = data
    try:
        page.save("Saving the updated page")
        return 1
    except:
        print("Updated Page not saved")
        return 0

#Add new property to the sandbox item('P31' = 'Q4115189')
def edit_wikidata(page, pid, val):
    #display title of the page
    title = page.title()
    print(title)

    #add property
    target_claim = pywikibot.ItemPage(repo, val)
    new_claim = pywikibot.Claim(repo, pid)
    new_claim.setTarget(target_claim)
    print(new_claim)
    #save the claim
    text = input('Save Edit?')
    if text == 'y':
        page.addClaim(new_claim, summary=u'Add claim')
    return 0
    
#pages to be loaded
outreachy1_page = pywikibot.Page(repo, 'User:Sharon Kerubo/Outreachy 1')
sandbox_page = pywikibot.ItemPage(repo, 'Q4115189') #Wikidata sandbox
#other pages from my aricle
Q42519_page = pywikibot.ItemPage(repo, 'Q42519') #Grey
Q185635_page = pywikibot.ItemPage(repo, 'Q185635') #Tusk

#To be added to the sandbox item
test_property = 'P31' #instance of
test_value = 'Q4115189' #box

#call the functions
get_page(outreachy1_page)
add_hello(outreachy1_page)

get_page(sandbox_page)
get_page(Q42519_page)
get_page(Q185635_page)

edit_wikidata(sandbox_page, test_property,test_value)