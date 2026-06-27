// Assignment 2.1 Javascript Excercises: Frances Yeboah P7

//1
function string_sum(str){
    digits = Array.from(str)
    sum = 0
    for(let i = 0; i < digits.length; i++){
        sum += Number(digits[i])
    }
    return sum
}
//2
function keep_evens(arr){
	return arr.filter((num) => num % 2 == 0)
}
//3
function age(obj){
	return obj.age > 40
}
//4
function find_max(arr){
	return arr.toSorted((a,b) => a-b)[arr.length-1]
}
//5
function find_max_min(arr){
	return {
		max: find_max(arr),
		min: arr.toSorted((a,b) => a-b)[0]
	}
}
//6
function sum_double(arr){
	sum = 0
    for(let i = 0; i < arr.length; i++){
        sum += Number(arr[i])
    }
    return 2 * sum
}
//7
function sum_double_evens (arr){
	sum = 0
    for(let i = 0; i < arr.length; i++){
		if(Number(arr[i]) % 2 == 0)
			sum += Number(arr[i])
    }
    return 2 * sum
}
//8
function capitalize_firsts(str){
	all_words = str.split(' ')
	empty = []
	for (const word of all_words){
		empty.push(word.charAt(0).toUpperCase()+word.slice(1))
	}
	return empty.join(' ')
}
//9
function longest_word(str){
	all_words = str.split(' ')
	return all_words.toSorted((a,b) => a.length - b.length)[all_words.length-1]
}
//10
function longest_shortest_word(str){
	all_words = str.split(' ')
	return {
		longest: all_words.toSorted((a,b) => a.length - b.length)[all_words.length-1],
		shortest: all_words.toSorted((a,b) => a.length - b.length)[0]
		}
}
//11
function digits_only(str){
    new_str = ""
    for (let i = 0; i < str.length; i++){
        if(! isNaN(str.charAt(i)) && str.charAt(i) != ' '){
            new_str += str.charAt(i)
        }
    }
    return Array.from(new_str)
}
//12
const addNumbersArrow = (num1, num2) => {
return num1 + num2;
};
//13
const makes10 = (a,b) => {
    return a + b == 10
};

//14
const person = { name: 'Paul', school: 'TJ', year: 2025 }
school = person.school
year = person.year

//15
function complimentCats(name, numCats) {
    return `Hello, ${name}. Did you know I have ${numCats} cats. It's a whole vibe.`
}