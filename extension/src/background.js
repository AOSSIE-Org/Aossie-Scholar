chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.intent = 'profileView') {

        // Compute metrics
        var citations = request.citations
        citations.sort(function (a, b) { return b - a })
        var years = request.years

        //h-index
        var hIndex = 0
        for (var i = 0; i < citations.length; i++) {
            if (i + 1 >= citations[i]) {
                hIndex = i + 1
                break
            }
        }
        console.log('h-index ' + hIndex)

        //g-index
        var totalCitations = 0
        var gIndex = 0
        for (var i = 0; i < citations.length; i++) {
            totalCitations += parseInt(citations[i])
            if (Math.pow(i + 1, 2) <= totalCitations) {
                gIndex = i + 1
            }
            else {
                break
            }
        }
        console.log('g-index ' + gIndex)

        //m-index
        var mIndex = 0
        currentYear = new Date().getFullYear()
        var firstPubYear = (years.filter(Number)).reduce((a, b) => Math.min(a, b))
        timeGap = currentYear - (parseInt(firstPubYear) + 1)
        mIndex = (hIndex / timeGap).toFixed(2)
        console.log('m-index ' + mIndex)

        //o-index
        var oIndex = 0
        maxCitation = citations.reduce((a, b) => Math.max(a, b))
        var product = hIndex * maxCitation
        oIndex = Math.pow(product, (1 / 2)).toFixed(2)
        console.log('o-index '+oIndex)

        //h-median
        var hCore = []
        var hMedian = 0
        citations.forEach(el => {
            if (el > hIndex) {
                hCore.push(el)
            }
        })
        function median(values) {
            if (values.length === 0) return 0;

            values.sort(function (a, b) {
                return a - b;
            });

            var half = Math.floor(values.length / 2);

            if (values.length % 2)
                return values[half];

            return (values[half - 1] + values[half]) / 2.0;
        }
        hMedian = median(hCore)
        console.log('h-median '+hMedian)

        //e-index
        var sumCitations = 0
        for (var i = 0; i < citations.length; i++) {
            if (citations[i] != "") {
                sumCitations += parseInt(citations[i])
            }
        }
        var eIndex = ((sumCitations - (hIndex ** 2)) ** (1 / 2)).toFixed(2)
        console.log('e-index '+eIndex)

        chrome.tabs.create({ url: './views/profile.html' }, function () {
            chrome.tabs.executeScript(null, { file: './js/profile.js' }, function (e) {
                if (e == chrome.runtime.lastError) {
                    // The extension isnt supposed to work on chrome://extensions URL
                }
                chrome.runtime.sendMessage(null, { scriptOptions: request })
            })
        })
    }
})