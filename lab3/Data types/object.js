function sumSalaries(salaries) {
    return Object.values(salaries).reduce((a, b) => a + b, 0) // 650
} 


function count(obj) {
    return Object.keys(obj).length;
}
