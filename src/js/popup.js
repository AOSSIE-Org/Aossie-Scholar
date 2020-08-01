document.addEventListener('DOMContentLoaded', function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { intent: 'showRegPanel' }, function (response) {
            if (response) {
                // Show register panel on truthy response
                const regDiv = document.getElementById('registerDiv')
                const nameInput = document.getElementById('regNameInput')

                axios
                    .get('https://restcountries.eu/rest/v2/all?fields=name') // Fetch from API and iterate adding options
                    .then((res) => res.json())
                    .then((data) => {
                        for (let i = 0; i < data.length; i++) {
                            const regSelect = document.getElementById('regCountryInput')
                            const regOption = document.createElement('option')
                            regOption.innerHTML = data[i].name
                            regOption.value = data[i].name
                            regSelect.options.add(regOption)
                        }
                    })
                    .catch((error) => {
                        console.log(error)
                    })

                nameInput.value = response.content
                regDiv.style.display = 'block'
            } else if (typeof response === 'undefined') {
                if (chrome.runtime.lastError) {
                    // We couldn't talk to the content script, it doesn't run on non-Scholar URLs
                }
            }
        })
    })

    document.getElementById('searchForm').addEventListener('submit', (e) => {
        e.preventDefault()
        const searchTerm = document.getElementById('searchInput').value
        chrome.runtime.sendMessage({
            intent: 'search',
            searchTerm: searchTerm,
        })
    })

    function scrape(country) {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {
                intent: 'scrape',
                country: country,
            })
        })
    }

    document.getElementById('regForm').addEventListener('submit', (e) => {
        e.preventDefault()
        const country = document.getElementById('regCountryInput').value
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.tabs.sendMessage(tabs[0].id, { intent: 'loadBtn' }, function (response) {
                if (response.status) {
                    scrape(country)
                }
            })
        })
    })
})
