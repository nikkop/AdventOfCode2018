const nums = [1, 2, 3, 4, 5];
const raised = nums
    .map(num => Math.pow(num, num))
    .filter(num => num % 2 === 0);

