// function submitForm() {
//     var form = document.getElementById("formNovaEmpresa");
//     var formData = new FormData(form);
//     formData.append("csrfmiddlewaretoken", "{ csrf_token }");
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", "{% url 'novaempresa' %}", true);
//     xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
//     xhr.onreadystatechange = function() {
//         if (xhr.readyState === 4 && xhr.status === 200) {
//             console.log(xhr.responseText);
//         }
//     };
//     xhr.send(formData);
// }