function getTotalCitations(citations) {
    let sumCitations = 0
    for (let i = 0; i < citations.length; i++) {
        if (citations[i] != '') {
            sumCitations += parseInt(citations[i])
        }
    }
    return sumCitations
}
function getHindex(citations) {
    let hIndex = 0
    for (let i = 0; i < citations.length; i++) {
        if (i + 1 >= citations[i]) {
            hIndex = i + 1
            break
        }
    }
    return hIndex
}
function getGindex(citations) {
    let totalCitations = 0
    let gIndex = 0
    for (let i = 0; i < citations.length; i++) {
        totalCitations += parseInt(citations[i])
        if (Math.pow(i + 1, 2) <= totalCitations) {
            gIndex = i + 1
        } else {
            break
        }
    }
    return gIndex
}
function getMindex(years) {
    let mIndex = 0
    currentYear = new Date().getFullYear()
    const firstPubYear = years.filter(Number).reduce((a, b) => Math.min(a, b))
    timeGap = currentYear - (parseInt(firstPubYear) + 1)
    mIndex = (hIndex / timeGap).toFixed(2)
    return mIndex
}
function getOindex(citations, hIndex) {
    let oIndex = 0
    let maxCitation = 0
    maxCitation = citations.reduce((a, b) => Math.max(a, b))
    const product = hIndex * maxCitation
    oIndex = Math.pow(product, 1 / 2).toFixed(2)
    return oIndex
}
function getHmedian(citations, hIndex) {
    const hCore = []
    let hMedian = 0
    citations.forEach((el) => {
        if (el > hIndex) {
            hCore.push(el)
        }
    })
    function median(values) {
        if (values.length === 0) {
            return 0
        }

        values.sort(function (a, b) {
            return a - b
        })

        const half = Math.floor(values.length / 2)

        if (values.length % 2) return values[half]

        return (values[half - 1] + values[half]) / 2.0
    }
    hMedian = median(hCore)
    return hMedian
}
function getEindex(citations, hIndex) {
    let sumCitations = 0
    for (let i = 0; i < citations.length; i++) {
        if (citations[i] != '') {
            sumCitations += parseInt(citations[i])
        }
    }
    return parseFloat(Math.pow(sumCitations - Math.pow(hIndex, 2), 1 / 2).toFixed(2))
}
function getSindex(titles, citations, years) {
    sc = []
    sIndex = 0
    for (let i = 0; i < titles.length; i++) {
        if (citations[i] != '' && years[i] != '') {
            const temp = currentYear - parseInt(years[i]) + 1
            if (temp <= 5) {
                sc.push((5 / temp) * parseInt(citations[i]))
            }
            sc.push(parseInt(citations[i]))
        }
    }
    for (let i = 0; i < sc.length; i++) {
        if (i + 1 >= sc[i]) {
            sIndex = i + 1
            break
        }
    }
    return sIndex
}
function getTncc(data, newnCitations) {
    let sumNCitations = 0
    for (let i = 0; i < newnCitations.length; i++) {
        sumNCitations += newnCitations[i]
    }
    return Math.round(sumNCitations * (24.66 / data) * 100) / 100
}
function getNcitations(citations, sanitized) {
    const nCitations = []
    for (let i = 0; i < citations.length; i++) {
        if (citations != '') {
            nCitations.push(Math.round(parseInt(citations[i]) / sanitized[i]))
        }
    }
    return nCitations
}
function getCitPerDoc(country) {
    return new Promise(function (resolve) {
        const url = '../lib/scimagojr.xlsx'
        const req = new XMLHttpRequest()
        req.open('GET', url, true)
        req.responseType = 'arraybuffer'
        req.onload = () => {
            const data = new Uint8Array(req.response)
            const workbook = XLSX.read(data, {
                type: 'array',
            })
            const first_sheet_name = workbook.SheetNames[0]
            const worksheet = workbook.Sheets[first_sheet_name]
            const excelData = XLSX.utils.sheet_to_json(worksheet, {
                raw: true,
            })
            for (let i = 0; i < excelData.length; i++) {
                if (excelData[i].Country === country) {
                    resolve(excelData[i]['Citations per document'])
                }
            }
        }
        req.send()
    })
}
document.addEventListener('DOMContentLoaded', function () {
    function appendToPage(response) {
        const { titles, citations, coauthors, years, nCitations } = response
        console.log(country, website)
        for (let i = 0; i < response.pubCount; i++) {
            if (citations[i] === undefined) {
                citations[i] = ''
            }
            if (years[i] === undefined) {
                years[i] = ''
            }
            if (nCitations[i] === undefined) {
                nCitations[i] = ''
            }
        }

        // Bind data to profile template
        document.getElementById('scholarImage').setAttribute('src', response.scholarImage)
        document.getElementById('scholarName').innerText = response.scholarName
        document.getElementById('workplace').innerText = response.workplace
        document.getElementById('website').setAttribute('href', response.website)
        document.getElementById('country').innerText = response.country
        document.getElementById('pubCount').innerText = response.pubCount
        document.getElementById('citCount').innerText = response.citCount
        document.getElementById('hIndex').innerText = response.hIndex
        document.getElementById('gIndex').innerText = response.gIndex
        document.getElementById('mIndex').innerText = response.mIndex
        document.getElementById('oIndex').innerText = response.oIndex
        document.getElementById('hMedian').innerText = response.hMedian
        document.getElementById('eIndex').innerText = response.eIndex
        document.getElementById('sIndex').innerText = response.sIndex
        document.getElementById('sIndex').innerText = response.sIndex
        document.getElementById('TNCc').innerText = response.TNCc

        let currentPage = 1
        sendData(currentPage)

        function scrollHandler() {
            const wrap = document.getElementById('tbody')
            const height = wrap.offsetHeight
            const yoffset = window.pageYOffset
            const y = yoffset + window.innerHeight
            if (y > height) {
                currentPage += 1
                sendData(currentPage)
            }
        }
        window.onscroll = scrollHandler

        function sendData(page) {
            const pagenumber = page
            const startrow = (pagenumber - 1) * 10 + 1
            const endrow = pagenumber * 10
            for (let c = startrow; c < endrow; c++) {
                if (titles[c] !== undefined) {
                    const thead = document.getElementById('tbody')
                    const tr = document.createElement('tr')
                    let titletd = document.createElement('td')
                    titletd.innerText = titles[c]
                    tr.appendChild(titletd)
                    let cittd = document.createElement('td')
                    cittd.innerText = citations[c]
                    tr.appendChild(cittd)
                    let coauthtd = document.createElement('td')
                    coauthtd.innerText = coauthors[c]
                    tr.appendChild(coauthtd)
                    let ncittd = document.createElement('td')
                    ncittd.innerText = nCitations[c]
                    tr.appendChild(ncittd)
                    let yrtd = document.createElement('td')
                    yrtd.innerText = years[c]
                    tr.appendChild(yrtd)
                    thead.appendChild(tr)
                }
            }
        }

        // Visualise Chart
        graphYears = []
        presentYear = new Date().getFullYear()
        for (var i = presentYear - 10; i <= presentYear; i++) {
            graphYears.push(i)
        }
        var dict = {}
        for (x of graphYears) {
            count = 0
            for (y of years) {
                if (x == y) {
                    count++
                }
            }
            dict[x] = count
        }

        newDict = {}
        for (i of graphYears) {
            sum = 0
            for (var j = 0; j < response.pubCount; j++) {
                if (i == years[j]) {
                    if (citations[j] != '') {
                        sum += parseInt(citations[j])
                    }
                }
            }
            newDict[i] = sum
        }

        graphCitations = Object.values(newDict)
        graphPublications = Object.values(dict)
        let myChart = document.getElementById('myChart').getContext('2d')
        new Chart(myChart, {
            type: 'bar',

            // Dataset
            data: {
                labels: graphYears,
                datasets: [
                    {
                        label: 'Publications/ Year',
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgb(255, 99, 132)',
                        data: graphPublications,
                    },
                    {
                        label: 'Citations/ Year',
                        backgroundColor: 'rgb(231, 203, 138)',
                        borderColor: 'rgb(231, 203, 138)',
                        data: graphCitations,
                    },
                ],
            },

            // Configuration options
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    xAxes: [
                        {
                            stacked: true,
                        },
                    ],
                    yAxes: [
                        {
                            stacked: false,
                            ticks: {
                                beginAtZero: true,
                            },
                        },
                    ],
                },
            },
        })
    }

    chrome.runtime.sendMessage('fromProfileJs', function (response) {
        if (response.intent === 'calculateData') {
            response = response.data
            newCoAuthors = []
            demoDict = {}

            for (let i = 0; i < response.coAuthors.length; i++) {
                if (typeof response.coAuthors[i] !== 'number') {
                    newCoAuthors.push(response.coAuthors[i])
                }
            }

            const sanitized = []

            const promises = []
            for (let i = 0; i < newCoAuthors.length; i++) {
                promises.push(
                    window.axios.get(`https://scholar.google.com${newCoAuthors[i]}`).then((response) => {
                        const htmlData = response.data
                        const newString = htmlData.slice(
                            htmlData.lastIndexOf(
                                '<div id="gsc_vcd_table"><div class="gs_scl"><div class="gsc_vcd_field">Authors</div><div class="gsc_vcd_value">'
                            ) + 111,
                            htmlData.length
                        )
                        const count = newString.slice(0, newString.indexOf('</div></div>')).split(',').length
                        const url = response.config.url.slice(26, response.config.url.length)
                        demoDict[url] = count
                    })
                )
            }

            Promise.all(promises).then(() => {
                for (let n = 0; n < response.coAuthors.length; n++) {
                    if (typeof response.coAuthors[n] === 'number') {
                        sanitized.push(response.coAuthors[n])
                    } else {
                        for (const key in demoDict) {
                            if (key === response.coAuthors[n]) {
                                sanitized.push(demoDict[key])
                            }
                        }
                    }
                }

                // Compute metrics
                const { titles, citations, years, country, website } = response
                citations.sort(function (a, b) {
                    return b - a
                })

                hIndex = getHindex(citations)
                gIndex = getGindex(citations)
                mIndex = getMindex(years)
                oIndex = getOindex(citations, hIndex)
                hMedian = getHmedian(citations, hIndex)
                eIndex = getEindex(citations, hIndex)
                sIndex = getSindex(titles, citations, years)
                nCitations = getNcitations(citations, sanitized)
                sumCitations = getTotalCitations(citations)
                newCitations = response.citations.filter(Number)
                newYears = response.years.filter(Number)
                newnCitations = nCitations.filter(Number)
                getCitPerDoc(country)
                    .then((data) => getTncc(data, newnCitations))
                    .then((TNCc) => {
                        chrome.runtime.sendMessage(
                            {
                                intent: 'sendToServer',
                                scholarImage: response.image,
                                scholarName: response.scholarName,
                                workplace: response.workplace,
                                website: website,
                                country: country,
                                pubCount: response.titles.length,
                                citCount: sumCitations,
                                hIndex: hIndex,
                                gIndex: gIndex,
                                mIndex: mIndex,
                                oIndex: oIndex,
                                hMedian: hMedian,
                                eIndex: eIndex,
                                sIndex: sIndex,
                                titles: response.titles,
                                citations: newCitations,
                                nCitations: newnCitations,
                                TNCc: TNCc,
                                coauthors: sanitized,
                                years: newYears,
                            },
                            function (response) {
                                appendToPage(response)
                            }
                        )
                    })
            })
        }

        if (response.intent === 'displayData') {
            appendToPage(response.data.data[0])
        }
    })
})
module.exports = { getHindex, getEindex }
