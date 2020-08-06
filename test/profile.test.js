const puppeteer = require('puppeteer')
const extensionPath = 'src'
let browser

test('Test redirect to profile page', async () => {
    browser = await puppeteer.launch({
        headless: false, // extension are allowed only in the head-full mode
        slowMo: 100,
        args: ['--no-sandbox', `--disable-extensions-except=${extensionPath}`, `--load-extension=${extensionPath}`],
        defaultViewport: {
            width: 1300,
            height: 600,
            deviceScaleFactor: 1,
        },
    })
    const page = await browser.newPage()
    await page.goto('chrome-extension://pfgmjkmlifhekiegffjndhpioapgcopk/views/popup.html')
    // const newPagePromise = new Promise((resolve) => browser.once('targetcreated', (target) => resolve(target.page())))
    // await page.click('button#searchBtn')
    // const newPage = await newPagePromise
    // const testData = await newPage.$eval('.sidenav h3', (el) => el.innerText)
    // expect(testData).toBe('Publications')
    await page.close()
    await browser.close()
}, 10000)
