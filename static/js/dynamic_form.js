// Configuration object for the form fields
const formConfig = {
  questions: [
    {
      label: "Name",
      type: "text",
      name: "name",
      placeholder: "Enter your name",
    },
    {
      label: "Email",
      type: "email",
      name: "email",
      placeholder: "Enter your email",
    },
    {
      label: "Age",
      type: "number",
      name: "age",
      placeholder: "Enter your age",
    },
    {
      label: "Agree to Terms",
      type: "checkbox",
      name: "agree",
      text: "I agree to the terms and conditions",
    },
    {
      label: "Comments",
      type: "textarea",
      name: "comments",
      placeholder: "Enter your comments",
    },
    {
      label: "Upload Images",
      type: "file",
      name: "images",
      accept: "image/*",
      multiple: true,
    },
  ],
};

// Function to handle form submission
function handleSubmit(event) {
  event.preventDefault(); // Prevent the default form submission behavior

  const form = event.target; // Get the form element

  // Get the form data
  const formData = new FormData(form);

  // Get the signature data
  const signatureData = signaturePad.toDataURL();
  formData.append('signature', signatureData); // Add the signature data to the form data

  // Send the form values to the Flask endpoint
  fetch("/", {
    method: "POST",
    body: formData, // Send form data as multipart/form-data
  })
    .then((response) => response.text())
    .then((data) => {
      console.log(data);
      // Handle the response here (e.g., show a success message)
    })
    .catch((error) => {
      console.error("Error:", error);
      // Handle errors here (e.g., show an error message)
    });
}



// Function to generate the form dynamically
function generateForm() {
  const formContainer = document.getElementById("dynamic-form-container");

  // Create the form element
  const form = document.createElement("form");
  form.id = "dynamic-form"; // Assign an ID to the form
  form.addEventListener("submit", handleSubmit); // Add event listener for form submission

  // Create form fields based on the configuration object
  formConfig.questions.forEach((question) => {
    const { label, type, name, placeholder, text, accept, multiple } = question;

    // Create the label element
    const labelElem = document.createElement("label");
    labelElem.textContent = label;

    // Create the input element based on the field type
    let inputElem;
    if (type === "checkbox") {
      inputElem = document.createElement("input");
      inputElem.type = "checkbox";
      inputElem.name = name;
      inputElem.id = name;
      inputElem.value = "true";

      // Create a label for the checkbox
      const checkboxLabel = document.createElement("label");
      checkboxLabel.textContent = text;
      checkboxLabel.setAttribute("for", name);

      // Append the checkbox and its label to the form
      form.appendChild(inputElem);
      form.appendChild(checkboxLabel);
    } else if (type === "textarea") {
      inputElem = document.createElement("textarea");
      inputElem.name = name;
      inputElem.placeholder = placeholder;

      // Append the textarea to the form
      form.appendChild(inputElem);
    } else if (type === "file") {
      inputElem = document.createElement("input");
      inputElem.type = "file";
      inputElem.name = name;
      inputElem.accept = accept;
      inputElem.multiple = multiple;

      // Append the file input to the form
      form.appendChild(inputElem);
    } else {
      inputElem = document.createElement("input");
      inputElem.type = type;
      inputElem.name = name;
      inputElem.placeholder = placeholder;

      // Append the input to the form
      form.appendChild(inputElem);
    }

    // Create a line break element
    const brElem = document.createElement("br");

    // Append the label, input, and line break elements to the form
    form.appendChild(labelElem);
    form.appendChild(brElem);
  });

    // Create the signature canvas
    const canvas = document.createElement("canvas");
    canvas.id = "signatureCanvas";
    canvas.width = 400;
    canvas.height = 200;
  
    // // Create the signature file input field
    // const signatureInput = document.createElement("input");
    // signatureInput.type = "file";
    // signatureInput.id = "signatureInput";
    // signatureInput.name = "signature";
  
    // Append the canvas and signature input to the form
    form.appendChild(canvas);
    // form.appendChild(signatureInput);
    
  // Create the submit button
  const submitButton = document.createElement("button");
  submitButton.type = "submit";
  submitButton.textContent = "Submit";

  // Append the submit button to the form
  form.appendChild(submitButton);

  // Append the form to the form container
  formContainer.appendChild(form);
}

// Call the function to generate the form
generateForm();

// Automatically save the signature when the form is submitted
document.getElementById('dynamic-form').addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent the default form submission behavior

  const form = event.target; // Get the form element

  // Get the form data
  const formData = new FormData(form);

  // Get the signature data
  const signatureData = signaturePad.toDataURL();
  formData.append('signature', signatureData); // Add the signature data to the form data

  // Send the form values to the Flask endpoint
  fetch("/", {
    method: "POST",
    body: formData, // Send form data as multipart/form-data
  })
    .then((response) => response.text())
    .then((data) => {
      console.log(data);
      // Handle the response here (e.g., show a success message)
    })
    .catch((error) => {
      console.error("Error:", error);
      // Handle errors here (e.g., show an error message)
    });
});

