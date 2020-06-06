document.addEventListener('DOMContentLoaded', function () {
    chrome.tabs.query({active:true, currentWindow:true}, function(tabs){
        chrome.tabs.sendMessage(tabs[0].id,{intent:'showRegPanel'},function(response){
            if(response){                                                                                   //Show register panel on truthy response
                const regDiv = document.getElementById('registerDiv')
                regDiv.style.display = "block"
            }
            else if(typeof response == 'undefined'){
                if(chrome.runtime.lastError) {
                    // We couldn't talk to the content script, it doesn't run on non-Scholar URLs
                }
            }
        })
    })
})