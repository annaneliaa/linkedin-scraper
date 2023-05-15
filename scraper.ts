import * as puppeteer from 'puppeteer';
var fs = require('fs'); 

const LI_AT = 'AQEDAUMeSlEFOGavAAABh-NMiI8AAAGIK2bTiE0ASl8Tu-FSEVXXMhWE11lL9x49Ns2gxl0BWLESGMNLl23V5XJE38eFM4al5s4AWXJwqeq0f1_5YOCYJqJH4IMBC2_wh51hSTGGiuc42PmEupo4gV5A'

const sleep = (ms: number) => new Promise(r => setTimeout(r, ms));

(async () => {
    const browser = await puppeteer.launch({
        headless: false,
        executablePath: '/opt/homebrew/bin/chromium'
      })    
    const page = await browser.newPage();

    // trying to get the cookie out of the browser
    const cookie = process.env.LINKEDIN_ACCESS_TOKEN
    console.log(cookie)

    await page.setCookie({
        name: 'li_at',
        value: LI_AT,
        domain: 'www.linkedin.com',
        path: '/',
        expires: Date.now() + 1000 * 60 * 60 * 24 * 365
    })

    const url = 'https://www.linkedin.com/in/annavisman/'

    await page.goto(url);
    await page.setViewport({
        width: 1200,
        height: 800
    });

    page.evaluate(() => {
        window.scrollBy(0, window.innerHeight);
      });

    await sleep(10000);

    await page.screenshot({
        path: 'profile.png',
        fullPage: true
    });

    await page.pdf({path: 'linkedin.pdf'});
    
    await sleep(10000);

    await browser.close();
})();


