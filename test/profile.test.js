const puppeteer = require('puppeteer')
const extensionPath = 'src'

test('Test profile page redirect', async () =>{
    const browser = await puppeteer.launch({
        headless: false, // extension are allowed only in the head-full mode
        slowMo: 80,
        args: [
            '--window-size=1920,1080',
            `--disable-extensions-except=${extensionPath}`,
            `--load-extension=${extensionPath}`
        ]
    });
    const extensionID = 'pfgmjkmlifhekiegffjndhpioapgcopk'
    const extensionPopupHtml = 'views/popup.html'
    const page = await browser.newPage();
    await page.goto(`chrome-extension://${extensionID}/${extensionPopupHtml}`);
    const newPagePromise = new Promise(resolve => browser.once('targetcreated', target => resolve(target.page())));
    await page.click('button#searchBtn');
    const newPage = await newPagePromise;
    const testData = await newPage.$eval('.sidenav h3', el=>el.innerText);
    await newPage.close();
    await browser.close();
    expect(testData).toBe('Publications');
},10000);