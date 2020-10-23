let environment = process.env.environment
let testPathIgnorePatterns = []

if (environment === 'unitonly') testPathIgnorePatterns = ['profile.test.js']
if (environment === 'eeonly') testPathIgnorePatterns = ['metrics.test.js']

module.exports = {
    preset: 'jest-puppeteer',
    testPathIgnorePatterns,
    verbose: true,
    testEnvironment: 'jsdom',
}
