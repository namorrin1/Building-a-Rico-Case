// this is the most basic test case you can have, just to make sure your test environment is set up correctly.
// in the frontend folder, you should be able to run 'npm test' to verify.
// a 'coverage' folder will be created in the 'frontend' folder that shows test results.

const sum = require('../sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});