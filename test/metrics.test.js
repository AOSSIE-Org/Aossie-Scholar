const {
    getHindex,
    getEindex,
    getTotalCitations,
    getGindex,
    getMindex,
    getOindex,
    getHmedian,
} = require('../src/js/profile')

const citationArray = [69, 20, 19, 17, 10, 6, 5, 3, 2, 1, 1, 1]
const years = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031]
test('get h-index as 6', () => {
    expect(getHindex(citationArray)).toBe(6)
})

test('get e-index as 10.86', () => {
    const hIndex = getHindex(citationArray)
    expect(getEindex(citationArray, hIndex)).toBe(10.86)
})

test('get total citations as 154', () => {
    expect(getTotalCitations(citationArray)).toBe(154)
})

test('get g-index as 12', () => {
    expect(getGindex(citationArray)).toBe(12)
})

test('get m-index as 6.00', () => {
    const hIndex = getHindex(citationArray)
    expect(getMindex(years, hIndex)).toBe('6.00')
})

test('get o-index as 20.35', () => {
    const hIndex = getHindex(citationArray)
    expect(getOindex(citationArray, hIndex)).toBe('20.35')
})

test('get h-median as 19', () => {
    const hIndex = getHindex(citationArray)
    expect(getHmedian(citationArray, hIndex)).toBe(19)
})
