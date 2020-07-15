var arr=[]
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.intent == 'profileView') {
        arr=request
        chrome.tabs.create({ url: './views/profile.html' })
    }
        if(request=='fromProfileJs'){
            sendResponse(arr)
        }
        if (request.intent == 'sendToServer') {
            axios.post('https://reqres.in/api/register',{
                "email": "eve.holt@reqres.in",
                "password": "pistol"    
            })
            .then((response)=>console.log(response))
            .catch((error)=>console.log(error,error.response))
        }
})