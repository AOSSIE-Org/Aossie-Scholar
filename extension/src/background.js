chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.intent = 'profileView') {

        // Compute metrics
        var citations = request.citations
        citations.sort(function(a, b){return b-a})
        var years = request.years

        //h-index
        var hIndex=""
        for(var i=0;i<citations.length;i++){
            if(i+1>=citations[i]){
                hIndex=i+1
                break
            }
        }
        console.log('h-index '+hIndex)

        //g-index
        var totalCitations=0
        var gIndex=""
        for(var i=0;i<citations.length;i++){
            totalCitations+=citations[i]
            if(Math.pow(i+1,2)<=totalCitations){
                gIndex=i+1
            }
            else{
                break
            }
        }
        console.log('g-index '+gIndex)

        //m-index
        var mIndex=0
        currentYear = new Date().getFullYear()
        var firstPubYear= (years.filter(Number)).reduce((a,b)=>Math.min(a,b))
        timeGap = currentYear-(parseInt(firstPubYear)+1)
        mIndex = (hIndex/timeGap).toFixed(2)
        console.log('m-index '+mIndex)

        //o-index
        // maxCitation = citations.reduce((a,b)=>Math.max(a,b))
        // console.log(maxCitation)

        chrome.tabs.create({url: './views/profile.html'}, function () {
            chrome.tabs.executeScript(null, {file: './js/profile.js'},function (e) {
                    if (e == chrome.runtime.lastError) {
                        // The extension isnt supposed to work on chrome://extensions URL
                    }
                    chrome.runtime.sendMessage(null, {scriptOptions: request})
            })
        })
    }
})