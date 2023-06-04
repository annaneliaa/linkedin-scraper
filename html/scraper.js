"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const LI_AT = 'AQEDAUMeSlEFOGavAAABh-NMiI8AAAGIK2bTiE0ASl8Tu-FSEVXXMhWE11lL9x49Ns2gxl0BWLESGMNLl23V5XJE38eFM4al5s4AWXJwqeq0f1_5YOCYJqJH4IMBC2_wh51hSTGGiuc42PmEupo4gV5A';
const puppeteer = __importStar(require("puppeteer"));
var fs = require('fs');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(() => __awaiter(void 0, void 0, void 0, function* () {
    const browser = yield puppeteer.launch({
        headless: false,
        executablePath: '/opt/homebrew/bin/chromium'
    });
    const page = yield browser.newPage();
    const cookie = process.env.LINKEDIN_ACCESS_TOKEN;
    console.log(cookie);
    yield page.setCookie({
        name: 'li_at',
        value: LI_AT,
        domain: 'www.linkedin.com',
        path: '/',
        expires: Date.now() + 1000 * 60 * 60 * 24 * 365
    });
    const url = 'https://www.linkedin.com/in/annavisman/';
    yield page.goto(url);
    yield page.setViewport({
        width: 1200,
        height: 800
    });
    page.evaluate(() => {
        window.scrollBy(0, window.innerHeight);
    });
    yield sleep(10000);
    yield page.screenshot({
        path: 'profile.png',
        fullPage: true
    });
    yield page.pdf({ path: 'linkedin.pdf' });
    yield sleep(10000);
    yield browser.close();
}))();
