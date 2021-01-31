let arr = []
let purpose = ''

function createProfile() {
    chrome.tabs.create({
        url: './views/profile.html',
    })
}

function createSearchResults() {
    chrome.tabs.create({
        url: './views/search.html',
    })
}

function checkDB(data) {
    axios.get(`http://127.0.0.1:8000/api/?search=${data.scholarName}+${data.workplace}`).then((response) => {
        const request = data
        if (response.data[0] === undefined) {
            axios
                .post('http://127.0.0.1:8000/api/', {
                    scholarName: request.scholarName,
                    scholarImage: request.scholarImage,
                    workplace: request.workplace,
                    website: request.website,
                    country: request.country,
                    pubCount: request.pubCount,
                    citCount: request.citCount,
                    hIndex: request.hIndex,
                    gIndex: request.gIndex,
                    mIndex: request.mIndex,
                    oIndex: request.oIndex,
                    eIndex: request.eIndex,
                    hMedian: request.hMedian,
                    sIndex: request.sIndex,
                    TNCc: request.TNCc,
                    titles: request.titles,
                    coauthors: request.coauthors,
                    citations: request.citations,
                    nCitations: request.nCitations,
                    years: request.years,
                })
                .catch((error) => console.log(error))
        } else {
            const { id } = response.data[0]
            axios
                .put(`http://127.0.0.1:8000/api/${id}/`, {
                    scholarName: request.scholarName,
                    scholarImage: request.scholarImage,
                    workplace: request.workplace,
                    website: request.website,
                    country: request.country,
                    pubCount: request.pubCount,
                    citCount: request.citCount,
                    hIndex: request.hIndex,
                    gIndex: request.gIndex,
                    mIndex: request.mIndex,
                    oIndex: request.oIndex,
                    eIndex: request.eIndex,
                    hMedian: request.hMedian,
                    sIndex: request.sIndex,
                    TNCc: request.TNCc,
                    titles: request.titles,
                    coauthors: request.coauthors,
                    citations: request.citations,
                    nCitations: request.nCitations,
                    years: request.years,
                })
                .catch((error) => console.log(error))
        }
    })
}

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.intent === 'profileView') {
        arr = request
        purpose = 'calculateData'
        createProfile()
    }
    if (request.intent === 'search') {
        const searchTerm = request.searchTerm.split(' ').join('+')
        axios.get(`http://127.0.0.1:8000/api?search=${searchTerm}`).then((response) => {
            if (response.data.length === 1) {
                arr = response
                purpose = 'displayData'
                createProfile()
            } else {
                arr = response
                purpose = 'searchResults'
                createSearchResults()
            }
        })
    }
    if (request.intent === 'createProfile') {
        arr = request.data
        purpose = 'showData'
        createProfile()
    }
    if (request === 'fetchSearchResults') {
        sendResponse({
            data: arr,
            intent: purpose,
        })
    }
    if (request === 'fromProfileJs') {
        sendResponse({
            data: arr,
            intent: purpose,
        })
    }
    if (request.intent === 'sendToServer') {
        sendResponse(request)
        checkDB(request)
    }
    if (request.intent === 'checkStarred') {
        axios.get(`http://127.0.0.1:8000/api/?search=${request.name}+${request.work}`).then((response) => {
            if (response.data[0] !== undefined && response.data[0].isStarred) {
                sendResponse({ isStarred: 'true' })
            } else {
                sendResponse({ isStarred: 'false' })
            }
        })
    }
    if (request.intent === 'saveStarred') {
        axios
            .get(`http://127.0.0.1:8000/api/?search=${request.name}+${request.work}`)
            .then((response) => {
                return response.data[0].id
            })
            .then((id) => {
                axios.put(`http://127.0.0.1:8000/api/${id}/`, {
                    isStarred: true,
                })
            })
    }
    if (request.intent === 'deleteStarred') {
        axios
            .get(`http://127.0.0.1:8000/api/?search=${request.name}+${request.work}`)
            .then((response) => {
                return response.data[0].id
            })
            .then((id) => {
                axios.put(`http://127.0.0.1:8000/api/${id}/`, {
                    isStarred: false,
                })
            })
    }
    if (request === 'fetchStarred') {
        axios.get('http://127.0.0.1:8000/api/?search=true').then((data) => {
            sendResponse(data)
        })
    }
    return true
})
