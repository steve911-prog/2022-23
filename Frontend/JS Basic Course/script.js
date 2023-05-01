// //console.log("hello from script.jj");
// //12:13

// //let age = 25;
// //console.log(age);
// //const salary = 6000000;
// //console.log(salary);

// //let sum;
// //sum = 5;
// //console.log(sum);
// //19:00

// const name = "Vladdie";
// const language = "JS";
// const channel = "Codevolution";

// const total = 0;
// const PI = 3.14;

// const isPrimaryNumberv = true;
// const isNewUser = false;

// let result;
// console.log(result);

// const res = null;
// //22:10

// const data = null;

// //

// const person = {
//   firstName: "Bruce",
//   lastName: "Wayne",
//   age: 30,
// };

// console.log(person.firstName);

// const oddNumbers = [1, 3, 5, 7, 9];

// console.log(oddNumbers[0]);

//Assignment Operators
//Comparsion Operators

//let x = 10;
//let y = 5;
//console.log(y % x);
//console.log(x++,++x, --y)

//console.log(x != y);
/* console.log(x === y);
console.log(x !== y);
console.log(x >= y); */

//const isValidNumber  = x > 8 && 8 < y;//&& - and
//const isValidNumber = x > 8 || 8 < y; //|| - or
//const isValidNumber = true; //|| - or
//console.log(!isValidNumber);

//str
//console.log("Bruce " + "Wayne");

//const isEven = 10 % 2 === 0 ? true : false; // If condition is true it
//returns true, else - false. Instead of false or true can be any other
//strings numbers, whatever

//console.log(isEven);

//Type Conversions
//Implicit one   (neyavnoe preobrazoavanie)
//console.log(2 + "3"); //result will be "23"
//console.log(true + "3"); //result will be "true3"
// console.log("2" + "3"); //result will be "23", but
// console.log("2" - "3"); //result will be -1
//NaN - Not a Number
//console.log("2" - true); //result will be 1, if false - 2

//console.log(5 + undefined)//Nan

//Explicit - yavnoe
//console.log(Number("6")); //converts to anumber
//console.log(parseInt("6")); //converts to anumber
//console.log(parseFloat("6.08")); //converts to afloat
// console.log(String(6)); //converts to astring
// console.log(50.0.toString()); //converts to astring "50"

//console.log(Boolean(7.0));//truuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuhhhhhaaaaahhhhaaahahaha
//false - null undefined 0 '' NaN

//Equality - ravenstvo
//coercion nasilie
//allows coercion
// const var1 = "t*st"
// const var2 = ["t*st"]

// console.log(var1 == var2);
// console.log(var1 === var2);

//Conditional statements
// const num = -5;

// if (num > 0) {
//   console.log("Number is positive");
// } else if (num < 0) {
//   console.log("Number is not negative");
// } else {
//   console.log("Num is zero");
// }

// const color = "red";

// switch (color) {
//   case "red":
//     console.log("r*d");
//     break;
//   case "blue":
//     console.log("blue");
//     break;
//   default:
//     console.log("Not a valid color");
// }

//Looping code
//for loop

// for (let i = 1; i <= 5; i++) {
//   console.log(i);
// }
//While loop

// let i = 1
// while(i<=5){
//     console.log("Iteration number" + i);
//     i++
// }

//Do..While loop
// let i = 1;
// do {
//     console.log("Iteration number " + i);
//     i++

// }   while (i<=5)

//For..of loop

// const numArray = [1, 2, 3, 4, 5];

// for (const num of numArray) {
//   console.log("Iteration " + num);
// }

//Functions
// function greet(user) {
//   console.log("Good morning! + " + user);
// }

// greet("M*sha");

// function add(a, b) {
//   console.log(a + b);
//   return a + b;
// }

// add("5", 6);

// const arrowSum = (a, b) => {
//   console.log(a + b);
//   return a + b;
// };

// arrowSum(5, 6);

//Scope masshtab determine opredelat

// const myNum = 10;
// const myName = "Hi";
// if (true) {
//   const myName = "Vishwas";
//   console.log(myName);
//   console.log(myNum); //IT IS OUTFUNCCTIONS
// }
//console.log(myName);

// function testFn() {
//     const myName = "Bis*kek"
// }
// console.log(myName);

// testFn();
