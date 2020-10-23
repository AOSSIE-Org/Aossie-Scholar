const { getHindex, getEindex } = require('../src/js/profile')

const citationArray = [69, 20, 19, 17, 10, 6, 5, 3, 2, 1, 1, 1]
test('get h-index as 6', () => {
    expect(getHindex(citationArray)).toBe(6)
})

test('get e-index as 10.86', () => {
    const hIndex = getHindex(citationArray)
    expect(getEindex(citationArray, hIndex)).toBe(10.86)
})
