import webview

def on_shown():
    print('ππ’π€π¦π£π°π°π¬ ππ π£πΊ ππ©π΄π’π― ππ¦π·π΄ π΄π¦π₯π’π―π¨ π£π¦π³π«π’π­π’π― ...')
    
def on_closed():
    print('ππ’π€π¦π£π°π°π¬ ππ π£πΊ ππ©π΄π’π― ππ¦π·π΄ π£π¦π³π©π’π΄πͺπ­ π₯πͺπ΅πΆπ΅πΆπ± !')
webview.create_window('Facebook PC by Ihsan Devs', url='https://facebook.com', html='', js_api=None, width=800, height=600, \
                      x=None, y=None, resizable=True, fullscreen=False, \
                      min_size=(900, 500), hidden=False, frameless=False, \
                      minimized=False, on_top=False, confirm_close=True, \
                      background_color='#037bfc', text_select=False)

webview.start()