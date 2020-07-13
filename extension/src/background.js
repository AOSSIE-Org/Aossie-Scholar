var arr=[]
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.intent == 'profileView') {
        arr=request
        chrome.tabs.create({ url: './views/profile.html' })
    }
        if(request=='fromProfileJs'){
            sendResponse(arr)
        }
})