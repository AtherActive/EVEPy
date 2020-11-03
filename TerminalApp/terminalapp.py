#Created by IAmSalt Salty

import settings
import main as api
import TerminalApp.terminal_messages as msg


def PrintData(id):
    url = 'https://evemarketer.com/types/{}'.format(api.PullDataFromAPI(id).itemID)

# Due to a bug I have to request the data again for every field. Otherwise it for some reason cannot read data.
# A fix is coming later once Flutter is up and running.
    print('''
****************-Market Info-****************
   Processed Item: {}
   Name:           {}              
                                   
   Buy Orders:                     
       Average:{:,}                  
       Volume: {:,}
       Max:    {:,}
       Min:    {:,}                  
                                   
   Sell Orders:                    
       Average:{:,}                  
       Volume: {:,}
       Max:    {:,}
       Min:    {:,}    
       
   URL: {}                                           
****************-Market Info-****************
'''
          .format(
        api.PullDataFromAPI(id).itemID,
        api.PullDataFromAPI(id).friendlyName,

        api.PullDataFromAPI(id).buyValues.avgPrice,
        api.PullDataFromAPI(id).buyValues.volume,
        api.PullDataFromAPI(id).buyValues.maxPrice,
        api.PullDataFromAPI(id).buyValues.minPrice,
        api.PullDataFromAPI(id).sellValues.avgPrice,
        api.PullDataFromAPI(id).sellValues.volume,
        api.PullDataFromAPI(id).sellValues.maxPrice,
        api.PullDataFromAPI(id).sellValues.minPrice,
        url
                  )
    )


def retry():
    choice = input(msg.retry)
    if choice == 'y':
        app_start()
    else:
        exit(0)

def app_pre():
    api.ImportMarketData()
    return

def app_start():
    print(msg.startup)
    id = -1

    name = input(msg.inputValue)

    print(msg.loading)
    try:
        PrintData(name)
    except:
        print('''
        *************************************************
        *An error occurred. Did you spell the name right?*
        *************************************************
        ''')
        app_start()

    retry()
    return 0


app_pre()
app_start()
