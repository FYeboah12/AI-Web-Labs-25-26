const students = [
    { name: "Alice", dob: "2006-02-15", courses: "Calculus,Astronomy", grades: "A,B" },
    { name: "Bob", dob: "2005-07-02", courses: "History,Calculus,Art", grades: "C,A,B" },
    { name: "Carla", dob: "2006-02-21", courses: "Biology,Calculus,Philosophy", grades: "B,B,A" },
    { name: "Derek", dob: "2005-12-30", courses: "Calculus,Chemistry", grades: "A,C" },
    { name: "Ella", dob: "2006-02-03", courses: "Physics,Art,Calculus", grades: "A,A,A" },
    { name: "Farah", dob: "2006-01-15", courses: "History,English", grades: "B,C" },
    { name: "George", dob: "2005-11-11", courses: "Calculus,English", grades: "C,B" },
    { name: "Hana", dob: "2006-02-28", courses: "Philosophy,Calculus", grades: "B,A" },
    { name: "Ian", dob: "2006-03-01", courses: "Calculus,History", grades: "A,A" },
    { name: "Jade", dob: "2006-02-08", courses: "Astronomy,Calculus,Art", grades: "B,B,C" },
  ];

// -------- PROBLEMS -------- //

//  ----------------------
//  Problem 1
// 
//  generate/return a list of all students names
let names = students.map(student => student.name)
console.log(1)
console.log(names)

//  ----------------------
//  Problem 2
// 
//  generate/return a list of all student data objects for students born in February
//console.log(student[0].dob.split('-')[1])
let febs = students.filter(student => student.dob.split('-')[1] == '02')
console.log(2)
console.log(febs)

//  ----------------------
//  Problem 3
// 
//  generate/return a list of all student names for students born in February
let febsNames = febs.map(student => student.name)
console.log(3)
console.log(febsNames)

//  ----------------------
//  Problem 4
// 
//  generate/return a list of all student names for students born in February and took Calculus
let febsNamesCalc = febs.filter(student => student.courses.includes('Calculus'))
febsNamesCalc = febs.map(student => student.name)
console.log(4)
console.log(febsNamesCalc)

//  ----------------------
//  Problem 5
// 
//  generate/return a list of grades (disassociated from student names etc, just list of grades)
//    for students born in February and took Calculus
let febsCalcGrades = febs.filter(student => student.courses.includes('Calculus'))
febsCalcGrades = febs.map(student => student.grades)
console.log(5)
console.log(febsCalcGrades)

//  ----------------------
//  Problem 6
// 
//  Create an object that can help you convert letter grades to GPAs (A=4, B=3, C=2, D=1, F=0)
//    and return a list of GPAs for the students
//gpa is sum of grades div by classes
const lettersToGrades = {"A":4,"B":3,"C":2,"D":1}
allGrades = students.map(student => student.grades)
allGrades = allGrades.map(grade => grade.split(','))
for(let i =0; i < allGrades.length; i++){
    allGrades[i] = allGrades[i].map(grade => lettersToGrades[grade])
    allGrades[i] = allGrades[i].reduce((acc, cur) => acc + cur) / allGrades[i].length
}
// gpas = allGrades.map(grade => lettersToGrades[grade.split(',')])
console.log(6)
console.log(allGrades)
//---------------------------------
//  Problem 7
// 
//  Using the object that can help you convert letter grades to GPAs (A=4, B=3, C=2, D=1, F=0)
//    and return a list of objects {name: ..., gpa: ...}
const lettersToGrades = {"A":4,"B":3,"C":2,"D":1}
allGrades = students.map(student => student.grades)
allGrades = allGrades.map(grade => grade.split(','))
for(let i =0; i < allGrades.length; i++){
    allGrades[i] = allGrades[i].map(grade => lettersToGrades[grade])
    allGrades[i] = allGrades[i].reduce((acc, cur) => acc + cur) / allGrades[i].length
}
// gpas = allGrades.map(grade => lettersToGrades[grade.split(',')])
console.log(6)
console.log(allGrades)

// -------- PUZZLES -------- //

// Who has the highest average grade among Calculus students? (Hint: reduce)

// How many total As have been earned by students born in February?

// Return the youngest student who has taken Philosophy.

// Which course has the most students enrolled?

// -------- Final Challenge -------- //
//
// Find/return the average GPA of all students born in February who took Calculus