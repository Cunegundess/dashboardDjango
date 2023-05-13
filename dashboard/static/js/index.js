function submitForm() {
    var form = document.getElementById("formNovaEmpresa");
    var formData = new FormData(form);
    formData.append("csrfmiddlewaretoken", "{ csrf_token }");
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "{% url 'novaempresa' %}", true);
    xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText);
        }
    };
    xhr.send(formData);
}

const cnpjInput = document.getElementById('cnpjInput');
  
  // add an event listener to the input field
  cnpjInput.addEventListener('input', (event) => {
    const { value } = event.target;
    // remove any non-numeric characters from the input
    const cleanedValue = value.replace(/\D/g, '');
    
    // format the cleaned value as a CNPJ with dots and dashes
    const formattedValue = cleanedValue.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})$/, '$1.$2.$3/$4-$5');
    
    // set the input field value to the formatted value
    event.target.value = formattedValue;
  });