async function addCustomer() {
    let customer = {
        name: document.getElementById('name').value,
        age: document.getElementById('age').value,
        gender: document.getElementById('gender').value,
        address: document.getElementById('address').value,
        phone: document.getElementById('phone').value,
        adhaar_no: document.getElementById('adhaar_no').value,
        pin: document.getElementById('pin').value,
        balance: document.getElementById('balance').value
    };

    let response = await fetch('/add_customer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(customer)
    });

    let result = await response.json();
    alert(result.message);
}

async function deposit() {
    let data = {
        account_id: document.getElementById('deposit_account_id').value,
        amount: document.getElementById('deposit_amount').value
    };

    let response = await fetch('/deposit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    let result = await response.json();
    alert(result.message);
}

async function withdraw() {
    let data = {
        account_id: document.getElementById('withdraw_account_id').value,
        amount: document.getElementById('withdraw_amount').value
    };

    let response = await fetch('/withdraw', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    let result = await response.json();
    alert(result.message);
}

