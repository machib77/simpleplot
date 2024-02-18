console.log("JavaScript AGAIN!")

function initialRates() {
    let num1 = 1;
    let num2 = 3;
    let num3 = 7;

    document.getElementById('number1').value = num1;
    document.getElementById('number2').value = num2;
    document.getElementById('number3').value = num3;

    console.log(num1, num2, num3);

    let inputElement = document.getElementById('number1');
    // Simulate an input event
    inputElement.dispatchEvent(new Event('change'));
    
}

window.addEventListener('load', initialRates)

