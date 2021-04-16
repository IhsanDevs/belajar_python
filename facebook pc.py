import webview

def on_shown():
    print('𝘍𝘢𝘤𝘦𝘣𝘰𝘰𝘬 𝘗𝘊 𝘣𝘺 𝘐𝘩𝘴𝘢𝘯 𝘋𝘦𝘷𝘴 𝘴𝘦𝘥𝘢𝘯𝘨 𝘣𝘦𝘳𝘫𝘢𝘭𝘢𝘯 ...')
    
def on_closed():
    print('𝘍𝘢𝘤𝘦𝘣𝘰𝘰𝘬 𝘗𝘊 𝘣𝘺 𝘐𝘩𝘴𝘢𝘯 𝘋𝘦𝘷𝘴 𝘣𝘦𝘳𝘩𝘢𝘴𝘪𝘭 𝘥𝘪𝘵𝘶𝘵𝘶𝘱 !')
webview.create_window('Facebook PC by Ihsan Devs', url='https://facebook.com', html='', js_api=None, width=800, height=600, \
                      x=None, y=None, resizable=True, fullscreen=False, \
                      min_size=(900, 500), hidden=False, frameless=False, \
                      minimized=False, on_top=False, confirm_close=True, \
                      background_color='#037bfc', text_select=False)

webview.start()