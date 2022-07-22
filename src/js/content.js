let scholarName = ''

function scrapeData(country) {
    const titleArray = []
    const citArray = []
    const yrArray = []
    const coAuthorArray = []
    const titles = document.querySelectorAll('.gsc_a_at')
    const citations = document.querySelectorAll('.gsc_a_ac')
    const coAuthors = document.querySelectorAll('.gsc_a_tr .gsc_a_t')
    const years = document.getElementsByClassName('gsc_a_h gsc_a_hc gs_ibl')
    const img = document.getElementById('gsc_prf_pup-img').getAttribute('src')
    const workPlace = document.getElementsByClassName('gsc_prf_il')[0].innerText
    let website
    try {
        website = document.getElementById('gsc_prf_ivh').getElementsByTagName('a')[0].getAttribute('href')
    } catch (error) {
        website = undefined
    }

    for (let i = 0; i < titles.length; i++) {
        const title = titles[i].textContent
        const cit = citations[i].textContent
        const year = years[i].textContent
        titleArray.push(title)
        citArray.push(cit)
        yrArray.push(year)
        const authorsPerPublication = coAuthors[i].getElementsByClassName('gs_gray')[0].innerText
        if (authorsPerPublication.indexOf('...') === -1) {
            coAuthorArray.push(authorsPerPublication.split(',').length)
        } else {
            coAuthorArray.push(coAuthors[i].getElementsByClassName('gsc_a_at')[0].getAttribute('href'))
        }
    }
    chrome.runtime.sendMessage({
        intent: 'profileView',
        scholarName: scholarName,
        titles: titleArray,
        citations: citArray,
        years: yrArray,
        image: img,
        workplace: workPlace,
        website: website,
        country: country,
        coAuthors: coAuthorArray,
    })
}

// eslint-disable-next-line no-inner-declarations
function check() {
    setTimeout(function () {
        const btn = document.getElementById('gsc_bpf_more')
        if (btn.getAttribute('disabled') === null) {
            btn.click()
            check()
        } else {
            const selectcountry = document.getElementById('dropdownid').value
            scrapeData(selectcountry)
        }
    }, 1000)
}

window.onload = () => {
    scholarName = document.getElementById('gsc_prf_in').innerHTML
    const lineDiv = document.createElement('div')
    lineDiv.setAttribute('class', 'line-wrapper')
    const horizontalDiv = document.createElement('div')
    horizontalDiv.setAttribute('class', 'horizontal')
    const verticalDiv = document.createElement('div')
    verticalDiv.setAttribute('class', 'vertical')
    lineDiv.appendChild(horizontalDiv)
    lineDiv.appendChild(verticalDiv)
    const button = document.createElement('button')
    button.id = 'profileButton'
    button.appendChild(lineDiv)
    document.getElementById('gsc_prf_in').appendChild(button)
    const dropdown = document.createElement('select')
    dropdown.id = 'dropdownid'
    dropdown.setAttribute('class', 'classic')
    fetch('https://countriesnow.space/api/v0.1/countries/') // Fetch from API and iterate adding options
        .then((res) => res.json())
        .then((jsondata) => {
            array = jsondata.data
            for (let i = 0; i < array.length; i++) {
                const option = document.createElement('option')
                option.innerHTML = array[i].country
                option.value = array[i].country
                option.id = 'optionid'
                dropdown.appendChild(option)
            }
        })
        .catch((error) => {
            console.log(error)
        })
    document.getElementById('gsc_prf_in').appendChild(dropdown)
    document.getElementById('profileButton').addEventListener('click', function () {
        check()
    })
}
