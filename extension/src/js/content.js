chrome.runtime.onMessage.addListener(function(request,sender,sendResponse){
    if(request.intent=='showRegPanel'){
        const div = document.getElementById('gsc_prf_in')
        const authorName = div.innerHTML
        sendResponse({content:authorName})                                              //Response sent only when on Scholar website
    }
    else if (request.intent == 'scrape') {
        var titleArray = []
        var citArray = []
        var yrArray = []
        var titles = document.querySelectorAll('.gsc_a_at')
        var citations = document.querySelectorAll('.gsc_a_ac')
        var years = document.getElementsByClassName('gsc_a_h gsc_a_hc gs_ibl')
        const img = document.getElementById('gsc_prf_pup-img').getAttribute('src')
        for (var i = 0; i < titles.length; i++) {
            var title = titles[i].textContent
            var cit = citations[i].textContent
            var year = years[i].textContent
            titleArray.push(title)
            citArray.push(cit)
            yrArray.push(year)
        }
        sendResponse({
            titles: titleArray,
            citations:citArray,
            years:yrArray,
            image:img
        })
    }
     else if (request.intent == 'loadBtn') {
        function check() {
            setTimeout(function () {
                var btn = document.getElementById('gsc_bpf_more')
                if (btn.getAttribute('disabled') == null) {
                    btn.click()
                    check()
                }
                 else{
                    sendResponse({status:"true"})
                }
            }, 2500)
        }
        check()
    }
    return true
})