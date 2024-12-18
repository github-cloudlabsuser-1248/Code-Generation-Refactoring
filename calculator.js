function divide(a, b) {
    if (b === 0) {
        return "Error: Division by zero";
    }
    return a / b;
}
// Function to perform addition
function add(a, b) {
    return a + b;
}

// Function to perform subtraction
function subtract(a, b) {
    return a - b;
}

// Function to perform multiplication
function multiply(a, b) {
    return a * b;
}

// Function to perform division
function divide(a, b) {
    if (b === 0) {
        return "Error: Division by zero";
    }
    return a / b;
}


// Function to get user input and perform the selected operation
function calculator() {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    readline.question("Choose an operation: add, subtract, multiply, divide\n", (operation) => {
        readline.question("Enter the first number:\n", (num1) => {
            readline.question("Enter the second number:\n", (num2) => {
                const a = parseFloat(num1);
                const b = parseFloat(num2);

                let result;
                switch (operation) {
                    case "add":
                        result = add(a, b);
                        break;
                    case "subtract":
                        result = subtract(a, b);
                        break;
                    case "multiply":
                        result = multiply(a, b);
                        break;
                    case "divide":
                        result = divide(a, b);
                        break;
                    default:
                        result = "Invalid operation";
                }

                console.log("The result is: " + result);
                readline.close();
            });
        });
    });
}

// Run the calculator
calculator();