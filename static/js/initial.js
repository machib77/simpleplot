function initialRates() {

    let init_obj = {
        '1Y': 1.0,
        '2Y': 3.0,
        '3Y': 4.0,
        '4Y': 4.5,
        '5Y': 4.8,
        '6Y': 5.0,
        '7Y': 5.1,
        '8Y': 5.2,
        '9Y': 5.3,
        '10Y':5.35,
    }

    for (let key in init_obj) {
        // console.log(`Key: ${key}, Value: ${parseFloat(init_obj[key]).toFixed(2)}`)
        document.getElementById(key).value = parseFloat(init_obj[key]).toFixed(2);
    }



    let inputElement = document.getElementById('1Y');
    // Simulate an input event
    inputElement.dispatchEvent(new Event('change'));
    
}

window.addEventListener('load', initialRates)

