let environment = process.env.environment
let testMatch = []

if (environment === 'unitonly') testMatch = ['**/test/metrics.test.js']
if (environment === 'eeonly') testMatch = ['**/test/profile.test.js']

module.exports = {
    preset: 'jest-puppeteer',
    testPathIgnorePatterns: ['/node_modules/'],
    testMatch: ['**/test/*.test.js'],
    verbose: true,
    testEnvironment: 'jsdom',
}
