let form = document.getElementById("enquiryForm");
form.addEventListener("submit", function(event) {
event.preventDefault();
    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let mobile = document.getElementById("mobile").value.trim();
    let department = document.getElementById("department").value;
    let branch = document.getElementById("branch").value;
    let message = document.getElementById("message").value.trim();
    if (name === "") {
        alert("Please enter your name");
    }
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        alert("Please enter a valid email");
    }
    else if (!/^[0-9]{10}$/.test(mobile)) {
        alert("Enter a valid 10 digit mobile number");
    }
    else if (department === "") {
        alert("Please select your department");
    }
    else if (branch === "") {
        alert("Please select your branch");
    }
    else if (message.length < 10) {
        alert("Message must contain at least 10 characters");
    }
    else {
        alert("Student enquiry submitted successfully!");

        form.reset();
    }

});
