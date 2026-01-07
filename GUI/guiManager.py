import webview

with open("index.html", "r") as file:
    htmlFile = file.read()

window = webview.create_window("Link Downloader", html=htmlFile, background_color="#000000") # confirm_close=True
webview.start()