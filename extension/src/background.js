chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.purpose = 'profileView') {

        // Compute metrics

        chrome.tabs.create({url: './views/profile.html'}, function () {
            chrome.tabs.executeScript(null, {file: 'profile.js'},function (e) {
                    if (e == chrome.runtime.lastError) {
                        // The extension isnt supposed to work on chrome://extensions URL
                    }
                    chrome.runtime.sendMessage(null, {scriptOptions: request})
            })
        })
    }
})