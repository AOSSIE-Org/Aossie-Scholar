chrome.runtime.onMessage.addListener(function(request,sender,sendResponse){
    if(request.intent=='showRegPanel'){
        const div = document.getElementById('gsc_prf_in')
        const authorName = div.innerHTML
        sendResponse({content:authorName})                                              //Response sent only when on Scholar website
    }
})