document.addEventListener('DOMContentLoaded', function profile() {
    function appendToPage(response) {
        var titles = response.titles
        var citations = response.citations
        var years = response.years
        for (var i = 0; i < response.pubCount; i++) {
            if (citations[i] == undefined) {
                citations[i] = ""
            }
            if (years[i] == undefined) {
                years[i] = ""
            }
        }

        //Bind data to profile template
        document.getElementById('scholarImage').setAttribute('src', response.scholarImage)
        document.getElementById('scholarName').innerText = response.scholarName
        document.getElementById('workplace').innerText = response.workplace
        document.getElementById('pubCount').innerText = response.pubCount
        document.getElementById('citCount').innerText = response.citCount
        document.getElementById('hIndex').innerText = response.hIndex
        document.getElementById('gIndex').innerText = response.gIndex
        document.getElementById('mIndex').innerText = response.mIndex
        document.getElementById('oIndex').innerText = response.oIndex
        document.getElementById('hMedian').innerText = response.hMedian
        document.getElementById('eIndex').innerText = response.eIndex
        for (var c = 0; c < response.pubCount; c++) {
            var thead = document.getElementById('tbody')
            var tr = document.createElement('tr')
            var td = document.createElement('td')
            td.innerText = titles[c]
            tr.appendChild(td)
            var td = document.createElement('td')
            td.innerText = citations[c]
            tr.appendChild(td)
            var td = document.createElement('td')
            td.innerText = years[c]
            tr.appendChild(td)
            thead.appendChild(tr)
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
                    if (citations[j] != "") {
                        sum += parseInt(citations[j])
                    }
                }
            }
            newDict[i] = sum
        }
        graphCitations = Object.values(newDict)
        graphPublications = Object.values(dict)
        let myChart = document.getElementById('myChart').getContext('2d')
        let barChart = new Chart(myChart, {
            type: 'bar',

            // Dataset
            data: {
                labels: graphYears,
                datasets: [{
                        label: 'Publications/ Year',
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgb(255, 99, 132)',
                        data: graphPublications
                    },
                    {
                        label: 'Citations/ Year',
                        backgroundColor: 'rgb(231, 203, 138)',
                        borderColor: 'rgb(231, 203, 138)',
                        data: graphCitations
                    }
                ]
            },

            // Configuration options
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    xAxes: [{
                        stacked: true
                    }],
                    yAxes: [{
                        stacked: false,
                        ticks: {
                            beginAtZero: true,
                        },
                    }]
                }
            }
        })

    }
    chrome.runtime.sendMessage('fromProfileJs', function (response) {
        if (response.intent == "calculateData") {
            response = response.data

            // Compute metrics
            var citations = response.citations
            citations.sort(function (a, b) {
                return b - a
            })
            var years = response.years

            //h-index
            var hIndex = 0
            for (var i = 0; i < citations.length; i++) {
                if (i + 1 >= citations[i]) {
                    hIndex = i + 1
                    break
                }
            }

            //g-index
            var totalCitations = 0
            var gIndex = 0
            for (var i = 0; i < citations.length; i++) {
                totalCitations += parseInt(citations[i])
                if (Math.pow(i + 1, 2) <= totalCitations) {
                    gIndex = i + 1
                } else {
                    break
                }
            }

            //m-index
            var mIndex = 0
            currentYear = new Date().getFullYear()
            var firstPubYear = (years.filter(Number)).reduce((a, b) => Math.min(a, b))
            timeGap = currentYear - (parseInt(firstPubYear) + 1)
            mIndex = (hIndex / timeGap).toFixed(2)

            //o-index
            var oIndex = 0
            maxCitation = citations.reduce((a, b) => Math.max(a, b))
            var product = hIndex * maxCitation
            oIndex = Math.pow(product, (1 / 2)).toFixed(2)

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

            //e-index
            var sumCitations = 0
            for (var i = 0; i < citations.length; i++) {
                if (citations[i] != "") {
                    sumCitations += parseInt(citations[i])
                }
            }
            var eIndex = ((sumCitations - (hIndex ** 2)) ** (1 / 2)).toFixed(2)

            //hc-index
            // sc=[]
            // hcIndex=0
            // for(var i=0;i<response.titles.length;i++){
            //     if(citations[i]!="" && years[i]!=""){
            //         sc.push((4/(currentYear-parseInt(years[i])+1))*parseInt(citations[i]))
            //     }
            // }
            // for (var i = 0; i < sc.length; i++) {
            //     if (i + 1 >= sc[i]) {
            //         hcIndex = i + 1
            //         break
            //     }
            // }
            // console.log(hcIndex)
            // console.log(sc)

            //hc-index(Not less than 1, coeff=4)
            // sc=[]
            // hcIndex=0
            // for(var i=0;i<response.titles.length;i++){
            //     if(citations[i]!="" && years[i]!=""){
            //         var temp=(currentYear-parseInt(years[i])+1)
            //         if(temp<=5){
            //         sc.push((5/temp)*parseInt(citations[i]))
            //         }
            //         sc.push(parseInt(citations[i]))
            //     }
            // }
            // for (var i = 0; i < sc.length; i++) {
            //     if (i + 1 >= sc[i]) {
            //         hcIndex = i + 1
            //         break
            //     }
            // }
            // console.log(hcIndex)
            // console.log(sc)



            // //Changes
            newCitations = response.citations.filter(Number)
            newYears = response.years.filter(Number)

            chrome.runtime.sendMessage({
                intent: 'sendToServer',
                scholarImage: response.image,
                scholarName: response.scholarName,
                workplace: response.workplace,
                pubCount: response.titles.length,
                citCount: sumCitations,
                hIndex: hIndex,
                gIndex: gIndex,
                mIndex: mIndex,
                oIndex: oIndex,
                hMedian: hMedian,
                eIndex: eIndex,
                titles: response.titles,
                citations: newCitations,
                coauthors: sanitized,
                years: newYears,
            }, function (response) {
                appendToPage(response)
            })
        }
        
        if (response.intent == "displayData") {
            appendToPage(response.data.data[0])
        }
    })
    

})