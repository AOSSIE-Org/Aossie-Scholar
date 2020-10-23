module.exports = {
    preset: 'jest-puppeteer',
    testPathIgnorePatterns: ['/node_modules/'],
    testMatch: ['**/test/*.test.js'],
    verbose: true,
}
